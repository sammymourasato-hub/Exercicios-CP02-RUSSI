A = float(input("Digite um valor para o lado A: "))
B = float(input("Digite um valor para o lado B: "))
C = float(input("Digite um valor para o lado C: "))

lados = [A, B, C]
lados.sort(reverse=True)
print(lados)

def tipos_de_triangulos():
    if A >= B + C:
        print("NAO FORMA TRIANGULO")

    else:
        if A ** 2 == B ** 2 + C ** 2:
            print("TRIANGULO RETANGULO")
        elif A ** 2 > B ** 2 + C ** 2:
            print("TRIANGULO OBTUSANGULO")
        else:
            print("TRIANGULO ACUTANGULO")

        if A == B == C:
            print("TRIANGULO EQUILATERO")
        elif A == B or A == C or B == C:
            print("TRIANGULO ISOSCELES")

print(f"Tipo de triângulo: {tipos_de_triangulos()}")