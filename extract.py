import pandas as pd

try:
    # Lecture du fichier CSV
    data = pd.read_csv('campaigns.csv')
    data.to_csv('extracted_data.csv', index=False)
    print("✅ Données extraites avec succès !")
except FileNotFoundError:
    print("❌ Erreur : Le fichier campaigns.csv est introuvable.")
    exit(1)
except Exception as e:
    print(f"❌ Erreur lors de l'extraction : {e}")
    exit(1)
