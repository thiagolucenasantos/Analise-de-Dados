def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

#Modelo de passagem de parametros 
exibir_poema(
    "Sexta-feira, 26 de Agosto, 2024",
    "Zen of Python",
    "Beutiful is better than ugly",
    autor= "Tim", ano=1999
)