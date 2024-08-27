MAIOR_IDADE = 18    
idade_especial = 12

#PRIMEIRO EXEMPLO
idade = int(input("Informe a sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode emitir CNH")

if idade <= MAIOR_IDADE:
    print("Menor de idade, não pode emitir CNH")

#SEGUNDO EXEMPLO
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode emitir CNH")
else:
    print("Menor de idade, não pode emitir CNH")

#TERCEIRO EXEMPLO
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode emitir CNH")
elif idade == idade_especial:
    print("Pode fazer aulas teóricas.")
else: print("Menor de idade, não pode emitir CNH")


