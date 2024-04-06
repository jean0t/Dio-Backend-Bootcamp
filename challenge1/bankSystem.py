# Criação de um sistema bancário com apenas um usuário
# dessa forma não é necessário conferir agência ou identidade da conta
from hashlib import sha1

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

print(menu)
try:
    while True:
        operacao = input("-> ").strip().lower()

        match operacao:
            case 'e':
                if len(extrato) == 0:
                    print("Nenhuma operação realizada.")
                else:
                    print("ID - Operação")
                    for item in extrato:
                        print(f"{sha1(item.encode()).hexdigest()} - {item}")

            case 's':
                try:
                    valor_saque = float(input("Valor para saque: "))
                except Exception as e:
                    raise ValueError

                if qtd_saques > 0 and valor_saque <= 500 and saldo >= valor_saque:
                    qtd_saques -= 1
                    saldo -= valor_saque
                    extrato.append(f"Saque de R$ {valor_saque}")
                    print("Saque realizado com sucesso.")
                elif qtd_saques == 0:
                    print("Quantidade máxima de saques realizada.")
                elif valor_saque > 500:
                    print("Valor acima do permitido.")

            case 'd':
                try:
                    valor_deposito = float(input("Valor para depósito: "))
                except:
                    raise ValueError

                saldo += valor_deposito
                extrato.append(f"Depósito de R$ {valor_deposito}")
                print("Depósito realizado com sucesso.")

            case _:
                print("Operação não permitida.")
except KeyboardInterrupt:
    print("\nOperação cancelada com sucesso.")
