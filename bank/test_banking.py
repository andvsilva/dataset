import Banking as bk

Clientes, Contas = bk.banco.CadastrarCliente()
Clientes, Contas = bk.banco.CadastrarCliente()
Clientes, Contas = bk.banco.CadastrarCliente()

print(Clientes)
print(Contas)

bk.banco.ConsultarCliente()
bk.banco.AtualizarCadastro()

bk.banco.ConsultarCliente()
bk.banco.RemoverCliente()
bk.banco.ConsultarCliente()

bk.banco.ListaDeClientes()

bk.cliente.Transferencia()
bk.cliente.Transferencia()

print(Contas)
bk.cliente.Deposito()
bk.cliente.Extrato()
print(Contas)
