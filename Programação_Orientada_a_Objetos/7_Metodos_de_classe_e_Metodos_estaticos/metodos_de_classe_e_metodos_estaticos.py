class Pessoa:
    def __init__(self,nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
    @classmethod #PERMITE O ACESSO A ATRIBUTOS E METODOS DAS CLASSES, PODENDO SER TRABALHADOS SEM A MODIFICAÇÃO DA CLASSE PRINCIPAL       
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18


pessoa = Pessoa.criar_data_nascimento(1986, 7, 12, "Maria")
print(pessoa.nome, pessoa.idade)

print(Pessoa.maior_de_idade(10))
print(Pessoa.maior_de_idade(22))