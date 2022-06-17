Clientes = {'cod':[], 'nome': [], 'tel': [], 'cc': []}
Contas = {'cod':[], 'saldo':[], 'tr':[]}
Transf = {'cod':[], 'tipo':[],'origem':[],'destino': [], 'valor': []}

numClientes = 0

class banco:
    def CadastrarCliente():
        global numClientes

        if numClientes < 3:
            #cod = input('\n Informe o código do cliente: ')
            cod = 12589632
            #nome = input('\n Informe o nome do cliente: ')
            nome = "Jason Peterson"
            #tel = input('\n Informe o telefone do cliente: ')
            tel = 1925846325
            #cc = input('\n Informe o numero da conta corrente do cliente: ')
            cc = 145825693
            #pdeposito = float(input("Informe o valor do deposito inicial: "))
            pdeposito = 1236.5

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
        
        #cod = int(input('\n Informe o codigo do cliente: '))
        cod = 12589632
        codv = cod in Clientes['cod'] # retorna True ou False

        if codv == True:
            pos = Clientes['cod'].index(cod)
            
            print(f"{'Codigo'}  {'Nome':>10} {'Telefone':>20} {'Conta':>20} {'Saldo': >15}")
            print(f"{Clientes['cod'][pos]}  {Clientes['nome'][pos]:>12} {Clientes['tel'][pos]:>22} {Clientes['cc'][pos]:>20} {Contas['saldo'][pos]: >15}")
        else:
            print('Código Inválido!!')
    
    def AtualizarCadastro():
      
        #cod = int(input('\n Informe o codigo do cliente: '))
        cod = 12589632
        codv = cod in Clientes['cod'] # retorna True ou False
        if codv == True:
            #novonome = input("Informe o novo nome do cliente: ")
            #novotel = input("Informe o novo telefone do cliente: ")
            novonome = "Jason Peter"
            novotel = 144555856856
            pos = Clientes['cod'].index(cod)

            Clientes['nome'][pos] = novonome
            Clientes['tel'][pos] = novotel
            print('Dados do cliente atualizado!!!')
        else:
            print('>>>> Codigo Invalido!!!')
            
    def RemoverCliente():
        #cod = input('\n Informe o codigo do cliente: ')
        cod = 12589632
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
