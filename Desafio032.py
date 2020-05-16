print(f"{'*'*10}Desafio 032 - Ano bissexto{'*'*10}")
ano = int(input("Informe o ano: "))
if (ano % 400 == 0):
    print(f"O ano {ano} é Bissexto")
else:
    if (ano % 100 == 0):
        print(f"O ano {ano} não é Bissexto")
    else:
        if(ano % 4 == 0):
            print(f"O ano {ano} é Bissexto")
        else:
            print(f"O ano {ano} não é Bissexto")