print("""
Bem Vindo ao DIO Bank!
      
O que deseja fazer?
Escolha uma das opçôes a baixo para proseguir""")

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
        try:
            valor = float(input("Informe o valor do depósito: "))
        
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("""
                Deposito efetuado com sucesso!
                
                Escolha uma das opções a baixo para proseguir.""")
                
            else:
                print("Operação falhou! O valor informado é inválido.")

        except ValueError:
            print("OPS! Caractere inválido. Por favor, digite o valor que deseja depositar.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

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
                
                print("""
                Saque efetuado com sucesso!
                
                Escolha uma das opções a baixo para proseguir.""")

            else:
                print("Operação falhou! O valor informado é inválido.")
                
        except ValueError:
            print("OPS! Caractere inválido. Por favor, digite o valor que deseja sacar.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
