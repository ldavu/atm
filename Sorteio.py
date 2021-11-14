import random
from time import sleep
import os

def Caixa():
    exec(open("CaixaHub.py").read())

def sortear():
    aleatorio = random.randint(1,100)


print("================\nBem-vindo ao sorteio\nVocê pode ganhar vários prêmios!\n================")
print("\nCaso queira voltar para o Caixa a qualquer hora digite 'sair'")
sair_Programa = ""

resposta = str(input())
if(resposta == "sair"):
    exec(open("BancoBrasileiro\CaixaHub.py").read())
    quit("Sorteio.py")
    

while(sair_Programa != "sim"):
    pass
