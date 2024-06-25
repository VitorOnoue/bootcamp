from abc import ABC, abstractmethod

AGENCIA = "0001"

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0 # float
        self._numero = numero # int
        self._agencia = AGENCIA # str
        self._cliente = cliente # Cliente
        self._historico = Historico() # Historico

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(0, numero, cliente) # Conta
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self.saldo(saldo - valor)
            print("Saque feito com sucesso.")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")

        return False
    
    def depositar(self, valor):
        saldo = self.saldo
        if valor > 0:
            self.saldo(saldo + valor)
            print("Depósito feito com sucesso.")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
        return False
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite, limite_saques):
        super().__init__(self, numero, cliente)
        self._limite = limite # float
        self._limite_saques = limite_saques # int

    # falta logica para limite saques e valor maximo de saque

class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append({"tipo": transacao.__class__.__name__, "valor": transacao.valor, "data": "1234-56-78"})

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco # str
        self._contas = [] # list

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super.__init__(self, endereco, contas)
        self._cpf = cpf # str
        self._nome = nome # str
        self._data_nascimento = data_nascimento # date

class Transacao(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def registrar(conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor # float

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        flag = conta.depositar(self.valor)
        if flag:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor # float

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        flag = conta.sacar(self.valor)
        if flag:
            conta.historico.adicionar_transacao(self)