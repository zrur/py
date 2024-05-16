Lista = []
rodando = True
while rodando:
    def menu_principal():
        print("MENU PRINCIPAL")
        print("(C) Cadastrar")
        print("(L) Listar")
        print("(P) Procurar")
        print("(S) Sair")
        opcao = input()
        return opcao


def cadastrar():
    print("Por favor informe a marca do Carro: ")
marca = str(input())
print("Por favor informe o modelo do Carro:")
modelo = str(input())
print("Por favor informe o ano do Carro:")
ano =float(input()) 
print("Por favor informe a placa do Carro:")
placa = str(input())
Lista.append(cadastrar)
 
def listar(lista_contato):
    indice = 0
    while indice < len(lista_contato):
        contato = lista_contato[indice]
        print("Nome\t\tTelefone\t\tEmail\t\tPeso")
        print(f"{contato['nome']}\t\t{contato['telefone']}\t\t" + \
              f"{contato['email']}\t\t{contato['peso']}")
        indice = indice + 1
    print("Tecle <ENTER> para continuar")
    input()

def escolha_opcoes():
    print('Digite Alguma opção: ')
    resposta = input().upper
    print("MENU PRINCIPAL")
    print("(C) Cadastrar")
    if resposta == "C":
        cadastrar()   
    elif resposta == "L":
        print("(L) Listar")
        Lista()
    elif resposta == "P":
        print("(P) Procurar")
        procurar()
    print("(S) Sair")
    
def procurar():
 print("Procurar placa de carro")
print("Qual placa de carro deseja procurar ?")
placa_procurar = str(input())

    