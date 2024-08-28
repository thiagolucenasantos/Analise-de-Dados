def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}")


salvar_carro("Chevrolet", "Fusca", 1998, "GBD9878")
#Utilizando essa forma de inserir argumentos, independente da ordem da função ele irá mostrar na ordem que deseja
salvar_carro(marca="Chevrolet", modelo = "Fusca", ano = 1999, placa= "ggg0999")

#Podemos também passar um dicionário para a função
salvar_carro(**{"marca":"Chevrolet", "modelo": "Fusca", "ano": 1999, "placa": "ggg0999"})


