import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Funcionario:
    def __init__(self, nome, cargo, salario, horas_trabalhadas):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_desconto_ir(self):
        if self.salario <= 1500:
            return 0
        elif 1500 < self.salario <= 3000:
            return 0.15 * self.salario
        elif 3000 < self.salario <= 5000:
            return 0.20 * self.salario
        else:
            return 0.27 * self.salario

def main():
    funcionarios = []
    
    # Leitura dos dados dos funcionários e gravação em arquivo
    num_funcionarios = int(input("Informe o número de funcionários: "))
    with open("folha_pag.txt", "w") as file:
        for _ in range(num_funcionarios):
            nome = input("Nome do funcionário: ")
            cargo = input("Cargo do funcionário: ")
            salario = float(input("Salário do funcionário: "))
            horas_trabalhadas = float(input("Horas trabalhadas do funcionário: "))
            funcionario = Funcionario(nome, cargo, salario, horas_trabalhadas)
            funcionarios.append(funcionario)
            file.write(f"{nome},{cargo},{salario},{horas_trabalhadas}\n")
    
    # Leitura dos dados do arquivo e cálculo de descontos
    descontos_ir = []
    total_descontos = 0
    total_salario_bruto = 0
    total_salario_liquido = 0
    with open("folha_pag.txt", "r") as file:
        for line in file:
            nome, cargo, salario, horas_trabalhadas = line.strip().split(',')
            salario = float(salario)
            horas_trabalhadas = float(horas_trabalhadas)
            funcionario = Funcionario(nome, cargo, salario, horas_trabalhadas)
            desconto_ir = funcionario.calcular_desconto_ir()
            salario_liquido = salario - desconto_ir
            descontos_ir.append(desconto_ir)
            total_descontos += desconto_ir
            total_salario_bruto += salario
            total_salario_liquido += salario_liquido
    
    # Impressão dos dados formatados em coluna
    print("\nRelatório de Folha de Pagamento:")
    print(f"{'Nome':<20}{'Cargo':<20}{'Salário Bruto':<15}{'Desconto IR':<15}{'Salário Líquido':<15}")
    with open("relatorio.txt", "w") as relatorio_file:
        relatorio_file.write("Relatório de Folha de Pagamento:\n")
        relatorio_file.write(f"{'Nome':<20}{'Cargo':<20}{'Salário Bruto':<15}{'Desconto IR':<15}{'Salário Líquido':<15}\n")
        for i, funcionario in enumerate(funcionarios):
            nome = funcionario.nome
            cargo = funcionario.cargo
            salario_bruto = funcionario.salario
            desconto_ir = descontos_ir[i]
            salario_liquido = salario_bruto - desconto_ir
            print(f"{nome:<20}{cargo:<20}{salario_bruto:<15.2f}{desconto_ir:<15.2f}{salario_liquido:<15.2f}")
            relatorio_file.write(f"{nome:<20}{cargo:<20}{salario_bruto:<15.2f}{desconto_ir:<15.2f}{salario_liquido:<15.2f}\n")
    
    print("\nTotais:")
    print(f"Total Descontos IR: {total_descontos:.2f}")
    print(f"Total Salário Bruto: {total_salario_bruto:.2f}")
    print(f"Total Salário Líquido: {total_salario_liquido:.2f}")
    relatorio_file.write("\nTotais:\n")
    relatorio_file.write(f"Total Descontos IR: {total_descontos:.2f}\n")
    relatorio_file.write(f"Total Salário Bruto: {total_salario_bruto:.2f}\n")
    relatorio_file.write(f"Total Salário Líquido: {total_salario_liquido:.2f}\n")

if __name__ == "__main__":
    main()