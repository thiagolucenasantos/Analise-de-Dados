#FAZENDO A MESMA MANIPULAÇÃO DE HORAS PORÉM SEM A BIBLIOTECA pytz
from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sp)