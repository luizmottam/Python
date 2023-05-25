import pandas as pd
import os

df = pd.read_csv('Produtos.csv',  delimiter=';') # Nome do arquivo

num_colunas = df.shape[1] # Quantidades de colunas
primeira_coluna = df.iloc[:, 0] # Pegar coluna sem o nome
primeiras_duas_colunas = df.iloc[:, [0, 1]] # Pegar mais de uma coluna e separar elas

print(num_colunas)