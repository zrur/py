arq1= open("C:/Users/arthu/Videos/AnyDesk/nomes-idades.csv","r")
lista =[]
linha = "-"
while linha != "":
    linha = arq1.readline()
    linha = linha.replace("\n","")
    if linha != "":
        lista.append(linha)
    
        
print("Linhas: ", linha)
    
#texto = arq1.read()
#print("Text: ",texto)
#linha1 = arq1.readline()
#linha1 = linha1.replace("\n")
#print("Linha1: ",linha1)
#linha2 = arq1.readline()
#print("Linha2: ",linha2)
arq1.close()