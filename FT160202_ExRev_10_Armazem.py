class Produto:

    def __init__(self, produto="", preco=0.0, quantidade=0):
        self.__nome_produto = produto
        self.__preco = preco
        self.__quantidade = quantidade

    # 2.2 Funções Setters
    def set_nomeProduto(self, x):
        self.__nome_produto = x

    def set_preco(self, x):
        self.__preco = x

    def set_quantidade(self, x):
        self.__quantidade = x

    # 2.3 Funções Getters
    def get_nomeProduto(self):
        return self.__nome_produto

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    # 2.4 Funções para deletar os atributos
    def del_nomeProduto(self):
        del self.__nome_produto

    def del_preco(self):
        del self.__preco

    def del_quantidade(self):
        del self.__quantidade

    def delTudoE(self):
        print()
        self.del_nomeProduto()
        self.del_preco()
        self.del_quantidade()

    # 2.5 Funções de leitura
    def le_nomeProduto(self):
        print("Qual é o nome da produto?", end=" ")
        self.set_nomeProduto(input())

    def le_preco(self):
        print("Qual é o preço do produto?", end=" ")
        self.set_preco(float(input()))

    def le_quantidade(self):
        print("Qual é a quantidade do produto?", end=" ")
        self.set_quantidade(int(input()))

    def leTudoE(self):
        print()
        self.le_nomeProduto()
        self.le_preco()
        self.le_quantidade()

    # 2.6 Funções de Apresentação
    # Listagem dos atributos do objeto
    def __str__(self):
        return f"{self.get_nomeProduto()}({self.get_preco()}€)({self.get_quantidade()})"

    def mostra_nomeProduto(self):
        print("Produto:", self.get_nomeProduto(), " | ", end="")

    def mostra_preco(self):
        print("Preço:", self.get_preco(), "€ | ", end="")

    def mostra_quantidade(self):
        print("Stock:", self.get_quantidade(), ".")

    def mostraTudoE(self):
        print()
        self.mostra_nomeProduto()
        self.mostra_preco()
        self.mostra_quantidade()


    # 0. Descrição
    "Classe de Excepção Personalizada."

    # 2. Funções
    def mensagemErro(self):
        print('Inseriu um valor negativo!')

#FUNÇÕES------------------------------------------------

def defineTitulo(titulo):
    titulo = "*       Armazem Pinheiro          *"
    return titulo

def inicializaMenu(menu):
    menu = [
        "*      1. Listar produtos         *",
        "*      2. Inserir produto         *",
        "*      3. Alterar preço           *",
        "*      4. Registar Venda          *",
        "*      5. Registar Reposição      *",
        "*      6. Apagar produtos         *",
        "*      7. Sair do programa.       *"
    ]
    return menu

# 1.03  Função do ciclo principal
def cicloPrincipal(produtos, titulo, menu):
    queroSair = False
    escolha = '\0'
    while (not queroSair):
        mostraMenu(titulo, menu)
        escolha = obtemEscolha(escolha, len(menu))
        queroSair = processaEscolha(escolha, produtos, queroSair)
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
def processaEscolha(
        escolha, produtos, queroSair):

    match (escolha):
        case '1':
            listarProdutos(produtos)
        case '2':
            inserirProduto(produtos)
            guardaFicheiro(produtos, nFicheiro)
        case '3':
            alterarPreco(produtos, produto)
            guardaFicheiro(produtos, nFicheiro)
        case '4':
            registarVenda(produtos)
            guardaFicheiro(produtos, nFicheiro)
        case '5':
            registarReposicao(produtos)
            guardaFicheiro(produtos, nFicheiro)
        case '6':
            apagarProdutos(produtos)
            guardaFicheiro(produtos, nFicheiro)
        case '7':
            queroSair = sairDoProgram(queroSair)
        case _:
            opcaoInvalida()
    return queroSair

#escolha 1 - Listar produtos
def listarProdutos(produtos):
    if not produtos:
        print("Sem Produtos!")
    else:
        print()
        for produto in produtos:
            produto.mostraTudoE()
    return

