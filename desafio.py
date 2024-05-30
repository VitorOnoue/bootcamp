menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input())
        if valor < 0:
            print()
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        

    elif opcao == "s":
        valor = float(input())
        if valor > limite:
            print("saques podem ser de até 500, saque não efetuado")
        else:
            numero_saques += 1
            if numero_saques > LIMITE_SAQUES:
                print("limite de saques excedido, saque não efetuado")
            elif valor > saldo:
                print("saldo insuficiente, saque não efetuado")
            elif valor < 0:
                print()
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"

    elif opcao == "e":
        print(extrato)
        print(f"R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")