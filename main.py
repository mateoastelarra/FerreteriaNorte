import pandas as pd
import csv
from helpers import filter_products_csv

data_empresa = pd.read_excel("CAVAL.xlsx")
data_ferreteria = pd.read_excel("CavalFer.xlsx")

data_empresa.to_csv("datos_empresa.csv")
data_ferreteria.to_csv("datos_ferretería.csv")

data_empresa_csv = pd.read_csv("datos_empresa.csv")
data_ferreteria_csv = pd.read_csv("datos_ferretería.csv")

#print(data_empresa_csv.iloc[0, 2])
#print(data_ferreteria_csv)
#print(data_ferreteria_csv.iloc[:, 3])
print(filter_products_csv(data_ferreteria_csv, data_empresa_csv, 3, 2))

