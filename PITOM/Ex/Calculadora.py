def cientifica(result):
    
        print(result)
        n1 = input("Deseja em notação cientifica ? [s,n]")
        
        while True:
            if n1 == "s":
                nota = (f'{result : .1e}')
#print(nota[0])
#print(nota)
               
#print(nota[1], "* 10 ^", nota[7] )
                break
            elif  n1 == "n":
                print("Ok !")
                break
        

def numeroF():
    while True:
        try:
            n1 = float(input("digite um valor: "))
        except ValueError:
            print("Valor invalido")
        else:
            break
    return n1
def numeroI():
    while True:
        try:
            n1 = int(input("digite um valor: "))
        except ValueError:
            print("Valor invalido")
        else:
            break
    return n1


def soma():
    n1 = numeroF();
    n2 = numeroF();
    cientifica(n1 + n2)

def sub():
    n1 = numeroF();
    n2 = numeroF();
    cientifica(n1 - n2)

def mult():
    n1 = numeroF();
    n2 = numeroF();
    cientifica(n1 * n2)

def div():
    while True:
        n1 = numeroF();
        n2 = numeroF();
        if n1 != 0 and n2 !=0:
            cientifica(n1 / n2)
            break
        else :
            print("Não existe divisão por zero, digite novamente: ")

def inv():
    n1 = numeroF();
    cientifica(1/n1)

def pot():
    print("Expoente ") 
    n1 = numeroI()
    print("Base ")  
    n2 = numeroI()
   
    cientifica(n2 ** n1)

def fat(n1):
    
    n2 =  1      
    for i in range(n1,1,-1):
        n2 = n2 * i
    
    return n2
    
    
def eul():
    n1 = numeroI()
    n2 = 0
    for i in range(n1):
        n2 = (1 / fat(i)) + n2
    cientifica(n2)

def pi():
    n1 = numeroI()
    n2 = 0
    for i in range(n1):
        n2 = (((-1)**i) / (2* i + 1)) + n2
        
    print(n2 * 4)
    
    

print("MEGA CALUCULADORA")

while True:
    op = input("Qual operaçao voce deseja realizar [+, -, *, /, I, ^, !, e, pi]: " )

    if(op == "+"):
        soma()
        break
    elif(op == "-"):
        sub()
        break
    elif(op == "*"):
        mult()
        break
    elif(op == "/"):
        div()
        break
    elif(op == "I"):
        inv()
        break
    elif(op == "^"):
        pot()
        break
    elif(op == "!"):
        print(fat(numeroI()))
        break
    elif(op == "e"):
        eul()
    elif (op == "pi"):
        pi()
    else:
        print("erro")
