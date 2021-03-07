class Banco:
    def __init__(self, nome, contas = [], financiamentos = []):
        self._nome_do_banco = nome
        self._contas = contas
        self._financiamentos = financiamentos

    # ----------------Propriedades--------------------
    @property
    def nome_do_banco(self):
        return self._nome_do_banco

    @nome_do_banco.setter
    def nome_do_banco(self, novo_nome):
        self._nome_do_banco = novo_nome


    @property
    def contas(self):
        return self._contas

    @contas.setter
    def contas(self, novas_contas):
        self._contas = novas_contas


    @property
    def financiamento(self):
        return self._financiamentos

    @financiamento.setter
    def financiamento(self, novos_financiamentos):
        self._financiamentos = novos_financiamentos

    # ------------------------------------------------

    def total_valor_contas(self):
        soma: float
        soma = 0

        for i in range(0, len(self._contas)):
            soma = soma + self._contas[i].saldo

        return soma

    def financiamentos_cliente(self, cpf):
        cpf_da_vez: int

        for i in range(0, len(self._financiamentos)):
            cpf_da_vez = self._financiamentos[i].cliente.cpf

            if cpf_da_vez == cpf:
                for j in range(0, len(self._financiamentos[i].cliente.financiamento)):
                    print(self._financiamentos[i].cliente.financiamento[j])
                break

    def __str__(self):
        conta = ''

        for i in range(0, len(self._contas)):
            conta = conta + f"\n-----{i+1}------ \nCliente: {self._contas[i].cliente.nome} \nSaldo: {self._contas[i].saldo} R$"

        conta = conta + "\n------------\n"


        financiamentos = ''

        for i in range(0, len(self._financiamentos)):
            financiamentos = financiamentos + f"\n-----{i+1}------ \nCliente: {self._financiamentos[i].cliente.nome} \nImóvel: {self._financiamentos[i].imovel.tipo} \nValor: {self._financiamentos[i].valor_financiamento} R$"

        financiamentos = financiamentos + "\n------------\n"

        return f"* NOME DO BANCO: {self._nome_do_banco} \n\n* CONTAS: \n{conta} \n* FINANCIAMENTOS: \n{financiamentos}"

