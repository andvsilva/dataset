

Clientes = {'cod':[], 'nome': [], 'tel': [], 'cc': []}
Contas = {'cod':[], 'saldo':[], 'tr':[]}
Transf = {'cod':[], 'tipo':[],'origem':[],'destino': [], 'valor': []}

numClientes = 0

class banco:
    def CadastrarCliente():
        global numClientes

        if numClientes < 3:
            print(">>>>>>>> Cadastrar Cliente <<<<<<<<")
            cod = input('\n Informe o código do cliente: ')
            nome = input('\n Informe o nome do cliente: ')
            tel = input('\n Informe o telefone do cliente: ')
            cc = input('\n Informe o numero da conta corrente do cliente: ')
            pdeposito = float(input("Informe o valor do deposito inicial: "))

            Clientes['cod'].append(cod)
            Clientes['nome'].append(nome)
            Clientes['tel'].append(tel)
            Clientes['cc'].append(cc)
            Contas['cod'].append(cod)
            Contas['saldo'].append(pdeposito)
            numClientes += 1
        else:
            print('\n Numero maximo de clientes atingido!!')
            print('Encerrando o sistema...')
        
        return Clientes, Contas

    def ConsultarCliente():
        print(">>>>>>>> Consulta Cliente <<<<<<<<")
        cod = input('\n Informe o codigo do cliente: ')

        codv = cod in Clientes['cod'] # retorna True ou False

        if codv == True:
            pos = Clientes['cod'].index(cod)
            
            print(f"{'Codigo'}  {'Nome':>10} {'Telefone':>20} {'Conta':>20} {'Saldo': >15}")
            print(f"{Clientes['cod'][pos]}  {Clientes['nome'][pos]:>12} {Clientes['tel'][pos]:>22} {Clientes['cc'][pos]:>20} {Contas['saldo'][pos]: >15}")
        else:
            print('Código Inválido!!')
    
    def AtualizarCadastro():
        print(">>>>>>>> Atualizar Cadastro <<<<<<<<")
        cod = input('\n Informe o codigo do cliente: ')

        codv = cod in Clientes['cod'] # retorna True ou False
        if codv == True:
            novonome = input("Informe o novo nome do cliente: ")
            novotel = input("Informe o novo telefone do cliente: ")

            pos = Clientes['cod'].index(cod)

            Clientes['nome'][pos] = novonome
            Clientes['tel'][pos] = novotel
            print('Dados do cliente atualizado!!!')
        else:
            print('>>>> Codigo Invalido!!!')
            
    def RemoverCliente():
        print(">>>>>>>>  Remover Cliente <<<<<<<<")
        cod = input('\n Informe o codigo do cliente: ')
        codv = cod in Clientes['cod'] # retorna True ou False
        
        if codv == True:
            pos = Clientes['cod'].index(cod)
            Clientes['cod'].pop(pos)
            Clientes['nome'].pop(pos)
            Clientes['tel'].pop(pos)
            Clientes['cc'].pop(pos)
            Contas['cod'].pop(pos)
            Contas['saldo'].pop(pos)

            print('Cliente removido com sucesso!!')
        else:
            print('Codigo Invalido!!!')

    def ListaDeClientes():
        print(">>>>>>>>  Lista de Cliente <<<<<<<<")
        global numClientes
        print(f"{'Codigo'}  {'Nome':>10} {'Telefone':>30} {'Conta':>20} {'Saldo': >15}")
        print('\n')

        for pos in range(numClientes):
            print(f"{Clientes['cod'][pos]}  {Clientes['nome'][pos]:>12} {Clientes['tel'][pos]:>28} {Clientes['cc'][pos]:>20} {Contas['saldo'][pos]: >15}")
            
class cliente:
    def Transferencia():
        print(">>>>>>>>  Transferencia <<<<<<<<")
        cod1 = input('\nInforme o codigo do cliente que fara a transferencia: ')
        codv1 = cod1 in Clientes['cod'] # retorna True ou False

        cod2 = input('\nInforme o codigo do cliente que recebera a transferencia: ')
        codv2 = cod2 in Clientes['cod'] # retorna True ou False

        if codv1 == True and codv2 == True:
            pos1 = Clientes['cod'].index(cod1)
            pos2 = Clientes['cod'].index(cod2)

            valorf = float(input('\n Informe o valor de Transferencia: '))
            valor1 = Contas['saldo'][pos1]
            valor1 = valor1 - valorf
            Contas['saldo'][pos1] = valor1   

            valor2 = Contas['saldo'][pos2]
            valor2 = valor2 + valorf
            Contas['saldo'][pos2] = valor2

            print('Tranferencia realizada com sucesso!!')
        else:
            print("Contas Inválidas!!!")  