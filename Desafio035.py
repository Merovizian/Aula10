print(f"\033[;1m{'*'*10}Desafio 035 - Três retas para triangulo{'*'*10}\033[0;0m")
reta_a = int(input("Informe o comprimento da primeira reta: "))
reta_b = int(input("Informe o comprimento da segunda reta: "))
reta_c = int(input("Informe o comprimento da terceira reta: "))

if (reta_a + reta_b > reta_c )and (reta_a + reta_c > reta_b) and (reta_c + reta_b > reta_a):
    print("\033[1;94mFormam um triângulo")
else:
    print("\033[1;91mNão formam um triângulo")