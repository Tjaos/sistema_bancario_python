navegacao = """
[s] Saque
[d] Deposito
[e] Extrato
[f] Fechar

"""
#variaveis
saldo = 0
extrato = ""
qtd_saques = 0

#Constantes
LIMITE = 500
LIMITE_SAQUES = 3


while True:
    opcao = input(navegacao)

    if opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        sem_saldo = valor > saldo 

        sem_limite = valor > LIMITE

        saques_esgotados = qtd_saques > LIMITE_SAQUES

        if sem_saldo:
            print("Falha ao sacar! Verifique se existe a quantia em saldo.")
        elif sem_limite:
            print(f"Falha ao sacar! Há um limite de R$ {LIMITE:.2f} por saque.")
        elif saques_esgotados:
            print(f"Falha ao sacar! Há uma quantidade limite de {LIMITE_SAQUES} saques diários")

        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtd_saques +=1
        
        else:
            print("Falha! O valor informado é inválido.")

            


    elif opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}"
        
        else:
            print("Operação falhou! Valor inválido.")
    
    elif opcao == "e":
        temp_message = "Não houve movimentações nesta conta."
        print("******************** EXTRATO ********************")
        if not extrato:
            print(temp_message)
            continue
        else:
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            print("*************************************************")

    elif opcao == "f":
        break

    else:
        print("Operação inválida, selecione uma operação listada anteriormente.")