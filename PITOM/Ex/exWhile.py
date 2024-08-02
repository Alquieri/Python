import random



# exercicio 1
#condicçao

'''n1 = int(input("Digite um numero de 0 a 10 "))

while n1 > 10 or n1 < 0:

    print("Valor invalido ! Digite novamente")
    n1 = int(input())

print("ok")'''

#True

'''while True:
    n1 = int(input("Digite um numero de 0 a 10:  "))
    
    if n1 <= 10 and n1 >= 0:
        print("ok")
        break

    print("Tente novamente ! ")'''

#Exercicio 2 


'''n1 = int(input("Digite um numero de 0 a 10 "))
i = 0 

while n1 <= 10 and n1 >= 0:
    result = i * n1
    print("{:02d} x {:02d} = {:02d} ".format(i,n1,result) )
    i+=1
    if i == 11:
        break'''

#Exercicio 3

'''n1 = int(input("Digite um numero para tabua:  "))
n2 = int(input("Onde deseja começar a tauba:  "))
n3 = int(input("Onde deseja terminar a tabua:  "))

i = n2

while i <= n3:

    result = i * n1
    print("{:02d} x {:02d} = {:02d} ".format(i,n1,result) )
    i+=1'''

#Exercicio 4

'''n1 = int(input("Digite um numero:  "))

n2 = n1 - 1

n3 = n1

while n2 >= 1:
   
   n3 = n3 * n2
   n2-=1

print(" O Resultado de sera ", (n3))'''


# Exercicio 5

'''n1 = int(input("Digite um numero:  "))
soma = n1
qnt = 0

while True:

    n1 = int(input("Digite um numero:  "))
    qnt = qnt + 1
    soma = soma + n1
    


    if n1 == 0:
        med = soma / qnt
        print("Quantidade de numeros digitados: ", qnt)
        print("Soma: ",soma)
        print("Media: ", med)
        
        break'''

# exercicio 6

'''r1 = random.randrange(1,101)
n3 = 0

while True:
    n1 = int(input("Acerte um numero entre 1 e 100:  "))

    if(n1 > r1):
        print("Numero secreto é menor")
        
    elif(n1< r1):
        print("Numero secreto é maior")
        
    n3+=1
    if(n1 == r1):
        print("Acertouuu !")
        print("Voce acertou em ", n3)

        break'''

# exercicio 7

'''n1 = int(input("Digite a base:  "))

n2 = int(input("Digite o expoente:  "))
i = 1 
n3 = n1


while i < n2:

    n3 = n3 * n1
    i+=1

print("{:d} elevado a {:d} = {:d} ".format(n1,n2,n3) )'''












   



    





   



