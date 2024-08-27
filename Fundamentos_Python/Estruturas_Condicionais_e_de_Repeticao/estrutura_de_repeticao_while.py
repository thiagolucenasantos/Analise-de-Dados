#UTILIZAMOS O HILE QUANDO NÃO SABEMOS QUANTAS VEZES DETERMINADA AÇÃO PODE SER EXECUTADA
#PORÉM ESSA AÇÃO SERÁ ACABADA APÓS DETERMINADA CONDIÇÃO DO WHILE

opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato.")