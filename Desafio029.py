print(f"{'*'*10}Desafio 029 - Compara se foi multado{'*'*10}")
valor_multa = float(input("Digite o valor da multa por km vigente: "))
velocidade_limite = int(input("Informe o limite de velocidade em km/h: "))
velocidade_atual = int(input("Informe a velocidade atual: "))
velocidade_acima = velocidade_atual-velocidade_limite

print(f"Você ultrapassou o limite da via em {velocidade_acima}km/h e foi multado em R${velocidade_acima*valor_multa}" if velocidade_acima > 0 else f"Velocidade: {velocidade_atual}km/h")
#Editado pelo git
