
import numpy as np
import array

#FUNÇÕES

def defineTitulo(titulo):
    titulo = "*       Estádio Pinheiro          *"
    return titulo

def inicializaMenu(menu):
    menu = [
        "*      1. Listar lugar            *",
        "*      2. Reservar Lugar          *",
        "*      3. Ocupar Lugar            *",
        "*      4. Fim do Jogo             *",
        "*      5. Sair do programa.       *"
    ]
    return menu

# 1.03  Função do ciclo principal
def cicloPrincipal(lugar, titulo, menu):
    queroSair = False
    escolha = '\0'
    while (not queroSair):
        mostraMenu(titulo, menu)
        escolha = obtemEscolha(escolha, len(menu))
        queroSair = processaEscolha(escolha, lugar, queroSair)
    return

#     Função "mostraMenu()"
def mostraMenu(titulo, menu):
    print("")
    print("***********************************")
    print("*                                 *")
    print(titulo)
    print("*                                 *")
    for cOpcao in range(0,len(menu),1):
        print(menu[cOpcao])
    print("*                                 *")
    print("***********************************")
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
def processaEscolha(escolha, lugar, queroSair):

    match (escolha):
        case '1':
            listarlugar(lugar,ESTADIO,LIVRE,RESERVADO)
        case '2':
            reservarLugar(lugar,NUMLUGARES,ESTADIO,LIVRE,RESERVADO)
            guardaFicheiro(ESTADIO, nomeFicheiro)
        case '3':
            ocuparLugar(lugar,NUMLUGARES,ESTADIO,OCUPADO,RESERVADO)
            guardaFicheiro(ESTADIO, nomeFicheiro)
        case '4':
            terminarJogo(resposta, NUMLUGARES)
            guardaFicheiro(ESTADIO, nomeFicheiro)
        case '5':
            queroSair = sairDoProgram(queroSair)
        case _:
            opcaoInvalida()
    return queroSair

#escolha 1 - Listar lugar
def listarlugar(lugar,ESTADIO,LIVRE,RESERVADO):
    for bancada in range(4):
            print()
            print("Bancada", bancada + 1 ,":")
            for fila in range(6):
                print()
                print(" ->Fila", fila + 1 ,":")    
                for lugar in range(NUMLUGARES):
                    if ESTADIO[bancada, fila, lugar] == LIVRE:
                        estado = "Livre"  
                    elif ESTADIO[bancada, fila, lugar] == RESERVADO:
                        estado = "Reservado"   
                    else: 
                        estado = "Ocupado"
                    print("  ---> Lugar", lugar + 1, ":", estado)
    return

#escolha 2 - reservar lugar
def reservarLugar(lugar,NUMLUGARES,ESTADIO,LIVRE,RESERVADO):
    try:
        print("Qual a bancada que deseja selecionar? 1 -", len(ESTADIO))
        bancada = int(input()) - 1
        try:
            print("Qual a fila que deseja selecionar? 1 - 6")
            fila = int(input()) - 1
            try:
                print("Qual o lugar que deseja reservar? 1 -", NUMLUGARES)
                lugar = int(input()) - 1
                if ESTADIO[bancada, fila, lugar] == LIVRE:
                    print("Lugar reservado com sucesso!")
                    ESTADIO[bancada, fila, lugar] = RESERVADO
                else:
                    print("Este lugar já está ocupado ou reservado.")
                return
            except Exception as X:
                print("Inseriu um valor inválido!")
                print()
        except Exception as X:
            print("Inseriu um valor inválido!")
            print()
    except Exception as X:
        print("Inseriu um valor inválido!")
        print()


#escolha 3 - ocupar lugar
def ocuparLugar (lugar,NUMLUGARES,ESTADIO,OCUPADO,RESERVADO):
    try:
        print("Qual a bancada que deseja selecionar? 1 -", len(ESTADIO))
        bancada = int(input()) - 1
        try:
            print("Qual a fila que deseja selecionar? 1 - 6")
            fila = int(input()) - 1
            try:
                print("Qual o lugar que deseja ocupar? 1 -", NUMLUGARES)
                lugar = int(input()) - 1
                if ESTADIO[bancada, fila, lugar] == RESERVADO:
                    print("Lugar ocupado com sucesso!")
                    ESTADIO[bancada, fila, lugar] = OCUPADO
                elif ESTADIO[bancada, fila, lugar] == OCUPADO:
                    print("Este lugar já se  encontra ocupado.")
                else:
                    print("Lugar ocupado com sucesso!")
                    ESTADIO[bancada, fila, lugar] = OCUPADO
                return
            except Exception as X:
                print("Inseriu um valor inválido!")
                print()
        except Exception as X:
            print("Inseriu um valor inválido!")
            print()
    except Exception as X:
        print("Inseriu um valor inválido!")
        print()

#escolha 4 - Registar Venda

def terminarJogo (resposta,NUMLUGARES):
    resposta = input("Tem a certeza (S/N)? ")
    if (len(resposta) > 0):
        if (resposta[0] == 's' or resposta[0] == 'S'):
            ESTADIO.fill(0) 
            print("Jogo terminado!")
        else:
            print("Operação cancelada.") 
    return

#escolha 5 - sair do programa
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

#Funçoes dos ficheiros -----------------------------------------
def guardaFicheiro(ESTADIO, nomeFicheiro):
    try:
        # 1. Abertura do ficheiro
        fo = open(nomeFicheiro, "w")
        # 2. Escrita de dados
        for bancada in range(len(ESTADIO)):
            for fila in range(len(ESTADIO[0])):
                for lugar in range(len(ESTADIO[0][0])):
                    fo.write(str(ESTADIO[bancada][fila][lugar]) + "\n")
        # 3. Fecho do ficheiro
        fo.close()
        print("Dados guardados com sucesso!")
    except Exception as e:
        print("Erro ao guardar o ficheiro:", e)

def leFicheiro(ESTADIO, nomeFicheiro):
    try:
        fo = open(nomeFicheiro, "r")
        for bancada in range(len(ESTADIO)):
            for fila in range(len(ESTADIO[0])):
                for lugar in range(len(ESTADIO[0][0])):
                    ESTADIO[bancada][fila][lugar] = int(fo.readline().strip())
        fo.close()
        print("Dados lidos com sucesso!")
    except Exception as e:
        print("Erro ao ler o ficheiro:", e)
#FIM DE FUNÇOES--------------------------------------------------

escolha = 0
resposta = 0
numOpcoes = 5
lugar = 0
titulo =""
menu = ["" for cOpcao in range(0,numOpcoes,1)]
LIVRE = 0
OCUPADO = 1
RESERVADO = 2
NUMLUGARES = 7
queroSair = False
ESTADIO = np.zeros((4, 6, NUMLUGARES), dtype=int)
nomeFicheiro = "estadio.txt"
leFicheiro(ESTADIO, nomeFicheiro)

titulo = defineTitulo(titulo)
menu = inicializaMenu(menu)
cicloPrincipal(lugar,titulo,menu)
despedida()



