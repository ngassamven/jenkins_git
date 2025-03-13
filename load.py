import pandas as pd
from sqlalchemy import create_engine
import psycopg2  # Ajout de l'import du module nécessaire

# Paramètres de connexion à PostgreSQL (remplacez ces valeurs par les vôtres)
DB_USER = "postgres"
DB_PASSWORD = "271994"  # ⚠️ Mettez ce mot de passe dans une variable d'environnement pour plus de sécurité
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "mydatabase"

# Charger les données transformées
try:
    data = pd.read_csv("transformed_data.csv")
    print("Fichier CSV chargé avec succès !")
except FileNotFoundError:
    print("Erreur : Le fichier transformed_data.csv est introuvable.")
    exit(1)

# Connexion à PostgreSQL
try:
    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    with engine.connect() as connection:
        print("Connexion réussie à la base de données PostgreSQL !")
        
        # Charger les données dans une table PostgreSQL
        data.to_sql('ma_table', con=engine, if_exists='replace', index=False)
        print("Données chargées dans la base de données avec succès !")

except Exception as e:
    print(f"Erreur de connexion à la base de données : {e}")
    exit(1)
