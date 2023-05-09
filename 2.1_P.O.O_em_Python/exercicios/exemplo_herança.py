class Conta:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome = nome

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

# exemplo de herança simples


class contaInvestimento(Conta):
    def __init__(self, numero, nome, saldo, taxaJuros):
        Conta.__init__(self, numero, nome, saldo)
        self.taxaJuros = taxaJuros

    def adcionarJuros(self):
        self.saldo += self.saldo * (self.taxaJuros / 100)

# exemplo de composição = relacionamento entre as classes, sem ter herança


class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def retornaNome(self):
        return self.__nome


class Empresa:
    func = []

    def __init__(self):
        print("Empresa criada")

    def funcionar(self):
        while True:
            print("1 - contratar funcionario")
            print("2 - Listar funcionarios")
            op = int(input())

            if op == 1:
                self.contratarFuncionario()

            elif op == 2:
                self.listarFuncionarios()

            else:
                print("Opção invalida")

    def contratarFuncionario(self):
        nome = input("Digite o nome do funcionario: ")
        self.func.append(Funcionario(nome))

    def listarFuncionarios(self):
        for funcionario in self.func:
            print(funcionario.retornaNome())


empresa = Empresa()
empresa.funcionar()
