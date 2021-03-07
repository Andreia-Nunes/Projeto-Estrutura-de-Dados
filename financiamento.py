class Financiamento:
    def __init__(self, cliente, imovel, banco, valor, aportes):
        self._cliente = cliente
        self._imovel = imovel
        self._banco = banco
        self._valor_financiamento = valor
        self._num_aportes = aportes

    #----------------Propriedades--------------------
    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, novo_cliente):
        self._cliente = novo_cliente


    @property
    def imovel(self):
        return self._imovel

    @imovel.setter
    def imovel(self, novo_imovel):
        self._imovel = novo_imovel


    @property
    def banco(self):
        return self._banco

    @banco.setter
    def banco(self, novo_banco):
        self._banco = novo_banco


    @property
    def valor_financiamento(self):
        return self._valor_financiamento

    @valor_financiamento.setter
    def valor_financiamento(self, novo_valor):
        self._valor_financiamento = novo_valor


    @property
    def numero_aportes(self):
        return self._num_aportes

    @numero_aportes.setter
    def numero_aportes(self, novo_aporte):
        self._num_aportes = novo_aporte

    #------------------------------------------------

    def receber_aporte(self, valor):
        self._valor_financiamento = self.valor_financiamento - valor

        self._num_aportes += 1

    def __str__(self):
        return f"Cliente: {self._cliente.nome} \nImóvel: {self._imovel.tipo} \nBanco: {self._banco.nome_do_banco} \nValor do financiamento: {self._valor_financiamento} R$ \nNúmero de aportes: {self._num_aportes}\n"