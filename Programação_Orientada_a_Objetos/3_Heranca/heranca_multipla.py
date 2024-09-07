class Animal:
    def __init__(self, numero_patas) -> None:
        self.numero_patas = numero_patas    
    
        #A BAIXO COMANDO PARA REPRESENTAÇÃO DOS NOSSOS ATRIBUTOS NO PRINT DO PROGRAMA    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f"{chave} = {valor}" for chave, valor
                                                        in self.__dict__.items()])}"
class Mamifero(Animal): #FILHO QUE EXTENDE DA CLASSE PAI ANIMAL
    def __init__(self, cor_pelo, **kw) -> None: #UTILIZANDO KWARGS PARA QUE O PYTHON POSSA LER OS ATRIBUTOS ESPECIFICOS COLOCADOS EM CADA CLASSE FILHA
        self.cor_pelo = cor_pelo
        super().__init__(**kw)#CHAMANDO O CONSTRUTOR PAI NO FILHO E PASSANDO O KWARGS PARA LER TANTO OS ATRIBUTOS DO PAI QUANTO DOS FILHOS

class Ave(Animal):
    def __init__(self, cor_bico, **kw) -> None:
        self.cor_bico = cor_bico
        super().__init__(**kw)       


class Cachorro(Mamifero):#EXTENDE DA CLASSE FILHA MAMIFERA E É NETA DA CLASSE PAI ANIMAL
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    def __init__(self, numero_patas, cor_pelo) -> None:
        print(Leao.__mro__)#COM O __mro__ PODEMOS OLHAR O CAMINHO PERCORRIDO ENTRE OS FILHOS ATÉ O PAI DOS ATRIBUTOS RELACIONADOS AS CLASSES
                            #ESSE MÉTODO É IMPORTANTE PARA PERCORRERMOS COMO A ORDEM QUE O INTERPRETADOR ESTÁ UTILIZANDO E FAZERMOS POSSÍVEIS MODIFICAÇÕES ONDE QUISERMOS
        super().__init__( numero_patas = numero_patas, cor_pelo=cor_pelo )


class Ornitorrinco(Mamifero, Ave): #EXTENDE DA CLASSE PAI E TAMBEM DA CLASSE FILHA
    pass

gato = Gato(numero_patas=4, cor_pelo="Amarelo")#POR UTILIZAR KWARGS PRECISAMOS PASSAR AS INFORMAÇÕES DE FORMA NOMEADA AGORA
print(gato)

ornitorrinco = Ornitorrinco(numero_patas=2, cor_pelo= "Azul", cor_bico="Laranja")
print(ornitorrinco)

leao = Leao(4, "Dourado")