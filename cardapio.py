opcao = 0
while opcao != 5:
    print ("Cardápio")
    print ("1- Hamburguer")
    print ("2- Pizza")
    print ("3- Salada")
    print ("4- Refrigerante")
    print ("5- Sair")
    opcao = int ( input("Escola uma opção: "))
    if opcao ==1:
        print("Voê escolheu hamburgue.")
    elif opcao ==2:
        print("Você escolheu pizza.")
    elif opcao ==3:
        print ("Você escolheu salada.")
    elif opcao ==4:
        print ("Você escolheu refrigerante.")
    elif opcao ==5:
        print ("Saindo do cardápio...")
        break
    