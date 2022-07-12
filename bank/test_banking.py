import Banking as bk
import json

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
bk.cliente.Transferencia()

print(Contas)
bk.cliente.Deposito()
bk.cliente.Extrato()
print(Contas)

print("salvando os dados dos clientes e contas em format .json")

with open('clientes.json', 'w') as fp:
    json.dump(Clientes, fp,  indent=4)
    
with open('contas.json', 'w') as fp:
    json.dump(Contas, fp,  indent=4)
    
print('feito. :)')