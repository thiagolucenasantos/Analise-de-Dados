from datetime import date, datetime, time

print("####date###")
data = date(2019, 2, 12)
print(data)
print(date.today())#RETORNA O DIA ATUAL

print(date.today())#RETORNA A DATA DE HOJE

print("###datetime###")
data_hora = datetime(2024, 3, 23, 14, 35, 5)#ALEM DA DATA NORMAL, TRÁS HORA, MINUTOS E SEGUNDOS
print(data_hora)
print(datetime.today())#RETORNA A DATA ATUAL + HORA ATUAL

print("###time###")
hora = time(23, 35, 16)
print(hora)

