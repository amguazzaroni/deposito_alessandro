import numpy as np
import pandas as pd

data_vendite = {
    "Prodotto": ["Laptop", "Smartphone", "Tablet", "Laptop", "Monitor", "Stampante", "Smartphone", "Tablet", "Monitor", "Laptop", "Stampante", "Tablet", "Smartphone", "Monitor", "Laptop"],
    "Quantità": [3, 7, 4, 2, 5, 3, 6, 8, 1, 4, 2, 6, 5, 3, 2],
    "Prezzo Unitario": [1000, 600, 400, 950, 300, 150, 620, 390, 310, 1050, 140, 420, 610, 320, 980],
    "Città": ["Milano", "Roma", "Torino", "Napoli", "Milano", "Bologna",
        "Roma", "Napoli", "Firenze", "Firenze", "Bologna", "Milano",
        "Torino", "Roma", "Napoli"]
}

df = pd.DataFrame(data_vendite)
print(df)

#aggiungo nuova colonna
df['Totale vendite'] = df['Quantità'] * df['Prezzo Unitario']

#raggruppo i dati per prodotto e calcolo to vendite
vendite_per_prodotto= df.groupby("Prodotto")["Totale vendite"].sum()
print(vendite_per_prodotto)

#prodotto più venduto
prodotto_più_venduto=df.groupby("Prodotto")["Quantità"].max()
print(prodotto_più_venduto)

#città con più vendite
citta_max = df.groupby("Città")["Totale Vendite"].max()

#mostra solo dove tot vendite > 1000
vendite_over_1000 = df[df["Totale Vendite"] > 1000]
print(vendite_over_1000)

#order-by
df_vendite_ordinato = df.sort_values(by="Totale Vendite", ascending=False)
print(df_vendite_ordinato)

#select città
vendite_per_città = df["Città"].value_counts()
print(vendite_per_città)

