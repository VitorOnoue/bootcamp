class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo
    
    @classmethod
    def nova_conta(cliente, numero):
        return new_conta
    
    def sacar(valor):
        return True
    
    def depositar(valor):
        return False
    
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(self, saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques

# class Historico:
#     def __init__(self):
#         pass

#     def adicionar_transacao(transacao):
#         pass