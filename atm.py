print("Bem-Vindo ao Caixa eletrónico online!")
restart = 'y'
saldo = 1500
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
            retirar = float(input())
            if retirar == 1:
                print("Quanto deseja retirar?")
                retirar = float(input())
                saldo_atual = saldo - retirar
                print(f"Seu saldo atual é de: {saldo_atual}")
                continuar = str(input("Deseja continuar?"))
                if continuar in ('n','N','não','nao'):
                    break
            if retirar in [10, 20, 50, 100]:
                retirar_atual = saldo - retirar
                print(f"Seu saldo é de: {retirar_atual}")
                continuar = str(input("Deseja continuar?"))
                if continuar in ('n','N','não','nao'):
                    break
            elif retirar in [10,20,50,100]:
                print('Informe um valor válido!')

            
        elif opcao == 3:
            print("Qual o valor que deseja depositar?")
            depositar_valor = float(input(""))
            depositar_valor_saldo = saldo + depositar_valor
            print(f"Seu saldo é de: {depositar_valor_saldo}")
        elif opcao == 4:
            pass

    
    elif chances <= 0:
        print("Suas tentativas acabaram")
    else:
        print(f"senha incorreta, {chances} Tentativa ")
        chances -= 1

#Codificação Davu macuxi#0001
