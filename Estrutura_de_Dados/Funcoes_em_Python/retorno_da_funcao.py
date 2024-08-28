def calcula_total(numeros):
    return sum(numeros)

def retorno_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1

    return antecessor, sucessor

def retorna_none():
    print("Olá")
    return None #POR PADRÃO A FUNÇÃO RETORNA NONE

print(calcula_total([10, 10]))
print(retorno_antecessor_e_sucessor(10))
print(retorna_none())

    