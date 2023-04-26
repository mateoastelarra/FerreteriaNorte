import pandas as pd
from helpers import filter_products_csv

data_empresa = pd.read_excel("FerreteriaNorte\CAVAL.xlsx")
data_ferreteria = pd.read_excel("FerreteriaNorte\CAVALF.xlsx")

data_empresa.to_csv("FerreteriaNorte\datos_empresa.csv")
data_ferreteria.to_csv("FerreteriaNorte\datos_ferretería.csv")

data_empresa_csv = pd.read_csv("FerreteriaNorte\datos_empresa.csv")
data_ferreteria_csv = pd.read_csv("FerreteriaNorte\datos_ferretería.csv")

#print(data_empresa_csv.iloc[0, 2])
#print(data_ferreteria_csv)
#print(data_ferreteria_csv.iloc[:, 3])
#print(filter_products_csv(data_ferreteria_csv, data_empresa_csv, 3, 2))

merge = pd.merge(data_ferreteria, data_empresa, on="codigo")

merge.to_excel("FerreteriaNorte\prueba.xlsx")

