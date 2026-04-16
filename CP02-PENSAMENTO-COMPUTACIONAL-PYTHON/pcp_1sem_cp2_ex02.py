A = float(input("Digite um valor para o lado A: "))
B = float(input("Digite um valor para o lado B: "))
C = float(input("Digite um valor para o lado C: "))

lados = [A, B, C]
lados.sort(reverse=True)
print(lados)

def tipos_de_triangulos():
    if A >= B + C:
        return "NÃO FORMA TRIÂNGULO"

    elif A**2 == B**2 + C**2:
        return "TRIÂNGULO EQUILÁTERO"

    elif A**2 == B**2 + C**2:
        return "TRIÂNGULO RETÂNGULO"

    elif A**2 > B**2 + C**2:
        return "TRIÂNGULO OBTUSÂNGULO"

    elif A**2 < B**2 + C**2:
        return "TRIÂNGULO ACUTÂNGULO"

    elif A == B or A == C or B == C:
        return "TRIÂNGULO ISÓSCELES"

    else:
        return "TIPO NÃO IDENTIFICADO"

print(f"Tipo de triângulo: {tipos_de_triangulos()}")