#escolha 2 - Inserir Produto
def inserirProduto(produtos):
    try:
        print()
        print("Insira as informações do produto:")
        produto = Produto()
        produto.leTudoE()
        if produto.get_quantidade() < 0 or produto.get_preco() < 0:
            print("Inseriu valores negativos!")
        else:
            produtos.append(produto)
    except ValueError as v:
        if "," in str(v):
            print("Inseriu uma vírgula (,) em vez de ponto (.)!")    
        else:
            print("Valores inseridos são inválidos!")
    except Exception as X:
        print(X)
        print("Valores inseridos são inválidos!")
    finally:
        print()
        resposta = input("Quer inserir outra Produto (S/N)? ")
        if (len(resposta) > 0):
            if (resposta[0] == 's' or resposta[0] == 'S'):
                return  inserirProduto(produtos)
            else:
                return
        return  

#escolha 3 - Alterar Preco
def alterarPreco (produtos, produto):
    print()
    if not produtos:
        print("Não existem produtos no armazém!")
    else:
        produto = produtos
        for i, produto in enumerate(produtos, start=1):
            print(f"{i}. {produto.get_nomeProduto()}")
        try:
            print()
            resposta = int(input("Qual é o número do produto que deseja alterar? "))
            if resposta < 1 or resposta > len(produtos):
                print("Número de produto inválido.")
                return
            else:
                novo_preco = float(input("Digite o novo preço: "))
                if  novo_preco < 0.01:
                    print("Inseriu um preço igual ou inferior a 0!")
                else:
                    produtos[resposta - 1].set_preco(novo_preco)
                    print("Preço atualizado com sucesso!")
        except ValueError as v:
            if "," in str(v):
                print("Inseriu uma vírgula (,) em vez de ponto (.)!")    
            else:
                print("Valores inseridos são inválidos!")
        except Exception as X:
            print(X)
            print("Valores inseridos são inválidos!")
        finally:
            print()
            resposta = input("Quer alterar outro preço (S/N)? ")
            if (len(resposta) > 0):
                if (resposta[0] == 's' or resposta[0] == 'S'):
                    return alterarPreco(produtos, produtos)
                else:
                    return 
            return
        
#escolha 4 - Registar Venda
def registarVenda(produtos):
    if not produtos:
        print("Não existem produtos no armazém!")
    else:
        for i, produto in enumerate(produtos, start=1):
            print(f"{i}. {produto.get_nomeProduto()}")
        try:
            print()
            resposta = int(input("Quer registar a venda de qual produto (coloque o número)? ")) - 1
            if resposta < 0 or resposta >= len(produtos):
                print("Opção Inválida!")
            elif (str)(produtos[resposta].get_quantidade()) == "Sem stock!":
                print("Não existe stock para venda.")
            else:
                try:
                    print()
                    quantidade_reposta = int(input("Quantidade vendida: "))
                    if  int(quantidade_reposta) < 1:    
                        print("Inseriu um valor inferior a 1!")
                        print()
                    else:
                        produto = produtos[resposta] 
                        quantidade_disponivel = (produto.get_quantidade())
                        if quantidade_reposta <= quantidade_disponivel:
                            nova_quantidade = quantidade_disponivel - quantidade_reposta
                            produto.set_quantidade(nova_quantidade)
                            novo =(produtos[resposta].get_quantidade())
                            print("Venda registrada com sucesso!")
                            if novo  == 0:
                                produtos[resposta].set_quantidade("Sem stock!")
                            else:
                                return
                        else:
                            print("Quantidade excede stock atual!")
                except Exception as X:
                    print("Inseriu  um valor inválido!")
        except Exception as X:
            print("Inseriu um valor inválido!")
            print()
        finally:
            print()
            resposta = input("Quer registrar outra venda (S/N)? ")
            if (len(resposta) > 0):
                if (resposta[0] == 's' or resposta[0] == 'S'):
                    return registarVenda(produtos)   
                else:
                    return
                    
