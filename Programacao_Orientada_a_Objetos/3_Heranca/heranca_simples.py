class Veiculo: #CLASSE PAI
    def __init__(self, cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas
        
    def ligar_motor(self):
        print("Motor Ligado!!")
        
    #A BAIXO COMANDO PARA REPRESENTAÇÃO DOS NOSSOS ATRIBUTOS NO PRINT DO PROGRAMA    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor
                                                        in self.__dict__.items()])}"

class Motocicleta(Veiculo): #CLASSE MOTOCICLETA É FILHA DE VEÍCULO
    pass

class Carro(Veiculo): #CLASSE CARRO É FILHA DE VEÍCULO
    pass

    
class Caminhao(Veiculo): #CLASSE CAMINHAO É FILHA DE VEÍCULO
    def __init__(self, cor, placa, numero_de_rodas, carregado): #MÉTODO PARTICULAR DA CLASSE CAMINHÃO, AQUI SOBRESCREVEMOS O MÉTODO DO PAI
        super().__init__(cor, placa, numero_de_rodas)#COM A SUPER CONSEGUIMOS CHAMAR A IMPLEMENTAÇÃO DA MINHA CLASSE PAI
        self.carregado = carregado
        
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não' } estou carregado")

#UTILIZANDO A CLASSE FILHA MOTOCICLETA QUE HERDA AS OBRIGAÇÕES DA PAI VEICULO
moto = Motocicleta("Azul", "GCD 1209", 2)
moto.ligar_motor()

carro = Carro("Branco", "ASC 6628", 4)
carro.ligar_motor()

caminhao = Caminhao("Preto", "KJH675", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()


#EXIBINDO TODOS OS VEICULOS
print(moto)
print(carro)
print(caminhao)