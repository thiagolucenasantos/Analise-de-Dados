#CASO OS ATRIBUTOS SEJAM PUBLICOS PENSE BEM SE FAZ SENTIDO CRIAR VARIOS PROPERTY PARA ELES
class Pessoa:
    def __init__(self, nome, ano_nascimento) -> None:
        self.nome = nome
        self._ano_nascimento = ano_nascimento
        
  
    
    @property#AQUI ESTÁ UM EXEMPLO CLÁSSICO DE COMO O PROPERTY PODE SOMAR NO NOSSO PROGRAMA
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
  
  
pessoa = Pessoa("João", 1986)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")  