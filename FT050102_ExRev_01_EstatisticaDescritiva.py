import numpy as np
from time import sleep
import statistics
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import scipy
from pathlib import Path

class Aluno:

    def __init__(self, aluno="", classificacao=0):
        self.__nome_aluno = aluno
        self.__classificacao = classificacao

    # 2.2 Funções Setters
    def set_nomeAluno(self, x):
        self.__nome_aluno = x

    def set_classificacao(self, x):
        self.__classificacao = x

    # 2.3 Funções Getters
    def get_nomeAluno(self):
        return self.__nome_aluno

    def get_classificacao(self):
        return self.__classificacao

    # 2.4 Funções para deletar os atributos
    def del_nomeAluno(self):
        del self.__nome_aluno
        
    def del_classificacao(self):
        del self.__classificacao

    def delTudoE(self):
        print()
        self.del_nomeAluno()
        self.del_classificacao()

    # 2.5 Funções de leitura
    def le_nomeAluno(self):
        print("Qual é o nome da/o aluno?", end=" ")
        self.set_nomeAluno(input())

    def le_classificacao(self):
        print("Qual é a nota da/o aluno?", end=" ")
        self.set_classificacao(int(input()))

    def leTudoE(self):
        print()
        self.le_nomeAluno()
        self.le_classificacao()

    # 2.6 Funções de Apresentação
    # Listagem dos atributos do objeto
    def __str__(self):
        return f"{self.get_nomeAluno()}({self.get_classificacao()})"

    def mostra_nomeAluno(self):
        print("Aluno:", self.get_nomeAluno(), " | ", end="")

    def mostra_classificacao(self):
        print("Nota:", self.get_classificacao(), ".")

    def mostraTudoE(self):
        print()
        self.mostra_nomeAluno()
        self.mostra_classificacao()


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
        "*      3. Listar notas                     *",
        "*      4. Apresentar Graficos               *",
        "*      5. Apresentar Medidas  - Central     *",
        "*      6. Apresentar Medidas  - Dispersão   *",
        "*      7. Apagar Notas                     *",
        "*      8. Sair do programa.                 *"
    ]
    return menu

# 1.03  Função do ciclo principal
def cicloPrincipal(notas, titulo, menu):
    queroSair = False
    escolha = '\0'
    while (not queroSair):
        mostraMenu(titulo, menu)
        escolha = obtemEscolha(escolha, len(menu))
        queroSair = processaEscolha(escolha, notas, queroSair)
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
        escolha, notas, queroSair):

    match (escolha):
        case '1':
            inserirAlunoCSV(notas)
            guardaFicheiro(notas, nomeFicheiro)
        case '2':
            inserirAluno(notas)
            guardaFicheiro(notas, nomeFicheiro)
        case '3':
            listarNotas(notas)
        case '4':
            graficos(notas)
        case '5':
            medidaCentral(notas)
        case '6':
            medidaDispersao(notas)      
        case '7':
            apagarNotas(notas)
            guardaFicheiro(notas, nomeFicheiro)
        case '8':
            queroSair = sairDoProgram(queroSair)
        case _:
            opcaoInvalida()
    return queroSair



#escolha 1 - Inserir Aluno a partir de CSV
def inserirAlunoCSV(notas):
    try:
        print("Insira o nome do seu arquivo CSV:")
        nFicheiro = input()
        caminho_arquivo = Path(r"D:\FPY\UFCD10793_CESAEDataA", nFicheiro + ".csv")
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                campos = linha.strip().split(';')
                aluno = Aluno(campos[0], int(campos[1]))
                notas.append(aluno)
        print("Arquivo CSV lido com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado! Por favor, forneça um caminho válido.")
    except Exception as e:
        print("Ocorreu um erro:", e)


#escolha 2 - Inserir Aluno
def inserirAluno(notas):
    try:
        print()
        print("Insira as informações do aluno:")
        aluno = Aluno()
        aluno.leTudoE()
        if aluno.get_classificacao() < 0:
            print("Inseriu valores negativos!")
        else:
            notas.append(aluno)
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
                return  inserirAluno(notas)
            else:
                return
        return  

#escolha 3 - Listar notas
def listarNotas(notas):
    if not notas:
        print("Sem Notas!")
    else:
        print()
        for aluno in notas:
            aluno.mostraTudoE()
    return

