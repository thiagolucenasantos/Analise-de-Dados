# AND = para ser TRUE tudo tem que ser true
# OR = para ser TRUE apenas um tem que ser true

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print("---------")

saldo = 1000
saque = 200
limite = 250
conta_especial = True

exp = (saque >= saldo and saque <= limite) or (conta_especial and saldo >= saque)
print(exp)

#Deixando o codigo mais legivel
consulta_saque_cliente = saque >= saldo and saque <= limite
consulta_conta_especial_e_saldo_cliente = conta_especial and saldo >= saque

resultado_final_operacao = consulta_saque_cliente or consulta_conta_especial_e_saldo_cliente
print("Operação: " + str(resultado_final_operacao))