from transacao import Transacao

class Conta:
    def __init__(self, numero, titular, saldo_inicial=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser maior que zero.")
            return
        self.saldo += valor
        self.extrato.append(Transacao("DEPÓSITO", valor, "Depósito em conta"))
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        self.saldo -= valor
        self.extrato.append(Transacao("SAQUE", valor, "Saque em conta"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("O valor da transferência deve ser maior que zero.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para realizar a transferência.")
            return
        self.saldo -= valor
        conta_destino.depositar(valor)
        self.extrato.append(Transacao("TRANSFERÊNCIA", valor, f"Para conta {conta_destino.numero}"))
        print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero} realizada com sucesso.")

    def exibir_extrato(self):
        print(f"\n=== Extrato da Conta {self.numero} ===")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")
