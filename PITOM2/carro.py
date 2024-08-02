class Carro:
    def __init__(self, cor, portas, velocidade,ligado):
        self.cor = cor
        self.portas = portas
        self.velocidade= velocidade
        self.ligado = ligado

    def ligar(self,):
        self.ligado = True
        print("o carro ligou")
    def desligar(self,):
        self.ligado = False
        print("o carro desligou")
    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade = self.velocidade + velocidade
            print("o carro aumentou a velocidade para ", self.velocidade )
        else:
            print("o carro esta desligado " )
            
    def frear(self, velocidade):
        if self.ligado:
            self.velocidade = self.velocidade - velocidade
            print("o carro diminuiu a velocidade para ", self.velocidade )
        else:
            print("o carro esta desligado " )


uno = Carro('azul', 4, 100, False)

op = input("Menu:\n[1] ligar carro\n[2] desligar carro\n[3] frear carro\n[4] acelerar carro\n[0] sair")

while True:
    if op == 1:
        uno.ligar()
    elif op == 2:
        uno.desligar()
    elif op == 3:
        uno.acelerar(int(input("quanto c quer acelerar: ")))
    elif op == 4:
        uno.frear(int(input("quanto c quer frear: ")))
    elif op == 0:
        print("Programa encerrado")
        break

    
