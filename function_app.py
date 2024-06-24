import azure.functions as func
import logging
import pickle
import os
from surprise import dataset

app = func.FunctionApp()

@app.route(route="recommandation_api", auth_level=func.AuthLevel.ANONYMOUS)
def RecommanderApi(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Définir le chemin d'accès
    path = os.path.join('azure_collaborative', 'model_COFI.pkl')

    # Charger le modèle depuis le fichier
    with open(path, 'rb') as f:
        loaded_model = pickle.load(f)

    # Chemins relatifs aux fichiers de données et de modèle
    data_path = os.path.join('azure_collaborative', 'ratings.pkl')

    # Charger les données de notations
    with open(data_path, 'rb') as data_file:
        ratings = pickle.load(data_file)

    # Obtenir les recommandations pour un utilisateur spécifique
    user_id = req.params.get("user-id")
    recommended_articles = recommend_articles(user_id, loaded_model, ratings)
    
    print(f"Articles recommandés pour l'utilisateur {user_id}: {recommended_articles}")
    return func.HttpResponse(
        recommend_articles, status_code=200
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