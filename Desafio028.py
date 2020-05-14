import math, random

print(f"{'*' * 10}Desafio 028 - Descobrir número Random{'*' * 10}")
escolha_pc = random.randrange(1, 5)
escolha_user = int(input("Informe o numero para comparar com o Computador: "))

if escolha_pc == escolha_user:
    print("Parabéns Você acertou!!")
else:
    print(f"Lamento! Tente novamente. escolha do pc: {escolha_pc}")
