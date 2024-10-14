
def menu():

    navegacao = """
    [s] Saque
    [d] Deposito
    [e] Extrato
    [f] Fechar
    """
    return input(navegacao)

def sacar(saldo,valor,extrato,limite,numero_saques,limite_saques):
        
        excedeu_saldo = valor > saldo 

        excedeu_limite = valor >= limite

        excedeu_saques = numero_saques > limite_saques

        if excedeu_saldo:
            print("Falha ao sacar! Verifique se existe a quantia em saldo.")

        elif excedeu_limite:
            print(f"Falha ao sacar! Há um limite de R$ {limite:.2f} por saque.")

        elif excedeu_saques:
            print(f"Falha ao sacar! Há uma quantidade limite de {limite_saques} saques diários")

        elif valor > 0:
            saldo -= valor 
            extrato += f"\nSaque: R$ {valor:.2f}\n"
            numero_saques +=1
            print("\n*** Saque realizado com sucesso! ***")
        
        else:
            print("Falha! O valor informado é inválido.")
        return saldo, extrato


def exibir_extrato(saldo, extrato):
    temp_message = "Não houve movimentações nesta conta."
    print("******************** EXTRATO ********************")
    if not extrato:
        print(temp_message)
    else:
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("*************************************************")
    

def depositar(saldo,valor,extrato):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito de R$ {valor:.2f}"
        print("\n*** Depósito realizado com sucesso! ***")
    else:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato



def main():
    saldo = 0
    extrato = ""
    numero_saques = 0
    limite = 500
    LIMITE_SAQUES = 3

    while True:
        opcao = menu()

        if opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo,extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                                  )

        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "f":
            break

        else:
            print("Operação inválida, selecione uma operação listada anteriormente.")
main()