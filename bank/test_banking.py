import Banking as bk

Clientes, Contas = bk.banco.CadastrarCliente()

print(Clientes)
print(Contas)

bk.banco.ConsultarCliente()
bk.banco.AtualizarCadastro()

bk.banco.ConsultarCliente()

bk.banco.RemoverCliente()
#bk.banco.ConsultarCliente()