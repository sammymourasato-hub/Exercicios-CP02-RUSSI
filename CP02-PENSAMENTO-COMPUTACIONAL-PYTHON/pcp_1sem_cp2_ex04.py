# Funções obrigatórias
def calcular_horas_extras(salario_base, horas):
    # 1.5% do salário base por hora extra
    return horas * (salario_base * 0.015)


def calcular_descontos_faltas(salario_base, faltas):
    # 2% do salário base por falta
    return faltas * (salario_base * 0.02)


def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() != 's':
        return 0

    # Tabela de bônus por cargo
    bonus_por_cargo = {1: 1000, 2: 500, 3: 300, 4: 100}
    return bonus_por_cargo.get(cargo, 0)


# Entrada de dados
nome = input("Nome do funcionário: ")
cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Salário base: "))
horas_extras = float(input("Total de horas extras trabalhadas: "))
faltas = int(input("Total de faltas no mês: "))
recebeu_bonus = input("Recebeu bônus por desempenho (s ou n): ")

# Cálculos
v_horas_extras = calcular_horas_extras(salario_base, horas_extras)
v_bonus = calcular_bonus(cargo, recebeu_bonus)
v_faltas = calcular_descontos_faltas(salario_base, faltas)

salario_bruto = salario_base + v_horas_extras + v_bonus
total_acrescimos = v_horas_extras + v_bonus
total_descontos = v_faltas
salario_final = salario_bruto - total_descontos

# Exibição dos resultados
print("-" * 30)
print(f"Relatório de: {nome}")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Total de Acréscimos: R$ {total_acrescimos:.2f}")
print(f"Total de Descontos: R$ {total_descontos:.2f}")
print(f"Salário Final: R$ {salario_final:.2f}")
print("-" * 30)