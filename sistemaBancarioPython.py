extrato = []
conta = []
limiteQuinhentos = 500
limite_saques = 3


def deposito(conta, extrato):
    depositar = float(input("Informe o valor do depósito: "))
    if depositar <= 0:
        print("Erro, insira um valor positivo ou acima de 1 real")
        return
    print("Valor depositado com Sucesso!")
    conta.append(depositar)
    extrato.append(depositar)
    return extrato, conta
def func_saque(conta, extrato):
    global limite_saques
    global limiteQuinhentos
    saque = int(input("Informe o valor do saque: "))
    if saque > limiteQuinhentos:
        print("Erro, somente valor igual ou menor que 500 reais está disponivel para saque")
    elif saldoAtual(conta) < saque: 
        print("Realize depósito")
    elif limite_saques == 0:
        print("Erro, limite de saque diário excedido")
    else:
        limite_saques -=1
        conta.append(-saque)
        print("Saque concluido com sucesso :D")
        print(f'Saque diário disponivel: {limite_saques}')
        extrato.append(-saque)
        return extrato, conta

def mostrar_extrato(extrato):  
    for i in extrato:
        print(f'Extrato: {i:.2f}')
def saldoAtual(conta):
    saldo_atualizado = 0
    for valor in conta: 
        saldo_atualizado = saldo_atualizado + int(valor)
    print(f'O saldo Atual é de: R$ {saldo_atualizado:.2f}')
    return saldo_atualizado
        
while (True):
    opcao = int(input("Bem vindo ao Banco Python, selecione a operação desejada: \n 1 - Depositar \n 2 - Sacar \n 3 - Extrato \n 4 - Sair \n"))
    if opcao == 1:
       saldoAtual(conta)
       deposito(conta, extrato)
    elif opcao == 2:
        saldoAtual(conta)
        func_saque(conta, extrato)
    elif opcao == 3:
        saldoAtual(conta)
        mostrar_extrato(conta)
    elif opcao == 4:
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
