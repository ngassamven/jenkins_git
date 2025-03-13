import pandas as pd

# Charger les données extraites
data = pd.read_csv('extracted_data.csv')

# Exemple de transformation : normalisation d'une colonne
data['colonne_normalisee'] = data['Budget (FCFA)'].apply(lambda x: x / 1000)

data.to_csv('transformed_data.csv', index=False)
print("Données transformées avec succès !")
