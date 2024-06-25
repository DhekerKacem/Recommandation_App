import logging
import azure.functions as func
import pickle
import os
import json
import numpy as np

app = func.FunctionApp()
# Définir le chemin d'accès pour le modèle et les données
model_path = os.path.join('azure_collaborative', 'model_COFI.pkl')
data_path = os.path.join('azure_collaborative', 'ratings.pkl')

# Charger le modèle depuis le fichier
with open(model_path, 'rb') as f:
    loaded_model = pickle.load(f)

# Charger les données de notations
with open(data_path, 'rb') as data_file:
    ratings = pickle.load(data_file)

@app.route(route="recommandation_api", auth_level=func.AuthLevel.ANONYMOUS)
def RecommanderApi(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    

    # Obtenir les recommandations pour un utilisateur spécifique
    user_id = req.params.get("user_id")
    if not user_id:
        return func.HttpResponse(
            "Veuillez passer un user_id en paramètre.",
            status_code=400
        )

    user_id = int(user_id)
    recommended_articles = recommend_articles(user_id, loaded_model, ratings)
    
    # Convertir les valeurs int64 en int
    recommended_articles = [int(article_id) for article_id in recommended_articles]

    logging.info(f"Articles recommandés pour l'utilisateur {user_id}: {recommended_articles}")

    return func.HttpResponse(
        body=json.dumps(recommended_articles),
        mimetype="application/json",
        status_code=200
    )
    
# Exemple de fonction pour faire des recommandations
def recommend_articles(user_id, model, df, n=5):
    all_articles = df['article_id'].unique()
    rated_articles = df[df['user_id'] == user_id]['article_id'].values
    unrated_articles = [article for article in all_articles if article not in rated_articles]
    predictions = [model.predict(user_id, article) for article in unrated_articles]
    sorted_predictions = sorted(predictions, key=lambda x: x.est, reverse=True)
    recommended_article_ids = [pred.iid for pred in sorted_predictions[:n]]
    return recommended_article_ids