contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

#PODEMOS MANIPULAR OS DADOS NA COPIA COMO QUISERMOS SEM ALTERAR O DICIONÁRIO ORIGINAL
print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
