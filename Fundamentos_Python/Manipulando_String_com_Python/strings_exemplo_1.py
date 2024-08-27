nome = "thiago"

print(nome.upper()) #retorna o nome todo em maiúsculo
print(nome.lower()) #retorna o nome todo em minúsculo
print(nome.title()) #retorna a primeira letra do nome em maiúscula

texto = "   Olá mundo    "

print(texto + ".")
print(texto.strip() + "."); #retira os espaços em branco em ambos os lados
print(texto.rstrip() + "."); #retira os espaços em branco do lado direito
print(texto.lstrip() + "."); #retira os espaços em branco do lado esquerdo

menu = "Cardapio"
print(menu.center(12, "*"))#Centralizamos a string e adicionamos o simbolo qualquer de acordo com a quantidade de caracteres setada
print(".".join(menu)) #Aplica o simbolo que passarmos entre a string da nossa variável