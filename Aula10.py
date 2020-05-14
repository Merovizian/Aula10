menu = int(input("Informe qual exercicio da aula quer: "))

if menu == 1:
    tempo = int(input("Digite a idade do seu carro: "))
    ## Maneira Usual:
    if tempo <= 3:
        print ("Carro Novo")
    else:
        print ("Carro Velho")
    print("Fim!")

    ## Maneira rápida:
    print('Carro Novo' if tempo <=3 else 'Carro Velho')

if menu == 2:
    n1 = float(input("Digite sua primeira nota: "))
    n2 = float(input("Digite a sua segunda nota: "))
    n = (n1+n2)/2
    print(f"Sua média foi: {n:.2f}")
    if n >= 6:
        print("Aluno Aprovado!")
    else:
        print("Aluno Reprovado")