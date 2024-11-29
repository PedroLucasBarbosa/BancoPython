from datetime import datetime

class Transacao:
    def __init__(self, tipo, valor, descricao=""):
        self.tipo = tipo  # "DEPÓSITO", "SAQUE", "TRANSFERÊNCIA"
        self.valor = valor
        self.descricao = descricao
        self.data_hora = datetime.now()

    def __str__(self):
        return f"[{self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}] {self.tipo}: R${self.valor:.2f} ({self.descricao})"