#escolha 4 - mostrar graficos, histogramas, etc
def graficos(notas):
    if not notas:
        print("Não há notas para gerar histogramas.")
        return
    else:
        notas_alunos = [aluno.get_classificacao() for aluno in notas]

        # Histograma de Frequência Absoluta
        plt.figure(figsize=(8, 6))
        plt.hist(notas_alunos, bins=np.arange(min(notas_alunos), max(notas_alunos) + 2, 1), edgecolor='black')
        plt.title('Histograma - Frequência Absoluta')
        plt.xlabel('Nota')
        plt.ylabel('Frequência')
        plt.show()

        # Histograma de Frequência Absoluta Acumulada
        plt.figure(figsize=(8, 6))
        plt.hist(notas_alunos, bins=np.arange(min(notas_alunos), max(notas_alunos) + 2, 1),
                cumulative=True, edgecolor='black')
        plt.title('Histograma - Frequência Absoluta Acumulada')
        plt.xlabel('Nota')
        plt.ylabel('Frequência Acumulada')
        plt.show()
        
        # Histograma de Frequência Relativa
        plt.figure(figsize=(8, 6))
        plt.hist(notas_alunos, bins=np.arange(min(notas_alunos), max(notas_alunos) + 2, 1),
                density=True, edgecolor='black')
        plt.title('Histograma - Frequência Relativa')
        plt.xlabel('Nota')
        plt.ylabel('Densnota')
        plt.show()

        # Histograma de Frequência Relativa Acumulada
        plt.figure(figsize=(8, 6))
        plt.hist(notas_alunos, bins=np.arange(min(notas_alunos), max(notas_alunos) + 2, 1),
                cumulative=True, density=True, edgecolor='black')
        plt.title('Histograma - Frequência Relativa Acumulada')
        plt.xlabel('Nota')
        plt.ylabel('Frequência Acumulada')
        plt.show()

        # Histograma de Frequência Relativa (%)
        plt.figure(figsize=(8, 6))
        plt.hist(notas_alunos, bins=np.arange(min(notas_alunos), max(notas_alunos) + 2, 1),
                weights=np.ones(len(notas_alunos)) / len(notas_alunos) * 100, edgecolor='black')
        plt.title('Histograma - Frequência Relativa (%)')
        plt.xlabel('Nota')
        plt.ylabel('Frequência Relativa (%)')
        plt.show()

        # Histograma de Frequência Relativa Acumulada (%)
        plt.figure(figsize=(8, 6))
        plt.hist(notas_alunos, bins=np.arange(min(notas_alunos), max(notas_alunos) + 2, 1),
                cumulative=True, weights=np.ones(len(notas_alunos)) / len(notas_alunos) * 100, edgecolor='black')
        plt.title('Histograma - Frequência Relativa Acumulada (%)')
        plt.xlabel('Nota')
        plt.ylabel('Frequência Relativa Acumulada (%)')
        plt.show()
    return


#escolha 5 - medidas centrais
def medidaCentral(notas):
    if not notas:
        print("Sem notas!")
    else:
        notas_alunos = [aluno.get_classificacao() for aluno in notas]
        
        media = statistics.mean(notas_alunos)
        print("-> A média aritemética das notas é:", round(media, 2))
        media_harmonica = statistics.fmean(notas_alunos)
        print("-> A média harmônica das notas é:", round(media_harmonica, 2))
        media_geo = statistics.geometric_mean(notas_alunos)
        print("-> A média geométrica das notas é:", round(media_geo, 2))        
        mediana = statistics.median(notas_alunos)
        print("-> A mediana das notas é:", mediana)
        moda = statistics.multimode(notas_alunos)
        print("-> A moda das notas é:", moda)    
        
    return


#escolha 6 - medidas dispersão
def medidaDispersao(notas):
    if not notas:
        print("Sem notas!")
    else:
        notas_alunos = [aluno.get_classificacao() for aluno in notas]

        variancia = statistics.variance(notas_alunos)
        print("-> A variância das notas é:", round(variancia, 2))
        desvio_padrao = statistics.stdev(notas_alunos)
        print("-> O desvio padrão das notas é:", round(desvio_padrao, 2))
        np_notas = np.array(notas_alunos)
        skew = scipy.stats.skew(np_notas, bias=False)
        print("-> Skewness de notas:", round(skew, 4))
        percentis = np.percentile(notas_alunos, [25, 50, 75])
        print("-> Os percentis das notas são (25%, 50%, 75%):", [round(p, 2) for p in percentis])
        quartis = np.quantile(notas_alunos, [0.25, 0.5, 0.75])
        print("-> Os quartis das notas são (Q1, Q2, Q3):", [round(q, 2) for q in quartis])
        gamas = np.ptp(notas_alunos)
        print("-> As gamas das notas é:", round(gamas, 2))
        maximo = max(notas_alunos)
        print("-> O valor máximo das notas é:", maximo)
        minimo = min(notas_alunos)
        print("-> O valor mínimo das notas é:", minimo)
    return

#escolha 7 - apagar notas
def apagarNotas(notas):
    if not notas:
        print("Não existem alunos!")
    else:
        try:
            print()
            certeza = input("Tem a certeza que deseja apagar todas as notas dos alunos (S/N)? ")
            if (certeza[0] == 's' or certeza[0] == 'S'):
                del notas[0:len(notas)]
                print("Todas as notas foram apagadas!")
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
def guardaFicheiro(notas, nomeFicheiro):
    try:
        with open(nomeFicheiro, "w") as fo:
            for aluno in notas:
                fo.write(str(aluno.get_nomeAluno()) + "\n")
                fo.write(str(aluno.get_classificacao()) + "\n")
        print("Dados guardados com sucesso!")
    except Exception as X:
        print("Erro ao guardar os dados no arquivo:", X)

def leFicheiro(notas, nomeFicheiro):
    try:
        with open(nomeFicheiro, "r") as fo:
            while True:
                nome_aluno = fo.readline().strip()
                if not nome_aluno:  
                    break
                classificacao_str = fo.readline().strip()
                classificacao = int(classificacao_str)
                aluno = Aluno(nome_aluno, classificacao)
                notas.append(aluno)
        print("Dados lidos com sucesso!")
    except Exception as e:
        print("Erro ao ler os dados do arquivo:", e)

#FIM DE FUNÇOES------------------------------------------------------


notas = []
NUMOPCOES = 7
escolha = 0
nFicheiro = ""
nomeFicheiro = "notas.txt"
titulo =""
menu = ["" for cOpcao in range(0,NUMOPCOES,1)]
queroSair = False


leFicheiro(notas, nomeFicheiro)
titulo = defineTitulo(titulo)
menu = inicializaMenu(menu)
cicloPrincipal(notas,titulo, menu)
despedida()
