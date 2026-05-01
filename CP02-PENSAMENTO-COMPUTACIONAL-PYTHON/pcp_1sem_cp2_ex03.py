import math

# Entradas das notas dos Checkpoints -->
nota_cp1 = float(input("Nota do Checkpoint 1: "))
nota_cp2 = float(input("Nota do Checkpoint 2: "))
nota_cp3 = float(input("Nota do Checkpoint 3: "))

# Entradas das notas das Sprints -->
nota_sp1 = float(input("Nota da Sprint 1: "))
nota_sp2 = float(input("Nota da Sprint 2: "))

# Entradas da nota da Global Solution -->
nota_gs = float(input("Nota da Global Solution: "))

# Definindo menor nota -->
menor = nota_cp1

if nota_cp2 < menor:
    menor = nota_cp2

if nota_cp3 < menor:
    menor = nota_cp3

# CALCULANDO MÉDIAS (COM OU SEM PESO) -->
def calculo_media_sem_peso():
    return (nota_cp1 + nota_cp2 + nota_cp3 - menor + nota_sp1 + nota_sp2) / 4 * 0.4 + nota_gs * 0.6

def calculo_media_com_peso():
    return calculo_media_sem_peso() * 0.4

# Exibição dos Resultados
print(f"Média sem peso: {calculo_media_sem_peso(): .1f}")
print(f"Média com peso: {calculo_media_com_peso(): .1f}")