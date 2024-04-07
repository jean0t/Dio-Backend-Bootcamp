# Criação de um sistema bancário com apenas um usuário
# dessa forma não é necessário conferir agência ou identidade da conta
from datetime import date

# definindo os parametros iniciais
saldo = 0
limite_saque = 500
qtd_saques = 3
extrato = []

# menu
menu = """

Operações disponíveis:

(e) - Extrato
(s) - Saque
(d) - Depósito
(q) - quit

"""

def tirar_extrato():

    if len(extrato) == 0:
        return "Nenhuma operação realizada."

    else:
        print("month - Operação")
        for item in extrato:
            time = date.today()
            print(f"{time.month}/{time.year} - {item}")


def realizar_saque():

    global qtd_saques
    global extrato
    global saldo

    valor_saque = float(input("Valor para saque: "))

    if qtd_saques > 0 and saldo >= valor_saque and valor_saque > 0 and 500 >= valor_saque:
        qtd_saques -= 1
        saldo -= valor_saque

        extrato.append(f"Saque de R$ {valor_saque}")
        return "Saque realizado com sucesso."

    elif qtd_saques == 0:
        return "Quantidade máxima de saques realizada."

    elif valor_saque > 500:
        return "Valor acima do permitido."

    else:
        return "Saque não realizado"


def realizar_deposito():

    global extrato
    global saldo

    try:
        valor_deposito = float(input("Valor para depósito: "))
        if valor_deposito <= 0:
            return "Valor inválido."

        else:
            saldo += valor_deposito
            extrato.append(f"Depósito de R$ {valor_deposito}")
            return "Depósito realizado com sucesso."

    except:
        raise ValueError

def main():

    print(menu)
    try:
        while True:
            operacao = input("-> ").strip().lower()

            match operacao:
                case 'e':
                    tirar_extrato()

                case 's':
                    informacao = realizar_saque()
                    print(informacao)

                case 'd':
                    informacao = realizar_deposito()
                    print(informacao)

                case _:
                    print("Operação não permitida.")

    except KeyboardInterrupt:
        print("\nOperação cancelada com sucesso.")

main()
