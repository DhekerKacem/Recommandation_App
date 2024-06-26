# Recommandation_App
Réalisez une application de recommandation de contenu
Présentation du projet
My Content est une start-up qui veut encourager la lecture en recommandant des contenus pertinents pour ses utilisateurs. 
Avec la co-fondatrice nous souhaitons tester une solution de recommandation d’articles et de livres à des particuliers.
Comme nous ne disposons pas de données utilisateurs, nous allons utiliser les données disponibles sur www.kaggle.com/datasets/gspmoreira/news-portal-user-interactions-by-globocom/data pour développer notre MVP (Minimum Viable Product).
Ces données représentent les interactions des utilisateurs avec les articles disponibles. Elles contiennent des informations sur les articles (par exemple le nombre de mots dans l’article), ainsi que les informations sur les sessions des utilisateurs (par exemple heures de début et de fin) et les interactions des utilisateurs avec les articles (sur quel article l’utilisateur a-t-il cliqué lors de sa session ?).
Dans une logique MVP nous avons identifié la fonctionnalité la plus critique pour lancer votre application :  "En tant qu’utilisateur de l’application, je vais recevoir une sélection de cinq articles."
Nous avons, également, identifié que la prise en compte de l’ajout de nouveaux utilisateurs et de nouveaux articles dans l’architecture cible de votre produit est déterminante. 
Présentation des données
L’ensemble de données contient un échantillon d’interactions d’utilisateurs (pages vues) sur le portail d’actualités G1 du 1er au 16 octobre 2017, y compris environ 3 millions de clics, répartis en plus d’un million de sessions de 314 000 utilisateurs qui ont lu plus de 46 000 articles de presse différents au cours de cette période.
Il est composé de trois fichiers/dossiers :
- clicks.zip : Dossier contenant des fichiers CSV (un par heure), contenant les interactions des sessions utilisateurs dans le portail d’actualités.
- articles_metadata.csv : Fichier CSV contenant des informations sur tous les articles publiés (364047).
- articles_embeddings.pickle : une matrice NumPy contenant les plongements de contenu de l’article (vecteurs à 250 dimensions), entraînée sur le texte des articles.
- clicks_sample.csv : fichier CSV contenant un échantillon des interactions des sessions des utilisateurs.

