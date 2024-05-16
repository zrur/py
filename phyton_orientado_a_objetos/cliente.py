class Cliente:
    
    def _init_(self):#self é o objeto
        self.nome = "Desconhecido"
        self.cpf = ""
        self.idade = 0
    
    def comprar(self):
        print(f"{self.nome} com {self.idade} nos esta comprando um produto ")
    
    def trocar(self):
        print(f"{self.nome} Trouxe meu periferico para trocar")
    
    def reclamar(self):
        print(f"Eu {self.nome} CPF {self.cpf}Vim reclamar de algo")
        