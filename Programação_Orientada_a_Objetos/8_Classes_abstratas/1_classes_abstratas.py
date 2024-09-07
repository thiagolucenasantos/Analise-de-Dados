from abc import ABC, abstractmethod #PARA UTILIZARMOS UMA CLASSE ABSTRATA PRECISAMOS IMPORTAR O MÉTODO ABC

#CRIANDO METODOS ABSTRATOS NA NOSSA CLASSE PAI PODEMOS PADRONIZAR O CÓDIGO PARA QUE SEMPRE SEJA IMPLEMENTADO O NECESSÁRIO NAS DEMAIS CLASSES CRIADAS
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
class ControleTV(ControleRemoto): #AGORA COMO OS METODOS DA CLASSE PAI SAO ABSTRATOS, SOMOS OBRIGADOS A IMPLEMENTAR NAS CLASSES FILHAS
    def ligar(self):
        print("Ligando a TV")
        
    def desligar(self):
        print("Desligando a TV")
        
        
controle = ControleTV()
controle.ligar() #APÓS A IMPLEMENTAÇÃO OBRIATÓRIA, CONSEGUIMOS CHAMAR AS FUNÇÕES DE LIGAR E DESLIGAR
controle.desligar()