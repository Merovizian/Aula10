print(f"\033[;1m{'*' * 10}Desafio 033 - Qual maior e o menor entre 3 numeros {'*' * 10}	\033[0;0m")
numero_a = int(input("Informe o primeiro número: "))
numero_b = int(input("Informe o segundo número: "))
numero_c = int(input("Informe o terceiro número: "))

numero_maior = numero_a
numero_menor = numero_a

if numero_b >= numero_a and numero_b >= numero_c:
    numero_maior = numero_b
if numero_c >= numero_a and numero_c >= numero_b:
    numero_maior = numero_c

if numero_b <= numero_a and numero_b <= numero_c:
    numero_menor = numero_b
if numero_c <= numero_a and numero_c <= numero_b:
    numero_menor = numero_c


print(f"O maior numero é: {numero_maior}")
print(f"O menor numero é: {numero_menor}")
