#SET, ELIMINA ELEMENTOS DUPLICADOS DENTRO DE UMA LISTA
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

#ALÉM DE TIRAR DUPLICADOS ELE TAMBÉM RETORNA OS ELEMENTOS EM ORDEM ALETTÓRIA, ENTÃO CUIDADO AO UTILIZAR
letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}
