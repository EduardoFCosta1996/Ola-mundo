from datetime import datetime, timedelta

fmt = '%d/%m/%Y %H:%M:%S'

data_inicio = datetime.strptime('22/10/1996 07:22:11', fmt)
data_fim = datetime.strptime('22/10/2024 07:22:11', fmt)
delta = timedelta(days=30)
print(data_fim + delta)