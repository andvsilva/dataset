import banco

class Caixa(banco.Banco):
    print('>>>>>> Banco Caixa <<<<<<<')
    def __init__(self, nome, sobrenome, login, senha):
        super().__init__(nome, sobrenome, login, senha)