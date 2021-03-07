class Imovel:
    def __init__(self, tipo, valor, codigo):
        self._tipo = tipo
        self._valor = valor
        self._codigo = codigo

    #----------------Propriedades--------------------
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo


    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor


    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def cofigo(self, novo_codigo):
        self._codigo = novo_codigo

    # ------------------------------------------------

    def __str__(self):
        return f"Tipo do imóvel: {self._tipo} \nValor: {self._valor:.2f} R$ \nCódigo: {self._codigo}"

