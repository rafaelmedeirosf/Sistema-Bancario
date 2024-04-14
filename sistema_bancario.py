menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
quantidade_depositos = 0
LIMITE_SAQUES = 3

while True:

        opção = input(menu)

        if opção == "1":
                   
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                quantidade_depositos += 1
            else:
             print("Operação falhou! O valor informado é inválido.")


        
        elif opção == "2":
            print("Saque")

            valor = float(input("Informe o valor do saque: "))

            saldo_insuficiente = valor > saldo
            limite_saques = numero_saques >= LIMITE_SAQUES
            valor_limite = valor > 500

            
            
            if saldo_insuficiente:
                print(f"Operação falhou, saldo insuficiente, o valor atual do seu saldo é: R${saldo}")
            
            elif valor_limite:
                print("Operação falhou, valor limite de saque R$500,00")
            
            elif limite_saques:
                print("Saque não realizado, Você execeu o limite de saques diarios")            

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque realizado R$ {valor:.2f}\n"
                numero_saques += 1
            
            else:
                print("Operação falhou, valor informado invalido.")


        elif opção == "3":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print(f"Foram realizados {quantidade_depositos} depositos no periodo")
            
            if numero_saques < LIMITE_SAQUES:
                print(f"Foram realizados {numero_saques} saques no periodo você ainda pode efetuar mais {LIMITE_SAQUES - numero_saques} saque(s) no periodo")
            
            else:
                print(f"Foram realizados {numero_saques} saques no periodo você não pode mais efetuar saques, limite de saques = {LIMITE_SAQUES}")
            print("==========================================")


        elif opção == "0":
            break
        
        else:
             print("Operação inválida, por favor selecione novamente a operação desejada.")