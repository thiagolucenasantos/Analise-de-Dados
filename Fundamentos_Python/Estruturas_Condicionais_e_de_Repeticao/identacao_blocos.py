def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado")

def depositar(valor):
    saldo = 400
    saldo += valor
    print(saldo)
   
sacar(100)
depositar(200)
