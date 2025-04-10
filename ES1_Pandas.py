import pandas as pd
import numpy as np

data = {
   'Nome': ['Anna', 'Luca', 'Marco', 'Giulia', 'Sara', 'Paolo', 'Elena', 'Francesco', 'Laura', 'Simone', 'Chiara', 'Matteo', 'Alice', 'Davide', 'Valeria', 'Giorgio', 'Martina', 'Stefano', 'Ilaria', 'Alessandro'],
   'Età': ['15', '70', '53', '9', '60', '39', '54', '3', '53', '6', '31', '34', '92', '30', '31', '59', '52' , '21', '93', '15'],
   'Città':["Roma", "Milano", "Napoli", "Torino", "Palermo", "Genova", "Bologna", "Firenze", "Bari", "Catania", "Verona", "Venezia", "Messina", "Padova", "Trieste", "Brescia", "Taranto", "Prato", "Reggio Calabria", "Modena"],
   'Salario':[3098, 2141, 3798, 3128, 2228, 3500, 3664, 2731, 4397, 1130, 2508, 1533, 2374, 3807, 1733, 3018, 1800, 1601, 1177, 2731]
}

df= pd.DataFrame(data)

# Visualizzare le prime 5 righe usando il metodo iloc[]
prime_cinque_righe = df.iloc[:5]

# Visualizzare le ultime 5 righe usando il metodo iloc[]
ultime_cinque_righe = df.iloc[-5:]

# Visualizzare il tipo di dati di ciascuna colonna
data_types = df.dtypes

# Calcolare statistiche descrittive di base per le colonne numeriche
descr_stats = df.describe()

# Identificare e rimuovere eventuali duplicati
df_no_duplicates = df.drop_duplicates()

# Gestire i valori mancanti (sostituirli con la mediana)
df_filled = df_no_duplicates.fillna(df_no_duplicates.median())

# Aggiungere una nuova colonna "Categoria Età" senza funzioni
df_filled['Categoria Età'] = pd.cut(df_filled['Età'], bins=[-np.inf, 18, 65, np.inf], labels=["Giovane", "Adulto", "Senior"])

# Salvare il DataFrame pulito in un nuovo file CSV
df_filled.to_csv('df_pulito_20.csv', index=False)

