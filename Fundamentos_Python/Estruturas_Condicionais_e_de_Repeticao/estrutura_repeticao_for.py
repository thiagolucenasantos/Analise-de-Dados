texto = input(str("Digite uma palavra: "))
VOGAIS = "AEIOU"



#NO FOR ADICIONAMOS UMA VARIAVEL COM NOME DE letra E CAPTURAMOS O QUE FOI DIGITADO PELO USUARIO NA VARIAVEL texto
#NO IF VERIFICAMOS SE O USUÁRIO DIGITOU PALAVRA MAIÚSCULA OU MINUSCULA E VERIFICAMOS QUAIS VOGAIS EXISTEM
#APÓS A VERIFICAÇÃO IMPRIMIMOS AS VOGAIS COM QUEBRA DE LINHA
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" \n")
else:
    print("Digite palavras, não números.")

#  UTILIZANDO A FUNÇÃO BUILT-IN RANGE
for numero in range(0, 21, 2):
    print(numero, end=" ")
