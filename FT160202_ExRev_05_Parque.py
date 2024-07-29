#####################################################################
# 0. Bibliotecas
import sys   # Biblioteca entradas/saídas do sistema
import os    # Biblioteca das funções/comandos do sistema operativo
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
#pip3 install numpy
import numpy as np

##########################################################
# 1. Dados Globais
##########################################################
LIVRE = 0
OCUPADO = 1


##########################################################
# 2. Funções
###########################################################
# Função mostraMenu()
def mostraMenu( ):
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("***********************************")
    print("*                                 *")
    print("*             Parque Gest         *")
    print("*                                 *")
    print("*      1. Listar lugares.         *")
    print("*      2. Marcar lugar.           *")
    print("*      3. Libertar lugar.         *")
    print("*      4. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()
    return


# Função obtemEscolha()
def obtemEscolha(escolha):
    resposta = input(" -> Escolha uma opção (1-4): ")
    if (len(resposta) > 0):  # Evita "out of index error"
        escolha = resposta[0]
    else:
        escolha = 0
    return escolha

# Função processaEscolha()
def processaEscolha(escolha, lugares, nFicheiro, queroSair):
    if (escolha == '1'):
        listarLugares(lugares)
    elif (escolha == '2'):
        ocuparLugar(lugares)
        guardaFicheiro(lugares, nFicheiro)
    elif (escolha == '3'):
        libertarLugar(lugares)
        guardaFicheiro(lugares, nFicheiro)
    elif (escolha == '4'):
        queroSair = sairDoPrograma(queroSair)
    else:
        escolhaInvalida()
    return queroSair

# Função listarLugares()
def listarLugares(lugares):
    print("Listagem de Lugares:")
    for cLugar in range(0,lugares.size,1):
        print(" -> Lugar: ",(cLugar+1),": ", end =" ")
        if (lugares[cLugar] == LIVRE):
            print(" livre.")
        else:
            print(" ocupado.")
    input("Prima qq tecla para continuar ...")
    return

# Função ocuparLugar()
def ocuparLugar(lugares):
    try:
        print("Qual é o lugar a ocupar ( 1 -",lugares.size,")? ",end =" ")
        numLugar = int(input())
        if (numLugar < 1  or numLugar > lugares.size):
            print("Lugar inválido!")
            print("Lugares vão de 1 a ",lugares.size,"!")
        elif (lugares[numLugar-1]==OCUPADO):
            print("Lugar já está ocupado!")
        else:
            lugares[numLugar-1]=OCUPADO
            print("Lugar ocupado com sucesso!")
        input("Prima qq tecla para continuar ...")
        return
    except Exception as e:
        print("Erro ao ler os dados do ficheiro: ", e)

# Função libertarLugar()
def libertarLugar(lugares):
    try:
        print("Qual é o lugar a libertar ( 1 -",lugares.size,")? ",end =" ")
        numLugar = int(input())
        if (numLugar < 1  or numLugar > lugares.size):
            print("Lugar inválido!")
            print("Lugares vão de 1 a ",lugares.size,"!")
        elif (lugares[numLugar-1]==LIVRE):
            print("Lugar já está livre!")
        else:
            lugares[numLugar-1]=LIVRE
            print("Lugar libertado com sucesso!")
        input("Prima qq tecla para continuar ...")
        return
    except Exception as e:
        print("Erro ao ler os dados do ficheiro: ", e)
# Função sairDoPrograma()
def sairDoPrograma(queroSair):
    resposta = input("Tem a certeza (S/N)? ")
    if (resposta[0] =='s' or resposta[0] =='S'):
        queroSair = True
    return queroSair

# Função escolhaInvalida()
def escolhaInvalida():
    print("Opção inválida!")
    input("Prima qq tecla para continuar ...");
    return

# Função despedida()
def despedida():
    print("Obrigado por ter usado o nosso programa!")
    input("Prima qq tecla para continuar ...")
    return

# Função guardaFicheiro()
def guardaFicheiro( lugares, nomeFicheiro ):
    # 1. Abertura do ficheiro
    fo = open(nomeFicheiro, "w")
    # 2. Escrita de dados
    for cLugar in range(0,lugares.size,1):
        fo.write((str)((int)(lugares[cLugar])))
        fo.write("\n")
    # 3. Fecho do ficheiro
    fo.close()
    print("Dados guardados com sucesso!")
    return

# Função leFicheiro()
def leFicheiro( lugares, nomeFicheiro ):
    try:
        # 1. Abertura do ficheiro
        fo = open(nomeFicheiro, "r")
        # 2. Escrita de dados
        for cLugar in range(0,lugares.size,1):
            lugares[cLugar] = (int)(fo.readline())
            #print("Linha lida: ",lugares[cLugar])
        # 3. Fecho do ficheiro
        fo.close()
        print("Dados lidos com sucesso!")
    finally:
        return
##########################################################
# 3. Função principal
##########################################################
# 3.1 Dados
NUMLUGARES = 7
queroSair = False
escolha='\0'
nFicheiro = "parque.txt"
lugares= np.zeros(NUMLUGARES)

leFicheiro( lugares, nFicheiro)
while (not queroSair):
# 3.2 Algoritmo
    mostraMenu()
    escolha = obtemEscolha(escolha)
    queroSair = processaEscolha(escolha, lugares, nFicheiro, queroSair)
despedida()
