import Banking as bk
import json

Clientes, Contas = bk.banco.CadastrarCliente(1258, 'A', 5454, 125810, 1000)
Clientes, Contas = bk.banco.CadastrarCliente(1259, 'B', 464894, 125910, 1200)
Clientes, Contas = bk.banco.CadastrarCliente(1260, 'C', 466464, 126010, 1500)

print(Clientes)
print(Contas)

bk.banco.ConsultarCliente(1258)
bk.banco.AtualizarCadastro(1258, 'AB', 258963)

bk.banco.ConsultarCliente(1258)
bk.banco.RemoverCliente(1260)
bk.banco.ConsultarCliente(1259)

bk.banco.ListaDeClientes()

bk.cliente.Transferencia(1258, 1259, 600)
bk.cliente.Transferencia(1259, 1258, 200)
bk.cliente.Transferencia(1258, 1259, 100)

print(Contas)
bk.cliente.Deposito(1258, 600)
bk.cliente.Extrato(1258)
print(Contas)

print("salvando os dados dos cliente em format json")

with open('clientes.json', 'w') as fp:
    json.dump(Clientes, fp,  indent=2)
    
with open('contas.json', 'w') as fp:
    json.dump(Contas, fp,  indent=4)