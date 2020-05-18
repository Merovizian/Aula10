import math, random, time

print(f"\n{'*' * 10}\033[;1mDesafio 028 - Descobrir número Random{'*' * 10}")
escolha_pc = random.randrange(1, 5)
escolha_user = int(input("\033[1;34mInforme o numero para comparar com o Computador: "))
print("\033[1;33mProcessando...	")
time.sleep(2)
if escolha_pc == escolha_user:
    print("\033[1;92mParabéns Você acertou!!")
else:
    print(f"\033[1;31mLamento! Tente novamente. escolha do pc: {escolha_pc}")