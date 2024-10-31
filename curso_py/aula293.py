import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula292_ex.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        print(linha['Nome'], linha['Idade'])
