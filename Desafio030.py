print(f"\033[;1m{'*'*10}Desafio 030 - Par ou impar{'*'*10}\033[0;0m")
numero = int(input("Digite um numero: "))
print(f'\033[1;34mPAR' if (numero%2==0) else '\033[1;31mINPAR')
