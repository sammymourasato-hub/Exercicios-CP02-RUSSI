#Sistema de Financiamento Bancário - Parcelas Fixas (Tabela Price)
#FIAP - Atividade 05

def pode_aprovar(idade, renda, valor):

#Verifica se o cliente pode ter o empréstimo aprovado.
#Regras:
# - Ter mais de 18 anos
# - O valor do financiamento deve ser no máximo 20 vezes a renda mensal

    if idade <= 18:
        return False
    if valor > renda * 20:
        return False
    return True


def def_taxa(parcelas):

#Define a taxa de juros mensal com base no número de parcelas.
#- Até 6 parcelas: 5% ao mês
#- De 7 a 12 parcelas: 8% ao mês
#- De 13 a 24 parcelas: 10% ao mês

    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10


def calcular_parcela(valor, taxa, parcelas):

    #Calcula o valor da parcela usando a fórmula da Tabela Price (PMT).
    #PMT = PV * (i*(1+i)^n) / ((1+i)^n - 1)

    pmt = valor * (taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1)
    return pmt


def calcular_total(parcela, parcelas):

    #Calcula o total pago ao longo do financiamento.
    #total = PMT * n

    return parcela * parcelas


def calcular_juros(total, valor):

    #Calcula o total de juros pagos.
    #juros = total - PV

    return total - valor


def ler_float(mensagem):

    #Lê um valor float aceitando formato brasileiro.
    #Exemplos aceitos: 5000 / 5.000 / 5000,50 / 5.000,50
    #- Se há vírgula: ela é o separador decimal, pontos são de milhar
    #- Se não há vírgula: pontos também são tratados como milhar

    while True:
        try:
            entrada = input(mensagem).strip()
            if "," in entrada:
                # Formato BR: 5.000,50 -> remove pontos de milhar, troca vírgula por ponto
                entrada = entrada.replace(".", "").replace(",", ".")
            else:
                # Sem vírgula: 5.000 -> 5000 (ponto é separador de milhar)
                entrada = entrada.replace(".", "")
            valor = float(entrada)
            return valor
        except ValueError:
            print("  Por favor, informe um valor válido (ex: 5000 ou 5.000,50).")


def solicitar_dados():
    #Solicita os dados do cliente via input.
    print("\n" + "=" * 50)
    print("   SISTEMA DE FINANCIAMENTO BANCÁRIO")
    print("=" * 50)

    nome = input("\nNome do cliente: ").strip()

    while True:
        try:
            idade = int(input("Idade: "))
            if idade <= 0:
                print("  Idade inválida. Informe um valor positivo.")
            else:
                break
        except ValueError:
            print("  Por favor, informe um número inteiro para a idade.")

    while True:
        renda = ler_float("Renda mensal (R$): ")
        if renda <= 0:
            print("  Renda inválida. Informe um valor positivo.")
        else:
            break

    while True:
        valor = ler_float("Valor desejado do empréstimo (R$): ")
        if valor <= 0:
            print("  Valor inválido. Informe um valor positivo.")
        else:
            break

    while True:
        try:
            parcelas = int(input("Número de parcelas (3 a 24): "))
            if parcelas < 3 or parcelas > 24:
                print("  Número de parcelas inválido. Deve ser entre 3 e 24.")
            else:
                break
        except ValueError:
            print("  Por favor, informe um número inteiro para as parcelas.")

    return nome, idade, renda, valor, parcelas


def exibir_resultado(nome, valor, parcelas, taxa, parcela, total, juros, aprovado):
    #Exibe o resultado do financiamento de forma formatada.
    print("\n" + "=" * 50)
    print("   RESULTADO DO FINANCIAMENTO")
    print("=" * 50)

    if not aprovado:
        print(f"\nCliente: {nome}")
        print("\n EMPRÉSTIMO NEGADO")
        print("\nMotivos possíveis:")
        print("  - Idade igual ou inferior a 18 anos")
        print("  - Valor solicitado ultrapassa 20x a renda mensal")
    else:
        print(f"\nCliente:              {nome}")
        print(f"Valor financiado:     R$ {valor:,.2f}")
        print(f"Taxa de juros:        {taxa * 100:.0f}% ao mês")
        print(f"Valor da parcela:     R$ {parcela:,.2f}")
        print(f"Número de parcelas:   {parcelas}x")
        print(f"Valor total pago:     R$ {total:,.2f}")
        print(f"Total de juros pagos: R$ {juros:,.2f}")
        print("\n EMPRÉSTIMO APROVADO")

    print("=" * 50)


def main():
    nome, idade, renda, valor, parcelas = solicitar_dados()

    aprovado = pode_aprovar(idade, renda, valor)

    if aprovado:
        taxa = def_taxa(parcelas)
        parcela = calcular_parcela(valor, taxa, parcelas)
        total = calcular_total(parcela, parcelas)
        juros = calcular_juros(total, valor)
    else:
        taxa = parcela = total = juros = 0

    exibir_resultado(nome, valor, parcelas, taxa, parcela, total, juros, aprovado)


if __name__ == "__main__":
    main()