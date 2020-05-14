tempo = int(input("Digite a idade do seu carro: "))

## Maneira Usual:
if tempo <= 3:
    print ("Carro Novo")
else:
    print ("Carro Velho")

print("Fim!")

## Maneira rápida:
print('Carro Novo' if tempo <=3 else 'Carro Velho')

