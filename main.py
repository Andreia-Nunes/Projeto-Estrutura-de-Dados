from banco import *
from cliente import *
from conta import *
from financiamento import *
from imovel import *


vetor_clientes = []
vetor_contas = []
vetor_financiamentos = []
vetor_imoveis = []
banco = Banco("Banco do Brasil", [], [])

flag: str

flag = "S"

while flag == "S":
    opcao: int

    print("\n************************** MENU **************************")
    print("\nOpções:")
    print("\n1- Criar uma conta")
    print("2- Consultar financiamentos de um cliente")
    print("3- Realizar uma transferência")
    print("4- Consultar o total de valor nas contas do banco")
    print("5- Consultar o total dos financiamentos de um cliente")
    print("6- Realizar um empréstimo")
    print("7- Consultar total de empréstimos de um cliente")
    print("8- Sair")
    opcao = int(input("\nInsira a opção desejada: "))


    if opcao == 1:
        quantidade_contas: int
        quantidade_contas = int(input("\nQuantas contas deseja-se criar? "))

        for i in range(0, quantidade_contas):
            #Criando objetos Cliente:
            print()
            print("Cliente:")
            nome_cliente = input("Nome do cliente: ")
            cpf_cliente = input("CPF: ")
            salario_cliente = float(input("Salário: "))
            financiamento_cliente = []
            emprestimos_cliente = []

            cli = Cliente(nome_cliente, cpf_cliente, salario_cliente, financiamento_cliente, emprestimos_cliente)
            vetor_clientes.insert(i, cli)


            #Criando objetos Conta:
            print("\nConta:")
            saldo_conta = float(input("Saldo da conta: "))
            id_conta = int(input("ID da conta: "))
            cliente_conta = vetor_clientes[i]

            con = Conta(saldo_conta, id_conta, cliente_conta)
            vetor_contas.insert(i, con)

            #Repassando as contas para o atributo self._contas de Banco:
            banco.contas.append(vetor_contas[i])

            #Criando objetos Imóvel e Financiamento:
            resp: str

            print()
            resp = input("Deseja realizar um financiamento? (S/N) ").upper()

            if resp == "S":
                #Imóvel:
                print()
                print("Imóvel:")
                tipo_imovel = input("Tipo do imóvel: ")
                valor_imovel = float(input("Valor do imóvel: "))
                codigo_imovel = int(input("Código: "))

                imov = Imovel(tipo_imovel, valor_imovel, codigo_imovel)

                vetor_imoveis.insert(i, imov)

                #Financiamentos:
                print()
                print("Financiamento:")
                cliente_financiamento = vetor_clientes[i]
                imovel_financiamento = vetor_imoveis[i]
                valor_financiamento = float(input("Valor do financiamento: "))
                aporte_financiamento = int(input("Quantidade de aportes: "))

                fin = Financiamento(cliente_financiamento, imovel_financiamento, banco, valor_financiamento, aporte_financiamento)

                vetor_financiamentos.insert(i, fin)

                # Repassando as os financiamentos para o atributo self._financiamentos de Banco:
                banco.financiamento.append(fin)

                #Repassando o financiamento para o atributo self._financiamentos de Cliente:
                vetor_clientes[i].financiamento.append(vetor_financiamentos[i])

                print()

    elif opcao == 2:
        cpf_clien: str

        cpf_clien = input("\nInsira o CPF do cliente: ")
        print()

        for i in range(0, len(vetor_clientes)):
            if cpf_clien == vetor_clientes[i].cpf:
                banco.financiamentos_cliente(cpf_clien)

    elif opcao == 3:
        conta_transferidora: int
        conta_recebedora: int
        valor_transferido: float
        endereco_recebedora: object

        conta_transferidora = int(input("\nInsira o ID da sua conta: "))
        conta_recebedora = int(input("Insira o ID da conta recebedora: "))
        valor_transferido = float(input("Valor da transferência: "))

        for i in range(0, len(vetor_contas)):
            if conta_recebedora == vetor_contas[i].id:
                endereco_recebedora = vetor_contas[i]
                break

        for i in range(0, len(vetor_contas)):
            if conta_transferidora == vetor_contas[i].id:
                vetor_contas[i].transferencia(valor_transferido, endereco_recebedora)
                break

        print("\nTransferência realizada com sucesso!")

        for i in range(0, len(vetor_contas)):
            if conta_transferidora == vetor_contas[i].id:
                print(f"\nSaldo da conta {conta_transferidora}: {vetor_contas[i].saldo:.2f} R$")
                break

        for i in range(0, len(vetor_contas)):
            if conta_recebedora == vetor_contas[i].id:
                print(f"Saldo da conta {conta_recebedora}: {vetor_contas[i].saldo:.2f} R$ ")

    elif opcao == 4:
        print(f"\n Total nas contas do banco: {banco.total_valor_contas()} RS")


    elif opcao == 5:
        cliente_cpf: str

        cliente_cpf = (input("\nInsira o CPF do cliente: "))

        for i in range(0, len(vetor_clientes)):
            if cliente_cpf == vetor_clientes[i].cpf:
                print(f"Total financiado: {vetor_clientes[i].total_financiado()} R$")

    elif opcao == 6:
        cli_cpf: str
        valor_emprestimo: float

        cli_cpf = (input("\nInsira o CPF do cliente: "))
        valor_emprestimo = float(input("Valor do empréstimo: "))

        for i in range(0, len(vetor_clientes)):
            if cli_cpf == vetor_clientes[i].cpf:
                vetor_clientes[i].add_emprestimo(valor_emprestimo)
                break

        print("Empréstimo realizado com sucesso!")

    elif opcao == 7:
        cl_cpf: str

        cl_cpf = input("\nInsira o CPF do cliente: ")

        for i in range(0, len(vetor_clientes)):
            if cl_cpf == vetor_clientes[i].cpf:
                print(f"Soma de emprésimos do cliente: {vetor_clientes[i].soma_emprestimos()} R$")

    elif opcao == 8:
        flag = "N"
        print("\nSESSÃO ENCERRADA!")
        break

    #Flag:
    flag = input("\nDeseja realizar outra operação? (S/N) ").upper()

else:
    print("\nSESSÃO ENCERRADA!")













