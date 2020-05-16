print(f"{'*'*10}Desafio 031 - Preço viagem variavel{'*'*10}")
distancia =float(input("Informe a distancia a ser percorrida(em KM): "))
print(f"O preço final é: R${distancia*0.50}" if distancia<=200 else f"O preço final é: R${0.45*distancia}")
