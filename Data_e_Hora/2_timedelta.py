from datetime import datetime, timedelta, date

tipo_carro = "G"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "p":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "m":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")

print(date.today() - timedelta(days= 1)) #decrementa um dia da data atual