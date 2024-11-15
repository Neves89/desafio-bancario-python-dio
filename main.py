menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Qual o Valor a Ser Depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor: .2f}\n"
        else:
            print("Valor Informado Invalido.")
    
    elif opcao == "2":
        valor = float(input("Informe o Valor do Saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Negada! Sem Saldo Suficiente")
        
        elif excedeu_limite:
            print("Falhou! Valor Excede o Limite")

        elif excedeu_saques:
            print("Falhou! Maximo de Saques Diarios Excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Operaçao Falhou!")

    elif opcao == "3":
        print("\n>>>>>>>>>>>> Extrato <<<<<<<<<<<<")
        print("Sem Novas Movimentaçoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("*********************************")

    elif opcao == "0":
        break

    else:
        print("Opçao Invalida! Tente Novamente")

