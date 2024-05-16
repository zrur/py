class Pneu():
    def __init__(self) :
        self.marca = "Generico"
        self.aro = 14
        self.vida_util = 1000
        
        
    def usar(self):
        if self.vida_util >100:
            self.vida_util = self.vida_util - 1
        else:
            print("Pneu deve ser trocado") 
                

#relaçao de carro tendo o pneu


class Carro:
  #as variaveis quando esta dentro da self ela sobrevive ate q o objeto seja destruido  
    def _init_(self):# contsrutor init serve pra n ficar instanciando toda vez
        self.ligado = False
        self.marca = "Generica"
        self.modelo = "X"
        self.velocidade = 0
        self.pneu = Pneu()
        print("Construtor Carro executado")
        
    
    def ligar(self):
        self.ligado = True
        
    def desligar(self):
        self.ligado = False
    
    def situacao(self):
        # if self.ligado:
        #    texto = "Ligado"
        #else:
        #    texto = "Desligado"
        
        texto = "Ligado" if self.ligado else "Desligado"
        print(f"O carro{self.modelo} da {self.marca} "+ \
            "esta {texto} viajando a {self.velocidade} por hora")
  
def acelerar(self):
    if self.ligado:
        self.velocidade = self.velocidade + 5
        self.pneu.usar()
         
  
  
  
def main():    
    c1 = Carro()
    c2 = Carro()
    c3 = Carro()
    

    c1.marca = "Fiat"
    c1.modelo = "Mobly"
   


   
    c2.marca = "Citroen"
    c2.modelo = "C3"
    
   
    c1.modelo= "Kwid"
    
    c1.pneu.marca = "Pirrelli"
    c1.pneu.marca = 105
    c1.ligar()
    c1.acelarar()
    c1.acelarar() 
    c1.acelarar() 
    c1.acelarar() 
    c1.acelarar()
    
    c2.ligar()
    c2.acelerar()
    c2.acelerar()
    
    c2.situacao()#ligaçao com a instancia c1
    c1.situacao()
    c3.situacao
 #variaveis somem os objetos nao
#print("modulo carro:",_name_)
if __name__ == "_main_":
    main()