import os
import glob
import pandas as pd
import time

#Váriaveis
nomePasta = str(input('Digite o nome da pasta: '))
arquivos = []
df = 0
i = 0

# Limpa
def cls():
  time.sleep(2)
  os.system('clear') or None
  
# Caminho da pasta
pasta = nomePasta + '/'

cls()
# Percorrer todos os arquivos da pasta
for arquivo in glob.glob(os.path.join(pasta, '*')):
  
  # Exibir o nome do arquivo
  arquivos.append(arquivo)
  print(f"[{i}]{arquivo}")
  i+=1


index = int(input("Digite o index do arquivo que você quer: "))

cls()

def leitura(index):
    # Obter a extensão do arquivo
    extensao = os.path.splitext(arquivos[index])[1]
    # Exibir a extensão
    print(f"A extensão do arquivo é: {extensao}")
    cls()
    # Leitura do pandas, que depende da extensão
    if extensao == ".xlsx":
        df = pd.read_excel(arquivos[index])
    elif extensao == ".csv":
        df = pd.read_csv(arquivos[index], delimiter=';')
    else:
        df = None
        print("Extensão não suportada.")

    return df

df = leitura(index)
print(df)