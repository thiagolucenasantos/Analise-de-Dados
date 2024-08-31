lista = [1, "Python", [40, 30, 20]]

lista2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(lista2), id(lista))#AQUI PODEMOS COMPROVAR QUE O ENDEREÇO EM MEMÓRIA DA LISTA ORIGINAL E DA CÓPIA NÃO SÃO OS MESMOS

lista2[0] = 20

print(lista2)#PODEMOS VER QUE A LISTA2 QUE É UMA CÓPIA FOI ALTERADA E A LISTA ORIGINAL CONTINUA IGUAL
print(lista)
