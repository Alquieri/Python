print("    Bem vindo ao Lig - 4")

for i in range (20): 
    print('-', end="")


def tabuleiro():
    cont = 0
    for j in range (7):
        print( "" )
        for i in range (8): 
            if(cont <= 6):
                  print("  ", i + 1 , end="")
                  cont+=1
            else:
                print("|   ",  end="")
                
        
        
print("\n       Jogador 1 : ")

tabuleiro()

