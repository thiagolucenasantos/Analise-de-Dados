saldo = 2000
saque = 500

#TUDO QUE FOR VERDADEIRO SERÁ RETORNADO ANTES DO IF, O QUE NÃO FOR SERÁ RETORNADO APÓS O ELSE
status = "Sucesso" if saldo >= saque else "Falhou"

print(f"{status} ao realizar a compra")