class Cachorro:
    #def __init__ É ASSIM QUE CRIAMOS NOSSO CONSTRUTOR E ELE É SEMPRE INICIALIZADO
    #NO MOMENTO QUE INSTANCIAMOS NOSSO OBJETO
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        if (self.acordado == False):
            print("Ela está dormindo, não pode latir")
        else:
            print("AU AU...")

    def correr(self):
        print("Começou a correr!!")

    # def__del__ ELE É O OPOSTO DO INIT, SEMPRE É EXECUTADO NO FINAL QUANDO O OBJETO É DESTRUIDO
    def __del__(self):
        print("Destruindo a instância da classe com o método __del__")
        

c = Cachorro("Buba", "dourada", True)
c.latir()

del c #UTILIZANDO DESTA FORMA FORÇAMOS O del a destruir o objeto antes do print Olá

print("Olá")