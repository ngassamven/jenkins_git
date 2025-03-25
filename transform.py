import pandas as pd

try:
    # Charger les données extraites
    data = pd.read_csv('extracted_data.csv')

    # Vérifier si la colonne existe avant transformation
    if 'Budget (FCFA)' in data.columns:
        data['colonne_normalisee'] = data['Budget (FCFA)'].apply(lambda x: x / 1000)
        data.to_csv('transformed_data.csv', index=False)
        print("✅ Données transformées avec succès !")
    else:
        print("❌ Erreur : La colonne 'Budget (FCFA)' est introuvable dans le fichier.")
        exit(1)
except FileNotFoundError:
    print("❌ Erreur : Le fichier extracted_data.csv est introuvable.")
    exit(1)
except Exception as e:
    print(f"❌ Erreur lors de la transformation : {e}")
    exit(1)
