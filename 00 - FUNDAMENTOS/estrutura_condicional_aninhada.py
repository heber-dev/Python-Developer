conta_padrao = True
conta_estudante = False
conta_vip = False

saldo = 5000
saque = 10000
cheque_especial = 1450

if conta_padrao:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_estudante:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_vip:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")