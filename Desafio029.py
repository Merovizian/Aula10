print(f"\033[;1m{'*'*10}Desafio 029 - Compara se foi multado{'*'*10}")
valor_multa = float(input("\033[1;93mDigite o valor da multa por km vigente: "))
velocidade_limite = int(input("\033[1;30mInforme o limite de velocidade em km/h: "))
velocidade_atual = int(input("\033[1;32mInforme a velocidade atual: "))
velocidade_acima = velocidade_atual-velocidade_limite

print(f"\033[1;31mVocê ultrapassou o limite da via em {velocidade_acima}km/h e foi multado em R${velocidade_acima*valor_multa}" if velocidade_acima > 0 else f"\033[1;34mVelocidade: {velocidade_atual}km/h")
