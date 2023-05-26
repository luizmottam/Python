import pandas as pd

df = pd.read_excel('Teste.xlsx') # Nome do arquivo

#primeira_coluna = df.iloc[:, 0] # Pegar coluna sem o nome
#primeiras_duas_colunas = df.iloc[:, [0, 1]] # Pegar mais de uma coluna e separar elas

def le_coluna_por_coluna(df):

  num_colunas = df.shape[1] # Quantidades de colunas
  
  for i in range(num_colunas):
    coluna_em_analise = df.iloc[:, i]
    tem_duplicatas = coluna_em_analise.duplicated().any()
  
    if tem_duplicatas:
      print(f"Na coluna {df.columns[i]} existem duplicatas")
    else:
      print(f"Na coluna {df.columns[i]} não tem duplicatas")


def le_linha(df):
  # Verificar as linhas duplicadas
  linhas_duplicadas = df.duplicated()
  
  # Exibir as linhas duplicadas
  linhas_duplicadas = df[linhas_duplicadas]
  print(linhas_duplicadas)


le_linha(df)