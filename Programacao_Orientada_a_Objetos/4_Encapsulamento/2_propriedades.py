class Foo:
    def __init__(self, x = None):
        self._x = x
      
     #PARA RETORNAR VALOR PRECISAMOS OBRIGATORIAMENTE DO PROPERTY 
    @property #PERMITE QUE MANIPULEMOS UM METODO COMO SE FOSSE UM ATRIBUTO   
    def x(self):
        return self._x or 0
    
    @x.setter #SETTER SERIA A OPORTUNIDADE DE MODIFICAR OS ATRIBUTOS, SÓ É POSSÍVEL COM O SETTER
    def x(self, valor):
         self._x += valor
       
    #PARA NÃO EXCLUIR O ATRIBUTO POR COMPLETO, POR QUE ISTO PODE CAUSAR PROBLEMA NO CODIGO
    #PODEMOS SIMPLESMENTE LIMPA-LO, ATRIBUINDO 0 OU -1, ALGO QUE INFORME QUE FOI ZERADO POR EXEMPLO     
    @x.deleter
    def x(self):
        self._x = -1 
    

foo = Foo(10)
print(foo.x)
foo.x = 10 #COM O SETTER PODEMOS MANIPULAR AGORA O VALOR DO ATRIBUTO X
print(foo.x)

del foo.x #UTILIZANDO A PROPRIEDADE DELETER
print(foo.x)