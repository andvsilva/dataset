from datetime import datetime

## 1 - Criar a class 'banco' com entrada:
# login, senha, dados pessoais.
class banco:
    class Cliente:
        def __init__(self, nome, sobrenome, login, senha):
            self.nome = nome
            self.sobrenome = sobrenome
            self.email = login + '@company.com'
            self.senha = senha

        def nome_completo(self):
            return f'{self.nome} {self.sobrenome}'
        
        def client_info(self):
            return f'{self.nome} {self.sobrenome}\n {self.email}' 

    class Acesso:
        def checa_senha(self, login, senha):
            self.login = login
            self.senha = senha

            if login == self.login and senha == self.senha:
                print(" Conta inicializada")
            else: 
                print('Usuário inválido')

            def mostra_login(self):
                print(self.login)

            def mostra_senha(self):
                print(self.senha)
    class Extrato:
        def __init__(self):
            self.data_abertura = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
            self.transacoes = []

        def imprime(self):
            print('data abertura: {}'.format(self.data_abertura))
            print('transacoes:')
            for i in self.transacoes:
                print('-', i)
                
    class Conta:
        def __init__(self, numero, cliente, saldo, limite = 1000.0):
            self.extrato = banco.Extrato()
            self.numero = numero
            self.cliente = cliente
            self.saldo = saldo
            self.limite = limite
            self.extrato = banco.Extrato()

        def imprimeSaldo(self):
            print("Saldo: R$ %.2f" %self.saldo)

        def deposita(self, valor):
            self.saldo += valor #saldo + valor
            self.extrato.transacoes.append('deposito de {}'.format(valor))

        def saca(self, valor):
            if (self.saldo<valor):
                return False
            else:
                self.saldo -= valor
                self.extrato.transacoes.append('Saque de {}'.format(valor))

        def extrato(self):
            print('numero: {} \nsaldo: {}'.format(self.numero, self.saldo))
            self.extrato.transacoes.append('Tirou extrato- saldo de {}'.format(self.saldo))

        def transfere_para(self, destino, valor):
            retirou = self.saca(valor)
            if(retirou == False):
                return False
            else:
                destino.deposita(valor)
                self.extrato.transacoes.append('Transferencia de {} para a {}'.format(valor, destino.numero))
                return True

## 2 - Criar 3 classes para bancos diferentes:
## Caixa, Banco do Brasil e Sicredi
class Caixa(banco):
    pass

class Banco_do_Brasil(banco):
    pass

class Sicredi(banco):
    pass
        
#cliente1 = banco.Cliente('Rebeca', 'Praia', 'Rebeca234', '12345')
#cliente2 = banco.Cliente('Adriana', 'Mayara', 'Adriana23', '54321')

# cliente1 = Caixa.Cliente('Adriana', 'Mayara', 'Adrianamay', '54321')
# print(cliente1.client_info())

#conta1 = banco.Conta('123-4', cliente1, 1000.0)
#conta2 = banco.Conta('123-5', cliente2, 1000.0)
#conta1.deposita(100.0)
#conta1.saca(50.0)
#conta1.transfere_para(conta2, 200.0)
#conta1.extrato
#conta1.extrato.imprime()
#
#conta2.extrato.imprime()
#
#nome = input('Informe o nome: ')
#sobrenome = input('Informe o sobrenome: ')
#login = input('Informe o seu usuário: ')
#senha = input(' Informe a sua senha: ')
#confirma_senha = input('Confirma a senha: ')

#if senha == confirma_senha:
#  user = banco.Cliente(nome, sobrenome, login, senha)
#else:
#  print('Senha não confere..')
#print('Usuário criado com sucesso!')