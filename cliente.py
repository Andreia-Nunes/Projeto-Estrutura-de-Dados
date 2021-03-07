class Cliente:
    def __init__(self, nome, cpf, salario, financiamento=[], emprestimos=[]):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._financiamento = financiamento
        self._emprestimos = emprestimos

    # ----------------Propriedades--------------------

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def salario(self):
        return self._salario

    @property
    def financiamento(self):
        return self._financiamento

    @property
    def emprestimos(self):
        return self._emprestimos

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf

    @salario.setter
    def salario(self, novo_salario):
        self._salario = novo_salario

    @financiamento.setter
    def financiamento(self, novo_financiamento):
        self._financiamento = novo_financiamento

    @emprestimos.setter
    def emprestimos(self, novos_emprestimos):
        self._emprestimos = novos_emprestimos

    # --------------------------------------------------

    def total_financiado(self):
        soma_financiamentos = 0

        for i in range(0, len(self._financiamento)):
            soma_financiamentos = soma_financiamentos + self._financiamento[i].valor_financiamento

        return soma_financiamentos


    def add_emprestimo(self, valor_emprestimo):
        self._emprestimos.append(valor_emprestimo)


    def soma_emprestimos(self):
        soma = float

        soma = 0

        for i in range(0, len(self._emprestimos)):
            soma = soma + self._emprestimos[i]

        return soma


    def __str__(self):
        financiamento = ''

        for i in range(0, len(self._financiamento)):
            financiamento = financiamento  + f"\n   Imóvel: {self._financiamento[i].imovel.tipo} \n   Valor: {self._financiamento[i].valor_financiamento:.2f}\n"

        return "* NOME: {} \n* CPF:{} \n* SALÁRIO:{} \n* FINANCIAMENTOS: \n{} \n* SOMA DE EMPRÉSTIMOS: {} R$".format(self._nome, self._cpf, self._salario, financiamento, self.soma_emprestimos())
