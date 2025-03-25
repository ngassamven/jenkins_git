import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import os

# Paramètres de connexion sécurisés (utilisation des variables d'environnement)
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '271994')  # Remplacez par os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'mydatabase')

try:
    # Charger les données transformées
    data = pd.read_csv("transformed_data.csv")
    print("✅ Fichier CSV chargé avec succès !")
except FileNotFoundError:
    print("❌ Erreur : Le fichier transformed_data.csv est introuvable.")
    exit(1)

# Connexion à PostgreSQL
try:
    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    
    with engine.connect() as connection:
        print("✅ Connexion réussie à la base de données PostgreSQL !")

        # Charger les données dans une table PostgreSQL
        data.to_sql('ma_table', con=engine, if_exists='replace', index=False)
        print("✅ Données chargées dans la base de données avec succès !")

except Exception as e:
    print(f"❌ Erreur de connexion à la base de données : {e}")
    exit(1)
