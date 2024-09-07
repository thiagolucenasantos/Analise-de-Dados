class Bicicleta:
    #O SELF EM PYTHON É O MESMO QUE O THIS EM JAVA, ELE REPRESENTA A INSTÂNCIA DO OBJETO EM QUESTÃO
    def __init__(self, cor, modelo, ano, valor): #def__init__() é o método construtor da nossa classe
        #Logo a baixo estão os atributos da classe
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

        #PODEMOS COMPARAR OS MÉTODOS DAS CLASSES COMO SE FOSSEM FUNÇÕES, O MODO DE 
        #CRIAÇÃO É IDENTICO A UMA FUNÇÃO NORMAL, A DIFERENÇA É QUE TEMOS QUE CHAMAR UM 
        #PRIMEIRO ARGUMENTO DE NOME SELF
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando...")

    def correr(self):
        print("Correndoooo")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor
                                                        in self.__dict__.items()])}"


#AGORA VAMOS INSTANCIAR O OBJETO
b1 = Bicicleta("Azul", "Caloi", 1999, 850)
print(b1.modelo)
b1.buzinar()#CHAMANDO OS MÉTODOS DA CLASSE
b1.correr()
b1.parar()
print(b1)#Padronizamos atraves do def_str_ para demonstrar os atributos da bicicleta de forma amigável
