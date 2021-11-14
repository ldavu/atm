from os import close, kill, read, write
from tqdm import tqdm
from time import sleep
import os
'''
def carregando():
    pass
    print("Carregando.")
    for i in range('.', -1, -1):
        print(f"{i} ", end="", flush=True)
        sleep(0.5)
'''

print("Bem-Vindo ao Caixa eletrônico online!")

restart = 'y'
chances = 3
saldo = 2500
arq = open("banco_saldo", 'a')

sleep(2)
print("Gostaria ver entrar na área de sorteios?")
resposta = str(input())
if(resposta == "sim"):
    exec(open("BancoBrasileiro\Sorteio.py").read())
    quit("CaixaHub.py")
    print("\n"*30)
else:
    pass

while chances >= 0:
    senha = int(input("Digite sua senha de 4 dígitos: "))
    if senha == (1234):
        print("Você entrou na conta com sucesso!")
        print("pressione 1 para ver o saldo no banco")
        print("Pressione 2 para retirar um valor")
        print("Pressione 3 para depositar um valor")
        #print("Pressione 4 para retornar cartão") nao existe
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
                if retirar > saldo:
                    print("você está retirando um valor acima do seu saldo!")
                    arq.writelines(f"Erro: Cliente tentou retirar o valor de: {retirar}, acima do saldo na conta que é de: {saldo}\n")
                    arq.close()
                else:
                    saldo_atual = saldo - retirar
                    sleep(1)
                    for i in tqdm(range(5)):
                        sleep(0.5)
                    arq.writelines(f"{saldo_atual}\n")
                    print("Você retirou com sucesso!")
                    print(f"Seu saldo atual é de: {saldo_atual}")
                    continuar = str(input("Deseja continuar?"))
                    arq.close()
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
