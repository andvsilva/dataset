from datetime import datetime


class Cliente:
    def __init__(self, nome, sobrenome, login, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = login
        self.senha = senha

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

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
        self.extrato = Extrato()
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.extrato = Extrato()

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