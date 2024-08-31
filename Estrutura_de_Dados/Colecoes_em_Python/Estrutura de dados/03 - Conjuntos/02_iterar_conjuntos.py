#PODEMOS PERCORRER TAMBÉM ATRAVÉS DE UM FOR E INTERAR POR ENUMERATE
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
