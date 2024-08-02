import random

#exercicio 1
'''
lista = []

for i in range(10):
    lista.append(input("--> "))

cont = 0
n1 = input("Numero : ")

for i in range(9):
    m =int(lista[i])
    if(n1 >  lista[i]):
        cont = cont + 1


print("Dentre os numero digitados, {} sao menores que {}".format(cont,n1))
'''
#exercicio 2
'''
lista = []
par = []
impar = []

for i in range(10):
    n1 = int(input("--> "))

    lista.append(n1)
    if(lista[i] % 2 ==0 ):
        par.append(n1)
    else:
        impar.append(n1)


print("Numeros: ", lista )
print("Par: ", par )
print("Impar: ", impar )

'''

#exercicio 3
'''
lista = []


for i in range(10):
    n1 = int(input("--> "))
    lista.append(n1)

    
Maior = lista[0]
Menor = lista[0]

for i in range(10):

    if(lista[i] > Maior):
        Maior = lista[i]
    elif(lista[i] < Menor ):
        Menor  = lista[i]



print("Numeros: ", lista )
print("Maior: ", Maior)
print("Menor: ", Menor )

'''

#exercicio 4

'''
lista = []






for i in range(10):

    n1 = int(input("--> "))
    lista.append(n1)
   
print("Lista antes de organizar: ", lista)

for i in range (10):
    for j in range(10):
        if(lista[i] <  lista[j]):
            memoria = lista[i]
            lista[i]  = lista[j]
            lista[j]  = memoria


print("Lista depois de organizar: ", lista)

'''
#exerciico 5
'''

lista = []

for i in range(10):

    n1 = int(input("--> "))
    lista.append(n1)
   
print("Lista antes de organizar: ", lista)

for i in range (10):
    for j in range(10):
        if(lista[i] >  lista[j]):
            memoria = lista[i]
            lista[i]  = lista[j]
            lista[j]  = memoria


print("Lista depois de organizar: ", lista)
'''
#exercicio6
'''
list1 = []
list2 = []

for i in range (10):
    list1.append((random.randint(0,15)))
    list2.append((random.randint(0,15)))



print(list1)
print(list2)

for i in range (10):
    for j in range (10):
        if(list1[i] == list2[j]):
            print("\nO numero {} esta nas duas listas." .format(list1[i]))

'''

#exercicio 7
'''
list1 = []
list2 = []
list3 = []

for i in range (10):
    list1.append((random.randint(0,15)))
    list2.append((random.randint(0,15)))

print(list1)
print(list2)

for i in range (10):
    for j in range (10):
        if(list1[i] == list2[j] and list1[i] not in list3):
            list3.append(list1[i])
            
           


for i in range (len(list3)):
     print("\nO numero {} esta nas duas listas." .format(list3[i]))


'''          
                   
#exercicio 8

'''
list1 = []
list2 = []
list3 = []
cont = 0

for i in range (10):
    list1.append(input("--> "))

print(list1)

for m in range (10):
    if list1[m] not in list3:
        list3.append(list1[m])

for i in range (len(list3)):
    list4 = []
    for j in range (10):
        if(i == list1[j]):
            list4.append(j + 1)
    if(len(list4) > 1):
        print("\nO elemento {} se repete nas casas {} ." .format(i, list4))
    else: 
        cont = cont + 1
    
    if cont == 10:
        print("\nNenhum elemento se repetiu ")'''
    




    
