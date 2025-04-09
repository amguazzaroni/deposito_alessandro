import pandas as pd

#percorso del file CSV
file_path = 'vendite.csv'

#caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime righe del DtaFrame per confermare
print(df.head())