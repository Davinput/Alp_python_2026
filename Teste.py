#questão 4
salario = float(input("Digite o salário do funcionário: "))
cargo = input("Digite o cargo do funcionário: ")

if cargo == "Programador de Sistemas":
    novo_salario = salario * 1.30
    print(f"Novo salário: R$ {novo_salario:.2f}")

elif cargo == "Analista de Sistemas":
    novo_salario = salario * 1.20
    print(f"Novo salário: R$ {novo_salario:.2f}")

if cargo == "Analista de Banco de Dados":
    novo_salario = salario * 1.15
    print(f"Novo salário: R$ {novo_salario:.2f}")

else:
    print("Cargo inválido")
