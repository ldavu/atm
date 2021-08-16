print("Bem-Vindo ao Caixa eletrónico online!")
restart = 'y'
saldo = (f"R${1500.00}")
chances = 3
while chances >= 0:
    senha = int(input("Digite sua senha de 4 dígitos: "))
    if senha == (1234):
        print("Você entrou na conta com sucesso!")
        print("presione 1 para ver o saldo no banco")
        print("Presione 2 para retirar um valor")
        print("Presione 3 para depositar um valor")
        #print("Presione 4 para retornar cartão")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            print(f"Seu saldo é de {saldo}")
            continuar = str(input("Deseja continuar?"))
            if continuar in ('n','N','não','nao'):
                break
        elif opcao == 2:
            print("Qual o valor que deseja retirar da carteira? 10, 20, 50, 100 para outros valores digite 1")
            retirar = input("")
            if retirar in [10,20,50,100]:
                retirar_atual = retirar - saldo
                print(f"Seu saldo é de: {saldo}")
                continuar = str(input("Deseja continuar?"))
                if continuar in ('n','N','não','nao'):
                    break
            elif retirar != [10, 20, 50, 100]:
                print("Desculpe, coloque um valor válido!")
            if retirar == 1:
                print("Quanto deseja retirar?")
                retirar = float(input(""))
                if retirar in [10,20,50,100]:
                    print("Coloque um valor válido!")
                else:
                    saldo_atual = retirar - saldo
                    print(f"Seu saldo atual é de: {saldo}")
                    continuar = str(input("Deseja continuar?"))
                    if continuar in ('n','N','não','nao'):
                        break
            
        elif opcao == 3:
            print("Qual o valor que deseja depositar?")
            depositar_valor = float(input(""))
            depostiar_valor_saldo = depositar_valor + saldo
            print(f"Seu saldo é de: {saldo}")
        elif opcao == 4:
            pass

    
    elif chances <= 0:
        print("Suas tentativas acabaram")
    else:
        print(f"senha incorreta, {chances} Tentativa ")
        chances -= 1

#Codificação Davu macuxi#0001
