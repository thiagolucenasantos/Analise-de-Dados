menu = """
****MENU****
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

** Escolha a opção para iniciar a operação **

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).strip()
   
    print(f"Opção escolhida: {opcao}")

    if opcao == "1":
        valor = float(input("Informe o valor a depositar: "))
        print(valor)
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$: {valor:.2f}\n"
            print(f"Deposito realizado com sucesso. Valor do saldo atualizado R$: {saldo:.2f}")
        else:
            print("O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor a sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro de operação! Saldo insuficiente.")

        elif excedeu_limite:
            print("Erro de operação! Saque maior que o limite atual.")

        elif excedeu_saques:
            print("Erro de operação! Número de saques diários atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saldo atual após saque R$: {saldo:.2f}")

        else:
            print("O valor informado é inválido.")

    elif opcao == "3":
        print("\n###########EXTRATO###########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu Saldo atual: R$ {saldo:.2f}")
        print("--------------------------------")

    elif opcao == "4":
        print("Obrigado pela operação!! Volte Sempre!!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
