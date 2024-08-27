nome = "Thiago"
idade = 30
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Carlos", "idade": 40}#dicionario
saldo = 14.58948

print("Nome: %s idade: %d" %(nome, idade))
print("Nome: {} idade: {}".format(nome, idade)) #str format
print("Nome: {0} idade: {1}".format(nome, idade)) # passando os indices das variáveis
print("Nome: {nome} idade: {idade}".format(nome = nome, idade = idade)) # passando pelo format nomeados
print("Nome: {nome}, idade: {idade}".format(**dados)) #utilizando dicionario no format
#METODO MAIS EFICAZ E MAIS LEGÍVEL ATUALMENTE EM PYTHON 
print(f"Nome: {nome}, idade: {idade}")#f-strings, o modo mais atual 
print(f"Saldo: {saldo:.2f}")# formatação de casas decimais com duas casas
print(f"Saldo: {saldo:10.3f}")# com 10 espaços a frente do número e com 3 casas decimais