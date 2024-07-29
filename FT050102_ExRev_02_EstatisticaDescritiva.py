from os import system, name
import numpy as np
import time
from time import sleep
import math
import statistics
#pip install matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
#pip install scipy
import scipy
from scipy import stats
import csv
from pathlib import Path

class Aluno:

    def __init__(self, aluno="", anos=0):
        self.__nome_aluno = aluno
        self.__anos = anos

    # 2.2 Funções Setters
    def set_nomeAluno(self, x):
        self.__nome_aluno = x

    def set_anos(self, x):
        self.__anos = x

    # 2.3 Funções Getters
    def get_nomeAluno(self):
        return self.__nome_aluno

    def get_anos(self):
        return self.__anos

    # 2.4 Funções para deletar os atributos
    def del_nomeAluno(self):
        del self.__nome_aluno
        
    def del_anos(self):
        del self.__anos

    def delTudoE(self):
        print()
        self.del_nomeAluno()
        self.del_anos()

    # 2.5 Funções de leitura
    def le_nomeAluno(self):
        print("Qual é o nome da/o aluno?", end=" ")
        self.set_nomeAluno(input())

    def le_anos(self):
        print("Qual é a idade da/o aluno?", end=" ")
        self.set_anos(int(input()))

    def leTudoE(self):
        print()
        self.le_nomeAluno()
        self.le_anos()

    # 2.6 Funções de Apresentação
    # Listagem dos atributos do objeto
    def __str__(self):
        return f"{self.get_nomeAluno()}({self.get_anos()})"

    def mostra_nomeAluno(self):
        print("Aluno:", self.get_nomeAluno(), " | ", end="")

    def mostra_anos(self):
        print("Idade:", self.get_anos(), ".")

    def mostraTudoE(self):
        print()
        self.mostra_nomeAluno()
        self.mostra_anos()


    # 0. Descrição
    "Classe de Excepção Personalizada."

    # 2. Funções
    def mensagemErro(self):
        print('Inseriu um valor negativo!')


#FUNÇÕES------------------------------------------------

def defineTitulo(titulo):
    titulo = "*         Estatísticas                      *"
    return titulo 

def inicializaMenu(menu):
    menu = [
        "*      1. Ler -  CSV                        *",
        "*      2. Inserir - programa                *",
        "*      3. Listar idades                     *",
        "*      4. Apresentar Graficos               *",
        "*      5. Apresentar Medidas  - Central     *",
        "*      6. Apresentar Medidas  - Dispersão   *",
        "*      7. Apagar Idades                     *",
        "*      8. Sair do programa.                 *"
    ]
    return menu

# 1.03  Função do ciclo principal
def cicloPrincipal(idades, titulo, menu):
    queroSair = False
    escolha = '\0'
    while (not queroSair):
        mostraMenu(titulo, menu)
        escolha = obtemEscolha(escolha, len(menu))
        queroSair = processaEscolha(escolha, idades, queroSair)
    return

#     Função "mostraMenu()"
def mostraMenu(titulo, menu):
    print("")
    print("*********************************************")
    print("*                                           *")
    print(titulo)
    print("*                                           *")
    for cOpcao in range(0,len(menu),1):
        print(menu[cOpcao])
    print("*                                           *")
    print("*********************************************")
    print()
    return

#     Função "obtemEscolha()"
def obtemEscolha(escolha, numOpcoes):
    print(" -> Escolha uma opção (1-",end="")
    print(numOpcoes,end="")
    print("): ",end="")
    resposta = input()
    if (len(resposta) > 0):   
       escolha = resposta[0]
    else:
       escolha = 0
    return escolha

#     Função "processaEscolha()"
def processaEscolha(
        escolha, idades, queroSair):

    match (escolha):
        case '1':
            inserirAlunoCSV(idades)
            guardaFicheiro(idades, nomeFicheiro)
        case '2':
            inserirAluno(idades)
            guardaFicheiro(idades, nomeFicheiro)
        case '3':
            listarIdades(idades)
        case '4':
            graficos(idades)
        case '5':
            medidaCentral(idades)
        case '6':
            medidaDispersao(idades)      
        case '7':
            apagarIdades(idades)
            guardaFicheiro(idades, nomeFicheiro)
        case '8':
            queroSair = sairDoProgram(queroSair)
        case _:
            opcaoInvalida()
    return queroSair



