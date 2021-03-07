class Conta:
    def __init__(self, saldo, id, cliente):
        self._saldo = saldo
        self._id = id
        self._cliente = cliente

    # ----------------Propriedades--------------------
    @property
    def saldo(self):
        return self._saldo

    @property
    def id(self):
        return self._id

    @property
    def cliente(self):
        return self._cliente

    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @cliente.setter
    def cliente(self, novo_cliente):
        self._cliente = novo_cliente

    # ------------------------------------------------
    def creditar(self, valor_credito):
       self._saldo = self._saldo + valor_credito

    def debitar(self, valor_debito):
        if self._saldo >= valor_debito:
            self._saldo = self._saldo - valor_debito
        else:
            print("Saldo insuficiente")

    def transferencia(self, valor_debitado, outra_conta):
        if self._saldo >= valor_debitado:
            self._saldo = self._saldo - valor_debitado
            outra_conta.creditar(valor_debitado)
        else:
            print("Saldo insuficiente")

    def __str__(self):
        return "* ID: {} \n* CLIENTE: {} \n* SALDO: {} R$".format(self._id, self._cliente.nome, self._saldo)