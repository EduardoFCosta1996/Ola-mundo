from datetime import datetime
from pytz import timezone

#data_str ='2024 - 10 - 21  07:49:55'
#data_str_fmt = '%Y - %m - %d %H:%M:%S'
#data = datetime(2024, 10, 21)
#data = datetime.strptime(data_str, data_str_fmt)
data = datetime.now(timezone('Asia/tokyo'))
print(data)