#escolha 1 - Inserir Aluno a partir de CSV
def inserirAlunoCSV(idades):
    try:
        print("Insira o nome do seu arquivo CSV:")
        nFicheiro = input()
        caminho_arquivo = Path(r"D:\FPY\UFCD10793_CESAEDataA", nFicheiro + ".csv")
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                campos = linha.strip().split(';')
                aluno = Aluno(campos[0], int(campos[1]))
                idades.append(aluno)
        print("Arquivo CSV lido com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado! Por favor, forneça um caminho válido.")
    except Exception as e:
        print("Ocorreu um erro:", e)


#escolha 2 - Inserir Aluno
def inserirAluno(idades):
    try:
        print()
        print("Insira as informações do aluno:")
        aluno = Aluno()
        aluno.leTudoE()
        if aluno.get_anos() < 0:
            print("Inseriu valores negativos!")
        else:
            idades.append(aluno)
    except ValueError as v: 
            print("Valores inseridos são inválidos!")
    except Exception as X:
        print(X)
        print("Valores inseridos são inválidos!")
    finally:
        print()
        resposta = input("Quer inserir outra/o Aluno (S/N)? ")
        if (len(resposta) > 0):
            if (resposta[0] == 's' or resposta[0] == 'S'):
                return  inserirAluno(idades)
            else:
                return
        return  

#escolha 3 - Listar idades
def listarIdades(idades):
    if not idades:
        print("Sem Idades!")
    else:
        print()
        for aluno in idades:
            aluno.mostraTudoE()
    return

#escolha 4 - mostrar graficos, histogramas, etc
def graficos(idades):
    if not idades:
        print("Não há idades para gerar histogramas.")
        return
    else:
        idades_alunos = [aluno.get_anos() for aluno in idades]

        # Histograma de Frequência Absoluta
        plt.figure(figsize=(8, 6))
        plt.hist(idades_alunos, bins=np.arange(min(idades_alunos), max(idades_alunos) + 2, 1), edgecolor='black')
        plt.title('Histograma - Frequência Absoluta')
        plt.xlabel('Idade')
        plt.ylabel('Frequência')
        plt.show()

        # Histograma de Frequência Absoluta Acumulada
        plt.figure(figsize=(8, 6))
        plt.hist(idades_alunos, bins=np.arange(min(idades_alunos), max(idades_alunos) + 2, 1),
                cumulative=True, edgecolor='black')
        plt.title('Histograma - Frequência Absoluta Acumulada')
        plt.xlabel('Idade')
        plt.ylabel('Frequência Acumulada')
        plt.show()
        
        # Histograma de Frequência Relativa
        plt.figure(figsize=(8, 6))
        plt.hist(idades_alunos, bins=np.arange(min(idades_alunos), max(idades_alunos) + 2, 1),
                density=True, edgecolor='black')
        plt.title('Histograma - Frequência Relativa')
        plt.xlabel('Idade')
        plt.ylabel('Densidade')
        plt.show()

        # Histograma de Frequência Relativa Acumulada
        plt.figure(figsize=(8, 6))
        plt.hist(idades_alunos, bins=np.arange(min(idades_alunos), max(idades_alunos) + 2, 1),
                cumulative=True, density=True, edgecolor='black')
        plt.title('Histograma - Frequência Relativa Acumulada')
        plt.xlabel('Idade')
        plt.ylabel('Frequência Acumulada')
        plt.show()

        # Histograma de Frequência Relativa (%)
        plt.figure(figsize=(8, 6))
        plt.hist(idades_alunos, bins=np.arange(min(idades_alunos), max(idades_alunos) + 2, 1),
                weights=np.ones(len(idades_alunos)) / len(idades_alunos) * 100, edgecolor='black')
        plt.title('Histograma - Frequência Relativa (%)')
        plt.xlabel('Idade')
        plt.ylabel('Frequência Relativa (%)')
        plt.show()

        # Histograma de Frequência Relativa Acumulada (%)
        plt.figure(figsize=(8, 6))
        plt.hist(idades_alunos, bins=np.arange(min(idades_alunos), max(idades_alunos) + 2, 1),
                cumulative=True, weights=np.ones(len(idades_alunos)) / len(idades_alunos) * 100, edgecolor='black')
        plt.title('Histograma - Frequência Relativa Acumulada (%)')
        plt.xlabel('Idade')
        plt.ylabel('Frequência Relativa Acumulada (%)')
        plt.show()
    return


