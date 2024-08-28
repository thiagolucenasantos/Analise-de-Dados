# Em python como tudo se comporta como objeto, podemos utilizar as funções como objetos também
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operacao é = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 5, subtrair)

soma_numeros = somar
print(f"A soma total é: {soma_numeros(19,5)}")
