class Estudante:
    escola = "Escola do Bairro"  #ESTA É UMA VARIÁVEL DE CLASSE, ÚNICA PARA TODOS OS OBJETOS
    
    def __init__(self, nome, matricula) -> None:
        self.nome = nome   # ESTAS SÃO VARIÁVEIS DE INSTANCIA, CADA OBJETO POSSUE UMA COPIA DELA
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
        for obj in objs:
            print(obj)
    
aluno_1 = Estudante("José", 1)
aluno_2 = Estudante("Maria", 2)
mostrar_valores(aluno_1, aluno_2)


Estudante.escola = "Nova Escola" #MUDANDO A VARIÁVEL DE CLASSE A PARTIR DE AGORA TODOS OS ALUNOS A BAIXO MUDARÃO DE ESCOLA
aluno_1.matricula = 5 # AQUI MOTIFICAMOS A VARIÁVEL DE INSTANCIA SOMENTE NO ALUNO 1, OS DEMAIS PERMANECEM IGUAIS
mostrar_valores(aluno_1, aluno_2)