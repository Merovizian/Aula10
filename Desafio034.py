print(f"{'*'*10}Desafio 034 - Calculo de salario com condição {'*'*10}")
salario = float(input("Informe o salário: "))
print(f"Novo salário: R$ {salario*1.1:.2f}" if (salario > 1250) else f"Novo salário: R$ {salario*1.15:.2f}")