arq1= open("C:/Users/arthu/Videos/AnyDesk/nomes-idades.csv","r")
lista =[]
linha = "-"
while linha != "":
    linha = arq1.readline()
    linha = linha.replace("\n","")
    #joao;(11)1111-1111;23
     #['joao';'(11)1111-1111;'23']
    if linha != "":
        dados = linha.split(";")
        print("Dados:",dados)
        d ={
            "nome":"Joao",
            "telefone": "(11)1111-1111",
            "idade": 23
        }
        lista.append(d)
print(lista)
    