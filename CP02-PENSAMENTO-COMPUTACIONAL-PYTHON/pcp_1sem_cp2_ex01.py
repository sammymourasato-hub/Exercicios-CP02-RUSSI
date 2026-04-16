# ENTRADA DOS DADOS DA CARGA -->
cod_origem = int(input("Digite o código do estado de origem da carga do caminhão (1 a 5): "))
peso_ton = float(input("Digite o peso da carga do caminhão (toneladas): "))
cod_carga = int(input("Digite o código da carga (10 a 40): "))
print()

# CONVERSÃO DE TONELADAS PARA QUILOS -->
peso_kg = (peso_ton * 1000)
print(f"Peso convertido em kilos: {peso_kg:.2f}Kg")

# PREÇO DA CARGA POR KG -->
def valor_carga_por_kg():
    if 10 <= cod_carga <= 20:
        return peso_kg * 100

    elif 21 <= cod_carga <= 30:
        return peso_kg * 250

    elif 31 <= cod_carga <= 40:
        return peso_kg * 340

    else:
        return print("ERRO!! Dígite números do código de 10 a 40")

print(f"O preço da carga: R${valor_carga_por_kg(): .2f}")

# VALOR DOS IMPOSTOS
def valor_imposto():
    if cod_origem == 1:
        return valor_carga_por_kg() * 0.35

    elif cod_origem == 2:
        return valor_carga_por_kg() * 0.25

    elif cod_origem == 3:
        return valor_carga_por_kg() * 0.15

    elif cod_origem == 4:
        return valor_carga_por_kg() * 0.05

    elif cod_origem == 5:
        return 0

    else:
        return print("Erro!! OS números do código de origem de 1 a 5")

print(f"Valor do imposto: R${valor_imposto(): .2f}")

# VALOR TOTAL TRANSPORTADO PELO CAMINHÃO
def valor_total():
    return valor_carga_por_kg() + valor_imposto()

print(f"O valor total: R${valor_total(): .2f}")





