# ENTRADA DOS DADOS DA CARGA -->
cod_origem = int(input("Digite o código do estado de origem da carga do caminhão (1 a 5): "))
peso_ton = float(input("Digite o peso da carga do caminhão (toneladas): "))
cod_carga = int(input("Digite o código da carga (10 a 40): "))
print()

# CONVERSÃO DE TONELADAS PARA QUILOS -->
peso_kg = (peso_ton * 1000)
print(f"Peso convertido em kilos: {peso_kg:.2f} Kg")

# PREÇO DA CARGA POR KG -->
def valor_carga_por_kg():
    if 10 <= cod_carga <= 20:
        preco_carga1 = (peso_kg * 100.00)
        print(f"O preço da carga é de: R${preco_carga1:.2f}")

    elif 21 <= cod_carga <= 30:
        preco_carga2 = (peso_kg * 250)
        print(f"O preço da carga é de: R${preco_carga2:.2f}")

    elif 31 <= cod_carga <= 40:
        preco_carga3 = (peso_kg * 340)
        print(f"O preço da carga é de: R${preco_carga3:.2f}")

    else:
        ("ERRO!! Dígite números do código de 10 a 40")

# VALOR TOTAL TRANSPORTADO PELO CAMINHÃO





