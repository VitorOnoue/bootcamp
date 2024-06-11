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

"""keyword only saldo, valor, extrato, limite, numero_saques, limite_saques - saldo, extrato"""
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

"""positional only saldo, valor, extrato - saldo, extrato"""
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato

"""positional only saldo - keyword only extrato"""
def ver_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

"""armazenar users em uma lista - usuario = nome, nascimento, cpf, endereço - endereço = logradouro, numero - bairro - cidade/sigla do estado - nao é permitido usuarios com o mesmo cpf"""
def new_user(nome, nasc, cpf, end, users):
    for tup in users:
        if tup[2] == cpf:
            return
    new_user = (nome, nasc, cpf, end)

    return new_user

"""armazenar contas em uma lista - conta = agencia, numero e user - numero da conta começa em 1, e é sequencial. agencia é sempre "0001" - usuario pode ter mais de uma conta"""
def new_account(agencia, cpf, accounts, users):
    for user in users:
        if user[2] == cpf:
            new_account = (agencia, len(accounts) + 1, user)
            return new_account
    return


while True:

    users = []
    accounts = []

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        ver_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        nome = input("Informe seu nome: ")
        nasc = input("Informe sua data de nascimento: ")
        cpf = int(input("Informe seu cpf: "))

        rua = input("Logradouro: ")
        num_lar = int(input("Número da residência: "))
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        sigla = input("Sigla do estado: ")

        endereco = f"{rua}, {num_lar} - {bairro} - {cidade}/{sigla}"

        user = new_user(nome, nasc, cpf, endereco)

        if user is not None:
            users.append(user)

    elif opcao == "a":
        cpf = int(input("Informe seu cpf: "))
        account = new_account("0001", cpf, accounts, users)
        
        if account is not None:
            accounts.append(account)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")