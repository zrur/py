from carro import Carro,Pneu

lista_carros = []
executando = True
while executando:

    if opcao == 'c':

      print("Criar Novo Carros: ")
    print("Informe a marca: ")
    marca = input()
    print("Informe o modelo: ")
    modelo = input()

    c1 = Carro ()
    c1.marca = marca
    c1.modelo = modelo
    
    lista_carros.append(c1)
    
