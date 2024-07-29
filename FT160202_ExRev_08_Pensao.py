#####################################################################
# Fazer um programa que gere uma pensão de três andares
# e cinco quartos por andar.
# O programa deve apresentar um menu com as seguintes opções:
#  - Listar quartos;
#  - Reservar quarto;
#  - Ocupar quarto;
#  - Desocupar quarto;
#  - Sair do programa.
# Guarde o programa com o nome “FT0801H_ExRev_08_Pensao.py”.
#####################################################################
#####################################################################
# Solução:
# 1. Quais são as entradas e saída do programa?
#    Entradas: escolha (caractere)
#              numquarto (inteiro)
#    Saída:    estado dos quartos
# 2. Programa em Linguagem Python
#####################################################################
# 0. Bibliotecas
import sys  # Biblioteca entradas/saídas do sistema
import os  # Biblioteca das funções/comandos do sistema operativo
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
# pip3 install numpy
import numpy as np
from array import *

##########################################################
# 1. Dados Globais
##########################################################
LIVRE = 0
RESERVADO = 1
OCUPADO = 2


##########################################################
# 2. Funções
###########################################################
# Função mostraMenu()
def mostraMenu():
    #system('cls')
    print("")
    print("***********************************")
    print("*                                 *")
    print("*       Pensão Pinheiro           *")
    print("*                                 *")
    print("*      1. Listar quartos.         *")
    print("*      2. Reservar quarto.        *")
    print("*      3. Check-in.               *")
    print("*      4. Check-out.              *")
    print("*      5. Sair do programa.       *")
    print("*                                 *")
    print("***********************************")
    print()
    return


# Função obtemEscolha()
def obtemEscolha(escolha):
    resposta = input(" -> Escolha uma opção (1-5): ")
    if (len(resposta) > 0):  # Evita "out of index error"
        escolha = resposta[0]
    else:
        escolha = 0
    return escolha


# Função processaEscolha()
def processaEscolha(escolha, quartos, nFicheiro, queroSair):
    if (escolha == '1'):
        listarQuartos(quartos)
    elif (escolha == '2'):
        reservarQuarto(quartos)
        guardaFicheiro(quartos, nFicheiro)
    elif (escolha == '3'):
        ocuparQuarto(quartos)
        guardaFicheiro(quartos, nFicheiro)
    elif (escolha == '4'):
        libertarQuarto(quartos)
        guardaFicheiro(quartos, nFicheiro)
    elif (escolha == '5'):
        queroSair = sairDoPrograma(queroSair)
    else:
        escolhaInvalida()
    return queroSair


# Função listarQuartos()
def listarQuartos(quartos):
    print("Listagem de quartos:")
    for cAndar in range(0, len(quartos), 1):
        print("Andar ", (cAndar + 1), ": ", end="\n")
        for cQuarto in range(0, len(quartos[0]), 1):
            print(" -> Quarto ", (cQuarto + 1), ": ", end="")
            if (quartos[cAndar][cQuarto] == LIVRE):
                print(" livre.")
            elif (quartos[cAndar][cQuarto] == RESERVADO):
                print(" reservado.")
            else:
                print(" ocupado.")
        input("Prima qq tecla para continuar ...")
    return


# Função reservarQuarto()
def reservarQuarto(quartos):
    try:
        print("Qual é o andar a selecionar ( 1 -",
              len(quartos), ")? ", end="")
        numAndar = int(input())
        try:
            print("Nesse andar, qual é o quarto a reservar ( 1 -",
                  len(quartos[0]), ")? ", end="")
            numQuarto = int(input())

            if (numAndar < 1 or numAndar > len(quartos)):
                print("Andar inválido!")
                print("Andares vão de 1 a ", len(quartos), "!")
            if (numQuarto < 1 or numQuarto > len(quartos[0])):
                print("Quarto inválido!")
                print("Quartos vão de 1 a ", len(quartos[0]), "!")
            elif (quartos[numAndar - 1][numQuarto - 1] == RESERVADO):
                print("Quarto já está reservado!")
            elif (quartos[numAndar - 1][numQuarto - 1] == OCUPADO):
                print("Quarto já está ocupado!")
            else:
                quartos[numAndar - 1][numQuarto - 1] = RESERVADO
                print("Quarto reservado com sucesso!")
            input("Prima qq tecla para continuar ...")
            return
        except Exception as X:
            print("Inseriu um valor inválido!")
            print()
    except Exception as X:
        print("Inseriu um valor inválido!")
        print()

