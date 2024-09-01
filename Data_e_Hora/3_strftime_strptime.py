#UTILLIZAÇÃO DE FUNÇÕES PARA MANIPULAR DATAS
from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y - %A"#PODEMOS FAZER NOSSA PRÓPRIA MÁSCARA PARA UTILIZARMOS SOMENTE O QUE É INTERESSANTE NO MOMENTO
marcara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual)
print(data_hora_atual.strftime("Data atual: %d/%m/%Y, %H:%M:%S"))
print(data_hora_atual.strftime(f"Utilização da mascara: {mascara_ptbr}"))

####CONVERSAO STRING EM OBJETO DATETIME###
data_convertida = datetime.strptime(data_hora_str, marcara_en)
print(f"Convertendo data e hora: {data_convertida}")
print(type(data_convertida))
