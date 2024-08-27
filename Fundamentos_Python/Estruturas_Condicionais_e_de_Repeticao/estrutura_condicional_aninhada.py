#EXEMPLO DE IFS ANINHADOS

conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 2400
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
       print("Saque realizado com sucesso!!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com sucesso com o uso do cheque especial.")
    else:
        print("Saldo insuficiente para o valor a sacar.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insufuciente!")
else:
    print("Por favor selecione um tipo de conta.")