# Função ocuparQuarto()
def ocuparQuarto(quartos):
    try:
        print("Qual é o andar a selecionar ( 1 -",
              len(quartos), ")? ", end="")
        numAndar = int(input())
        try:
            print("Nesse andar, qual é o quarto a ocupar ( 1 -",
                  len(quartos[0]), ")? ", end="")
            numQuarto = int(input())

            if (numAndar < 1 or numAndar > len(quartos)):
                print("Andar inválido!")
                print("Andares vão de 1 a ", len(quartos), "!")
            if (numQuarto < 1 or numQuarto > len(quartos[0])):
                print("Quarto inválido!")
                print("Quartos vão de 1 a ", len(quartos[0]), "!")
            elif (quartos[numAndar - 1][numQuarto - 1] == OCUPADO):
                print("Quarto já está ocupado!")
            else:
                quartos[numAndar - 1][numQuarto - 1] = OCUPADO
                print("Quarto ocupado com sucesso!")
            input("Prima qq tecla para continuar ...")
            return
        except Exception as X:
            print("Inseriu um valor inválido!")
            print()
    except Exception as X:
        print("Inseriu um valor inválido!")
        print()

# Função libertarQuarto()
def libertarQuarto(quartos):
    try:
        print("Qual é o andar a selecionar ( 1 -",
              len(quartos), ")? ", end="")
        numAndar = int(input())
        try:
            print("Nesse andar, qual é o quarto a libertar ( 1 -",
                  len(quartos[0]), ")? ", end="")
            numQuarto = int(input())

            if (numAndar < 1 or numAndar > len(quartos)):
                print("Andar inválido!")
                print("Andares vão de 1 a ", len(quartos), "!")
            if (numQuarto < 1 or numQuarto > len(quartos[0])):
                print("Quarto inválido!")
                print("Quartos vão de 1 a ", len(quartos[0]), "!")
            elif (quartos[numAndar - 1][numQuarto - 1] == LIVRE):
                print("Quarto já está libertado!")
            else:
                quartos[numAndar - 1][numQuarto - 1] = LIVRE
                print("Quarto libertado com sucesso!")
            input("Prima qq tecla para continuar ...")
            return
        except Exception as X:
            print("Inseriu um valor inválido!")
            print()
    except Exception as X:
        print("Inseriu um valor inválido!")
        print()


# Função sairDoPrograma()
def sairDoPrograma(queroSair):
    try:
        resposta = input("Tem a certeza (S/N)? ")
        if (resposta[0] == 's' or resposta[0] == 'S'):
            queroSair = True
        return queroSair
    except Exception as X:
        print("Inseriu um valor inválido!")
        print()

# Função escolhaInvalida()
def escolhaInvalida():
    print("Opção inválida!")
    input("Prima qq tecla para continuar ...")
    return


# Função despedida()
def despedida():
    print("Obrigado por ter usado o nosso programa!")
    input("Prima qq tecla para continuar ...")
    return

#Funçoes dos ficheiros -----------------------------------------
def guardaFicheiro(quartos, nomeFicheiro):
    # 1. Abertura do ficheiro
    fo = open(nomeFicheiro, "w")
    # 2. Escrita de dados
    for cLinha in range(0, len(quartos), 1):
        for cColuna in range(0, len(quartos[0]), 1):
            fo.write((str)((int)(quartos[cLinha][cColuna])))
            fo.write("\n")
    # 3. Fecho do ficheiro
    fo.close()
    print("Dados guardados com sucesso!")
    return


# Função leFicheiro()
def leFicheiro(quartos, nomeFicheiro):
    try:
        # 1. Abertura do ficheiro
        fo = open(nomeFicheiro, "r")
        # 2. Escrita de dados
        for cLinha in range(0, len(quartos), 1):
            for cColuna in range(0, len(quartos[0]), 1):
                quartos[cLinha][cColuna] = (int)(fo.readline())
        # 3. Fecho do ficheiro
        fo.close()
        print("Dados lidos com sucesso!")
    finally:
        return

##########################################################
# 3. Função principal
##########################################################
# 3.1 Dados
NUMANDARES = 3
NUMQUARTOSPORANDAR = 5
queroSair = False
escolha = '\0'

quartos = [[LIVRE
            for i in range(NUMQUARTOSPORANDAR)]
           for j in range(NUMANDARES)]

nFicheiro = "quartos.txt"
leFicheiro(quartos, nFicheiro)

# 3.2 Algoritmo
while (not queroSair):
    mostraMenu()
    escolha = obtemEscolha(escolha)
    queroSair = processaEscolha(escolha, quartos, nFicheiro, queroSair)
despedida()