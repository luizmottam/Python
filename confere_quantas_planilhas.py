import pandas as pd

# Carregar o arquivo Excel
excel_file = pd.ExcelFile('Teste.xlsx')

# Obter a lista de nomes das planilhas
planilhas = excel_file.sheet_names

# Exibir a quantidade de planilhas
print(f"O documento possui {len(planilhas)} planilha(s).")