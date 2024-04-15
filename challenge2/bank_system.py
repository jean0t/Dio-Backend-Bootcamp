from textwrap import dedent
from classes_bank_system import *

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(dedent(menu))

def depositar(clientes):
    pass

def exibir_extrato(clientes):
    pass

def criar_cliente(clientes):
    pass

def criar_conta(numero_conta, clientes, contas):
    pass

def listar_contas(contas):
    pass

def main():
    clientes = []
    contas = []

    try:
        while True:
            opcao = menu()

            match opcao:
                case "d":
                    depositar(clientes)

                case "e":
                    exibir_extrato(clientes)

                case "nu":
                    criar_cliente(clientes)

                case "nc":
                    numero_conta = len(contas) + 1
                    criar_conta(numero_conta, clientes, contas)

                case "lc":
                    listar_contas(contas)

                case "q":
                    raise KeyboardInterrupt
            
                case _:
                    raise KeyboardInterrupt
    
    except KeyboardInterrupt:
        pass

main()
