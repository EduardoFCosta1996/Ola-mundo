import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula294_ex.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo, )
    escritor.writerow(colunas)
    
    for cliente in lista_clientes:
        escritor.writerow(cliente.values())