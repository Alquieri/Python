
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    def defno(self, valor):
        if valor < self.valor:
            if self.esquerda :
                 self.esquerda.defno(valor)    
            else:
                 self.esquerda = No(valor)
                 print("valor de cima", self.valor, "nó esquerda: ",valor)
        elif valor > self.valor:
            if self.direita:
                 self.direita.defno(valor)           
            else:
                 self.direita = No(valor)
                 print("valor de cima", self.valor, "nó direita: ",valor)
        else: 
            print("naaaooo")

    def ordem(self):
        if self.esquerda:
            self.esquerda.ordem()
        print(self.valor)    
        if self.direita: 
            self.direita.ordem()
      
        
        
no = No(int(input("Digite o nó mamae")))

print("Digite A para encerrar a qualquer momento")

while True: 
    try:

        n = int(input("Digite o proximo nó: "))
        no.defno(n)

    except ValueError:
        break
    

no.ordem()





            

    
    
    













