#menu = """

#[1]Depositar 
#[2]Sacar
#[3]Extrato
#[4]Listar Contas
#[5]Novo Usuario
#[6]Nova Conta
#[0]Sair

#=>"""
def menu():
    menu_str = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Listar Contas
    [5] Novo Usuario
    [6] Nova Conta
    [0] Sair
    =>"""
    return input(menu_str) 

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("Deposito Realizado")
    else:
        print("Operaçao Falhou")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operaçao Falhou")
    elif excedeu_limite:
        print("Operaçao Falhou")
    elif excedeu_saques:
        print("Operaçao Falhou")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque Realizado Com Sucesso")
    else:
        print("Operaçao Falhou, Valor Invalido")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n>>>>>>>>>>>> Extrato <<<<<<<<<<<<")
    print("Sem Novas Movimentaçoes." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo: .2f}")
    print("*********************************")

def novo_usuario(usuarios):
    cpf = input("Digite o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Usuario ja Cadastrado")
        return
    nome = input("Informe o Nome Completo: ")
    data_nascimento = input("Digite a Data de Nascimento: ")
    endereco = input("Digite o endereço completo (rua, numero - bairro - cidade/estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuario Criado Com Sucesso")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta Criada Com Sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario nao Encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agencia: {conta['agencia']}
            c/c: {conta['numero_conta']}
            Titular: {conta ['usuario']['nome']}
        '''
        print("=" * 100)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "1":
            valor = float(input("Informe o Valor de Deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "5":
            novo_usuario(usuarios)
        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = nova_conta_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "4":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operaçao Invalida, Selecione Novamente")

main()