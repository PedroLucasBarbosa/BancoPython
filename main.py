from banco import Banco

def exibir_menu():
    print("\n=== Sistema Bancário ===")
    print("1. Criar conta")
    print("2. Listar contas")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Transferir")
    print("6. Exibir extrato")
    print("7. Sair")

def main():
    banco = Banco()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Digite o número da conta: ")
            titular = input("Digite o nome do titular: ")
            saldo_inicial = float(input("Digite o saldo inicial (ou deixe vazio para 0): ") or 0)
            banco.criar_conta(numero, titular, saldo_inicial)
        
        elif opcao == "2":
            banco.listar_contas()
        
        elif opcao == "3":
            numero = input("Digite o número da conta para depósito: ")
            conta = banco.buscar_conta(numero)
            if conta:
                valor = float(input("Digite o valor do depósito: "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            numero = input("Digite o número da conta para saque: ")
            conta = banco.buscar_conta(numero)
            if conta:
                valor = float(input("Digite o valor do saque: "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            origem = input("Digite o número da conta de origem: ")
            destino = input("Digite o número da conta de destino: ")
            valor = float(input("Digite o valor da transferência: "))
            conta_origem = banco.buscar_conta(origem)
            conta_destino = banco.buscar_conta(destino)

            if conta_origem and conta_destino:
                conta_origem.transferir(valor, conta_destino)
            else:
                print("Uma ou ambas as contas não foram encontradas.")

        elif opcao == "6":
            numero = input("Digite o número da conta para exibir o extrato: ")
            conta = banco.buscar_conta(numero)
            if conta:
                conta.exibir_extrato()
            else:
                print("Conta não encontrada.")
        
        elif opcao == "7":
            print("Encerrando o sistema bancário...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
