#PARAMETROS POR POSIÇÃO E PARAMETROS NOMEADOS
def criar_carros(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

def criar_carros_2(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carros("Palio", 1999, "GHD8776", marca="Fiat", motor=1.0, combustivel="Gasolina")
criar_carros_2("Palio", 1999, "GHD8776", "CHEVROLET", motor=1.0, combustivel="Gasolina")