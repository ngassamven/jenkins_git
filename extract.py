import pandas as pd

# Exemple d'extraction d'un fichier CSV
data = pd.read_csv('campaigns.csv')
data.to_csv('extracted_data.csv', index=False)
print("Données extraites avec succès !")
