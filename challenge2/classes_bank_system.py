class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    def saldo(self):
        return self.saldo

    def nova_conta(self, cliente, numero):
        pass

    def sacar(self. valor):
        if self.saldo() >= valor:
            return True
        else:
            return False

    def depositar(self, valor):
        if valor > 0:
            return True
        else:
            return False


class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques


class Cliente:
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = list(contas)

    def realizar_transacao(self, conta, trasacao):
        return conta.transacao()

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
