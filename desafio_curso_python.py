menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Informe o valor que deseja depositar: "))

        if deposito > 0:
            saldo = saldo + deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"

    elif opcao == "2":
        saque = float(input("Informe o valor que deseja sacar: "))

        if saldo < saque:
            print("Operação falhou! Saldo insuficiente. \nO seu saldo é de: ", saldo)
        elif saque > limite:
            print("Operação falhou! \nO valor limite para cada saque é de: ", limite)
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Limite de saques diários excedido.\nSeu limite de saques é de: ", LIMITE_SAQUES)
        elif saque > 0:
            saldo = saldo - saque
            numero_saques = numero_saques + 1
            extrato += f"Saque: R$ {saque:.2f}\n"
        else:
          print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "3":
      print("\n================= extrato ==================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("============================================")
      
    elif opcao == "4":      
      print("\n      ################## Volte Sempre ################## \n")
      break

    else:
        print("Operação inválida! por favor selecione novamente a operação desejada.")
