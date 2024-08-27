while True:
    opcao = int(input("Digite um numero: "))

    if(opcao == 10):
        break

print(opcao)


for numero in range(100):
    
    if numero % 2 == 0:
        continue
    print(numero, end=" ")
