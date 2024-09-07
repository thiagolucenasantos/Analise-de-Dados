class Passaro:
    def voar(self):
        print("Voando...")
        
class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")
        
#UM MÉTODO QUE TEM UM OBJETO QUE SIMPLESMENTE CHAMA O MÉTODO VOAR, PARA UTILIZAR POLIMORFISMO PRECISAMOS TER HERANÇA
#ISSO É POLIMORFISMO UM MÉTODO QUE SE COMPORTA DIFERENTE DEPENDENDO DE QUAL CLASSE QUE É CHAMADA QUE POSSUE SEU METODO VOAR
def plano_voo(obj): 
    obj.voar()
    
p1 = Pardal()
p2 = Avestruz()

#AQUI CHAMAMOS A INSTNCIA PLANO DE VOO E PASSAMOS NOSSOS OBJETOS NO CASO SÃO FILHAS DE PASSARO (PAI) E POSSUEM O MÉTODO VOAR

plano_voo(Pardal())
plano_voo(Avestruz())