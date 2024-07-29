import numpy as np

#FUNÇÕES

def defineTitulo(titulo):
    titulo = "*       Projetores Pinheiro       *"
    return titulo

def inicializaMenu(menu):
    menu = [
        "*      1. Lista de Salas          *",
        "*      2. Levantar Projetor       *",
        "*      3. Devolver Projetor       *",
        "*      4. Sair do programa.       *"
    ]
    return menu

# 1.03  Função do ciclo principal
def cicloPrincipal(Projetores, EstadoSala, titulo, menu):
    queroSair = False
    escolha = '\0'
    while (not queroSair):
        mostraMenu(titulo, menu)
        escolha = obtemEscolha(escolha, len(menu))
        queroSair = processaEscolha(escolha, Projetores, EstadoSala, LIVRE, OCUPADO, queroSair)
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
       escolha = '0'
    return escolha

#     Função "processaEscolha()"
def processaEscolha(escolha, Projetores, EstadoSala, LIVRE, OCUPADO, queroSair):
    match escolha:
        case '1':
            listarSalas(EstadoSala, LIVRE)
        case '2':
            levantarProjetor(EstadoSala, Projetores, LIVRE, OCUPADO)
            guardaFicheiro(EstadoSala, nomeFicheiro)
        case '3':
            devolverProjetor(EstadoSala, Projetores, LIVRE, OCUPADO)
            guardaFicheiro(EstadoSala, nomeFicheiro)
        case '4':
            queroSair = sairDoProgram(queroSair)
        case _:
            opcaoInvalida()
    return queroSair

# escolha 1 - listar salas

def listarSalas (EstadoSala, LIVRE):
    for sala in range(1, 11):
        if EstadoSala[sala - 1][0] == LIVRE:
            estado = 'Vazia'
            id_projetor = 'Nenhum'
            print("-> Sala", sala, "Estado:", estado)
        else:
            estado = 'com projetor'
            id_projetor = EstadoSala[sala - 1][1]
            print("-> Sala", sala, "Estado:", estado, "ID do Projetor:", id_projetor)
    return

#escolha 2 - levantar projetores
def levantarProjetor(EstadoSala, Projetores, LIVRE, OCUPADO):
    try:
        sala_levantar = int(input(" -> Digite o número da sala para levantar o projetor: "))
        if EstadoSala[sala_levantar - 1][0] == LIVRE:
            if Projetores:
                projetor_id = Projetores.pop()
                EstadoSala[sala_levantar - 1][0] = OCUPADO
                EstadoSala[sala_levantar - 1][1] = projetor_id
                print("Projetor com ID", projetor_id, "levantado com sucesso para a sala", sala_levantar)
            else:
                print("Não existem projetores disponíveis.")
        else:
            print("Esta sala já tem um projetor.")
        return EstadoSala
    except Exception as e:
        print("Erro ao ler os dados do ficheiro: ", e)

#escolha 3 - devolver projetores
def devolverProjetor(EstadoSala, Projetores, LIVRE, OCUPADO):
    try:
        sala_devolver = int(input(" -> Digite o número da sala para devolver o projetor: "))
        if EstadoSala[sala_devolver - 1][0] == OCUPADO:
            projetor_id = EstadoSala[sala_devolver - 1][1]
            EstadoSala[sala_devolver - 1][0] = LIVRE
            Projetores.append(projetor_id)
            print("Projetor da sala", sala_devolver, "devolvido com sucesso!")
        else:
            print("Não existe um projetor nesta sala.")
        return
    except Exception as e:
        print("Erro ao ler os dados do ficheiro: ", e)

#escolha 4 - sair do programa
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

def guardaFicheiro(EstadoSala, nomeFicheiro):
    try:
        with open(nomeFicheiro, "w") as fo:
            # 2. Escrita de dados
            for cLinha in range(0, len(EstadoSala), 1):
                for cColuna in range(0, len(EstadoSala[0]), 1):
                    fo.write((str)((int)(EstadoSala[cLinha][cColuna])))
                    fo.write("\n")
        print("Dados guardados com sucesso!")
    except Exception as X:
        print("Erro ao guardar os dados no ficheiro: ", X)

def leFicheiro(EstadoSala, nomeFicheiro):
    try:
        with open(nomeFicheiro, "r") as fo:
            for cLinha in range(len(EstadoSala)):
                for cColuna in range(len(EstadoSala[0])):
                    EstadoSala[cLinha][cColuna] = int(fo.readline().strip())
        print("Dados lidos com sucesso!")
    except Exception as e:
        print("Erro ao ler os dados do ficheiro: ", e)

#FIM DE FUNÇOES------------------------------------------------------


# 1. Dados
EstadoSala = np.zeros((10, 2))
Projetores = [205,206,208,204]
nomeFicheiro = "videoprojetor.txt"
NUMOPCOES = 4
LIVRE = 0
OCUPADO = 1
titulo =""
menu = ["" for cOpcao in range(0,NUMOPCOES,1)]
queroSair = False
escolha = '\0'

leFicheiro(EstadoSala, nomeFicheiro)
titulo = defineTitulo(titulo)
menu = inicializaMenu(menu)
cicloPrincipal(Projetores, EstadoSala, titulo, menu)
despedida()
