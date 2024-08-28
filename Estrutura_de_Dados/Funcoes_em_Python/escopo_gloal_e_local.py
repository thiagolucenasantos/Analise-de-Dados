#VARIAVEL GLOBAL, MUITO CUIDADO AO DECLARAR UMA VARIÁVEL LOCAL
salario = 2000

def bonificacao(bonus):
    global salario
    salario += bonus
    return salario


novo_salario = bonificacao(500)
print(novo_salario)

