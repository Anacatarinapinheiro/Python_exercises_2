class Empregado:

    def __init__(self, n="", dep="", sal=0.0):  # nome, departamento, salario
        self.__nome = n
        self.__departamento = dep
        self.__salario = sal

    # 2.2 Funções Setters
    def set_nome(self, x):
        self.__nome = x
    def set_departamento(self, x):
        self.__departamento = x
    def set_salario(self, x):
        self.__salario = x

    # 2.3 Funções Getters
    def get_nome(self):
        return self.__nome
    def get_departamento(self):
        return self.__departamento
    def get_salario(self):
        return self.__salario

    # 2.4 Funções Del
    # funções para deletar os atributos
    def del_nome(self):
        del self.__nome
    def del_departamento(self):
        del self.__departamento
    def del_salario(self):
        del self.__salario

    # 2.5 Funções de leitura
    def leNome(self):
        print("Qual é o nome do empregado?", end=" ")
        self.set_nome(input())
    def leDepartamento(self):
        print("Qual é o Departamento?", end=" ")
        self.set_departamento(input())
    def leSalario(self):
        print("Qual é o salário?", end=" ")
        self.set_salario(float(input()))
    def leTudoE(self):
        print()
        self.leNome()
        self.leDepartamento()
        self.leSalario()

    # 2.6 Funções de Apresentação

    # Listagem dos atributos do objeto
    def __str__(self):
        return f"{self.get_nome()}({self.get_departamento()})({self.get_salario()} €)"
    def mostraNome(self):
        print("Nome:", self.get_nome(), " | ", end="")
    def mostraDepartamento(self):
        print("Departamento:", self.get_departamento(), " | ", end="")
    def mostraSalario(self):
        print("Salário:", format(self.get_salario(), '.2f'), "€.")

    def mostraTudoE(self):
        print()
        self.mostraNome()
        self.mostraDepartamento()
        self.mostraSalario()
        
def quantosQuer():
    print()
    print ("Quantos empregados quer inserir? ",end = "")
    numEmpregado = int(input())
    return numEmpregado

# Função despedida()
def despedida():
    print("Obrigado por ter usado o nosso programa!")
    input("Prima qq tecla para continuar ...")
    return


##########################################################
# 4. Função principal
##########################################################

EMPREGADOS = []

for i in range(1, quantosQuer() + 1):
    empregado = Empregado()
    empregado.leTudoE()
    EMPREGADOS.append(empregado)

print()
print("Existem", len(EMPREGADOS), "empregados:")
for i in EMPREGADOS:
    i.mostraTudoE()

print()
despedida()
