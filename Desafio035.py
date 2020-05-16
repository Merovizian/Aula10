print(f"{'*'*10}Desafio 035 - Três retas para triangulo{'*'*10}")
reta_a = int(input("Informe o comprimento da primeira reta: "))
reta_b = int(input("Informe o comprimento da segunda reta: "))
reta_c = int(input("Informe o comprimento da terceira reta: "))

if reta_a - reta_b > 0:
    modulo_ab = reta_a - reta_b
else:
    modulo_ab = (reta_a - reta_b)* -1

if reta_a - reta_c > 0:
    modulo_ac = reta_a - reta_c
else:
    modulo_ac = (reta_a - reta_c) *-1

if reta_b - reta_c > 0:
    modulo_bc = reta_b - reta_c
else:
    modulo_bc = (reta_b - reta_c)*-1



if reta_a + reta_b > reta_c and reta_c > modulo_ab:
    print("É um triângulo")
else:
    if reta_a + reta_c > reta_b and reta_b > modulo_ac:
        print("É um triângulo")
    else:
        if reta_c + reta_b > reta_a and reta_a > modulo_bc:
            print("É um triângulo")
        else:
            print("Não é um triângulo")