#escolha 5 - medidas centrais
def medidaCentral(idades):
    if not idades:
        print("Sem idades!")
    else:
        idades_alunos = [aluno.get_anos() for aluno in idades]
        
        media = statistics.mean(idades_alunos)
        print("-> A média aritemética das idades é:", round(media, 2))
        media_harmonica = statistics.fmean(idades_alunos)
        print("-> A média harmônica das idades é:", round(media_harmonica, 2))
        media_geo = statistics.geometric_mean(idades_alunos)
        print("-> A média geométrica das idades é:", round(media_geo, 2))        
        mediana = statistics.median(idades_alunos)
        print("-> A mediana das idades é:", mediana)
        moda = statistics.multimode(idades_alunos)
        print("-> A moda das idades é:", moda)    
        
    return


#escolha 6 - medidas dispersão
def medidaDispersao(idades):
    if not idades:
        print("Sem idades!")
    else:
        idades_alunos = [aluno.get_anos() for aluno in idades]

        variancia = statistics.variance(idades_alunos)
        print("-> A variância das idades é:", round(variancia, 2))
        desvio_padrao = statistics.stdev(idades_alunos)
        print("-> O desvio padrão das idades é:", round(desvio_padrao, 2))
        np_idades = np.array(idades_alunos)
        skew = scipy.stats.skew(np_idades, bias=False)
        print("-> Skewness de idades:", round(skew, 4))
        percentis = np.percentile(idades_alunos, [25, 50, 75])
        print("-> Os percentis das idades são (25%, 50%, 75%):", [round(p, 2) for p in percentis])
        quartis = np.quantile(idades_alunos, [0.25, 0.5, 0.75])
        print("-> Os quartis das idades são (Q1, Q2, Q3):", [round(q, 2) for q in quartis])
        gamas = np.ptp(idades_alunos)
        print("-> As gamas das idades é:", round(gamas, 2))
        maximo = max(idades_alunos)
        print("-> O valor máximo das idades é:", maximo)
        minimo = min(idades_alunos)
        print("-> O valor mínimo das idades é:", minimo)
    return

#escolha 7 - apagar idades
def apagarIdades(idades):
    if not idades:
        print("Não existem alunos!")
    else:
        try:
            print()
            certeza = input("Tem a certeza que deseja apagar todas as idades dos alunos (S/N)? ")
            if (certeza[0] == 's' or certeza[0] == 'S'):
                del idades[0:len(idades)]
                print("Todas as idades foram apagadas!")
            else:
                print("Operação cancelada.")
                return
        except Exception as X:
            print("Inseriu um valor inválido!")   
    return 

#escolha 8 - sair do programa
def sairDoProgram(queroSair):
    resposta = input("Tem a certeza (S/N)? ")
    if (len(resposta) > 0):
        if (resposta[0] == 's' or resposta[0] == 'S'):
            queroSair = True
        elif (resposta[0] == 'n' or resposta[0] == 'N'):
            return
        else:
            print("Opção Inválida.")
            return
    return queroSair


# escolha "else"
def opcaoInvalida():
    print("Opção inválida!")
    input("Prima qq tecla para continuar ...")
    return


#despedida para sair
def despedida():
    print("Obrigado por ter usado o nosso programa!")
    input("Prima qq tecla para continuar ...")
    print()
    return

# Funções FICHEIRO------------------------------
def guardaFicheiro(idades, nomeFicheiro):
    try:
        with open(nomeFicheiro, "w") as fo:
            for aluno in idades:
                fo.write(str(aluno.get_nomeAluno()) + "\n")
                fo.write(str(aluno.get_anos()) + "\n")
        print("Dados guardados com sucesso!")
    except Exception as X:
        print("Erro ao guardar os dados no arquivo:", X)

def leFicheiro(idades, nomeFicheiro):
    try:
        with open(nomeFicheiro, "r") as fo:
            while True:
                nome_aluno = fo.readline().strip()
                if not nome_aluno:  
                    break
                anos_str = fo.readline().strip()
                anos = int(anos_str)
                aluno = Aluno(nome_aluno, anos)
                idades.append(aluno)
        print("Dados lidos com sucesso!")
    except Exception as e:
        print("Erro ao ler os dados do arquivo:", e)

#FIM DE FUNÇOES------------------------------------------------------


idades = []
NUMOPCOES = 7
escolha = 0
nFicheiro = ""
nomeFicheiro = "idades.txt"
titulo =""
menu = ["" for cOpcao in range(0,NUMOPCOES,1)]
queroSair = False


leFicheiro(idades, nomeFicheiro)
titulo = defineTitulo(titulo)
menu = inicializaMenu(menu)
cicloPrincipal(idades,titulo, menu)
despedida()
