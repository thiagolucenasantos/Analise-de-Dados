class Conta:
    #_saldo É UMA VARIÁVEL PRIVADA, ENTÃO A MANIPULAÇÃO DEVE SER FEITA SOMENTE NO
    #ESCOPO DA CLASSE, POR CONVÊNÇÃO NÃO DEVE SER MANIPULADA FORA DELA DE FORMA ALGUMA
    def __init__(self, numero_agencia, saldo=0, ) -> None:
        self._saldo = saldo#atributo privado
        self.numero_agencia = numero_agencia#atributo publico
        
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor
        
    #PARA PODERMOS TER ACESSO AO SALDO, DEVEMOS CRIAR UM MÉTODO QUE PERMITE ISTO
    #AQUI É UM EXEMPLO SIMPLES, MAS É AQUI ONDE PODEMOS CRIAR A PERMISSÃO PARA
    #QUE O USUÁRIO POSSA ACESSAR O SEU SALDO, POR EXEMPLO DIGITAR SUA SENHA DE ACESSO
    def mostar_saldo(self):
        return self._saldo
    
conta = Conta("001", 100)
conta.depositar(100)
print(conta.numero_agencia)
print(conta.mostar_saldo())
    