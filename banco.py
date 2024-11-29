from conta import Conta

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero, titular, saldo_inicial=0):
        if numero in self.contas:
            print("Erro: Já existe uma conta com este número.")
            return
        nova_conta = Conta(numero, titular, saldo_inicial)
        self.contas[numero] = nova_conta
        print(f"Conta {numero} criada com sucesso para {titular}.")

    def buscar_conta(self, numero):
        return self.contas.get(numero, None)

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta registrada no banco.")
            return
        print("\n=== Contas Registradas ===")
        for numero, conta in self.contas.items():
            print(f"Conta {numero}: {conta.titular} (Saldo: R${conta.saldo:.2f})")
