def exibir_mensagem():
    print("Bom dia!!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anonimo"):
    print(f'Seja bem vindo {nome}')

exibir_mensagem()
exibir_mensagem_2("João")
exibir_mensagem_3()
exibir_mensagem_3("Pati")