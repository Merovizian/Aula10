print(f"\033[;1m{'*'*10}Desafio 032 - Ano bissexto{'*'*10}\033[0;0m")
ano = int(input("Informe o ano: "))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f"\033[1;34mO ano {ano} é BISSEXTO")
else:
    print(f"\033[1;31mO ano {ano} não é BISSEXTO")

