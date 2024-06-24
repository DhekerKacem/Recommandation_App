import streamlit as st
import requests
import json

# URL de l'API de recommandation
API_URL = "https://recommanderapi.azurewebsites.net/api/recommandation_api"

# Titre de l'application
st.title("Recommandation d'Articles")

# Entrée pour le user_id
user_id = st.text_input("Entrez l'ID utilisateur", "")

# Bouton pour obtenir les recommandations
if st.button("Obtenir des recommandations"):
    if user_id:
        try:
            # Appel à l'API de recommandation
            response = requests.get(API_URL, params={"user_id": user_id})

            # Vérification de la réponse de l'API
            if response.status_code == 200:
                recommendations = response.json()
                st.success(f"Articles recommandés pour l'utilisateur {user_id} :")
                for article_id in recommendations:
                    st.write(f"Article ID: {article_id}")
            else:
                st.error(f"Erreur {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Erreur lors de l'appel de l'API: {str(e)}")
    else:
        st.warning("Veuillez entrer un ID utilisateur valide.")
