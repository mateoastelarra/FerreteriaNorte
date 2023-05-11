import pandas as pd

# Carga el archivo de Excel en un DataFrame de pandas
df = pd.read_excel("archivo.xlsx")


# Accede a la columna "A" por índice
column_a_by_index = df.iloc[:, 0]

# Accede a la columna "A" por nombre
column_a_by_name = df["A"]

print (column_a_by_name)