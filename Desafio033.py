print(f"{'*' * 10}Desafio 033 - Qual maior e o menor entre 3 numeros {'*' * 10}")
numero_a = int(input("Informe o primeiro número: "))
numero_b = int(input("Informe o segundo número: "))
numero_c = int(input("Informe o terceiro número: "))

if numero_a > numero_b and numero_b > numero_c:
    print(f"Maior número: {numero_a}\nMenor número: {numero_c}")
if numero_a > numero_c and numero_c > numero_b:
    print(f"Maior número: {numero_a}\nMenor número: {numero_b}")

if numero_b > numero_a and numero_a > numero_c:
    print(f"Maior número: {numero_b}\nMenor número: {numero_c}")
if numero_b > numero_c and numero_c > numero_a:
    print(f"Maior número: {numero_b}\nMenor número: {numero_a}")

if numero_c > numero_a and numero_a > numero_b:
    print(f"Maior número: {numero_c}\nMenor número: {numero_b}")
if numero_c > numero_b and numero_b > numero_a:
    print(f"Maior número: {numero_c}\nMenor número: {numero_a}")

if numero_a == numero_b and numero_a > numero_c:
    print(f"Números {numero_a,numero_b} são maiores e {numero_c} menor")
if numero_a == numero_c and numero_a > numero_b:
    print(f"Números {numero_a,numero_c} são maiores e {numero_b} menor")
if numero_b == numero_c and numero_b > numero_a:
    print(f"Números {numero_b,numero_c} são maiores e {numero_a} menor")

if numero_a == numero_b and numero_a < numero_c:
    print(f"Número {numero_c} é maior e {numero_a,numero_b} menores")
if numero_a == numero_c and numero_a < numero_b:
    print(f"Número {numero_b} é maior e {numero_c,numero_a} menores")
if numero_b == numero_c and numero_b < numero_a:
    print(f"Números{numero_a} é maior e {numero_c,numero_b} menores")