#escolha 5 - registar reposicao
def registarReposicao(produtos):
    if not produtos:
        print("Não existem produtos no armazém!")
    else:
        for i, produto in enumerate(produtos, start=1):
            print(f"{i}. {produto.get_nomeProduto()}")
        try:
            print()
            resposta = int(input("Quer efetuar a reposição de qual produto (coloque o número)? ")) - 1
            if resposta < 0 or resposta >= len(produtos):
                print("Opção Inválida!")
            elif resposta > 0 or resposta <= len(produtos):
                try:
                    print()
                    quantidade_reposta = int(input("Quantidade a repor: "))
                    if quantidade_reposta <= 0:
                        print("Inseriu valores negativos!")
                    else:
                        produto = produtos[resposta] 
                        if (str)(produto.get_quantidade()) == "Sem stock!":
                            quantidade_disponivel  = 0
                        else:
                            quantidade_disponivel = produto.get_quantidade()
                        nova_quantidade = quantidade_disponivel + quantidade_reposta
                        produto.set_quantidade(nova_quantidade)
                        print("Produto reposto com sucesso!")
                except Exception as X:
                    print("Inseriu um valor inválido!")
            else:
                print("Valor inválido!")
        except Exception as X:
            print("Inseriu um valor inválido!")
        finally:
            print()
            resposta = input("Quer registar outra reposição (S/N)? ")
            if (len(resposta) > 0):
                if (resposta[0] == 's' or resposta[0] == 'S'):
                    return registarReposicao(produtos)
                else:
                    return 
                   

#escolha 6 - apagar produtos
def apagarProdutos(produtos):
    if not produtos:
        print("Não existem produtos no armazém!")
    else:
        for i, produto in enumerate(produtos, start=1):
            print(f"{i}. {produto.get_nomeProduto()}")
        try:
            print()
            resposta = int(input("Qual o produto que deseja apagar? ")) - 1
            certeza = input("Tem a certeza que deseja apagar esse produto (S/N)? ")
            if (certeza[0] == 's' or certeza[0] == 'S'):
                del produtos[resposta]
                print("O seu produto foi apagado com sucesso!")
            else:
                print("Operação cancelada.")
                return
        except Exception as X:
            print("Inseriu um valor inválido!")   
    return 

#escolha 7 - sair do programa
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
def guardaFicheiro(produtos, nomeFicheiro):
    try:
        # 1. Abertura do ficheiro
        with open(nomeFicheiro, "w") as fo:
            # 2. Escrita de dados
            for produto in produtos:
                fo.write(str(produto.get_nomeProduto()) + "\n")
                fo.write(str(produto.get_preco()) + "\n")
                fo.write(str(produto.get_quantidade()) + "\n")
        print("Dados guardados com sucesso!")
    except Exception as X:
        print("Erro ao guardar os dados no ficheiro: ", X)

def leFicheiro(produtos, nomeFicheiro):
    try:
        with open(nomeFicheiro, "r") as fo:
            while True:
                nome_produto = fo.readline().strip()
                if not nome_produto:  
                    break
                preco_str = fo.readline().strip()
                quantidade_str = fo.readline().strip()
                preco = float(preco_str)
                quantidade = int(quantidade_str)
                produto = Produto(nome_produto, preco, quantidade)
                produtos.append(produto)
        print("Dados lidos com sucesso!")
    except Exception as e:
        print("Erro ao ler os dados do ficheiro: ", e)

#FIM DE FUNÇOES------------------------------------------------------


produto_numero = 0
produtos = []
NUMOPCOES = 7
produto = 0
escolha = 0
nome = '\0'
nFicheiro = "armazem.txt"
quantidade = 0
resposta = 0
venda = []
preco = 0
titulo =""
menu = ["" for cOpcao in range(0,NUMOPCOES,1)]
queroSair = False


leFicheiro(produtos, nFicheiro)
titulo = defineTitulo(titulo)
menu = inicializaMenu(menu)
cicloPrincipal(produtos,titulo, menu)
despedida()



