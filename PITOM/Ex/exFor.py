#ex1
'''
n1 = int(input("Digite um numero: "))

for i in range (11):
    result = i * n1
    print("{} X {} = {}".format(n1,i,result))
'''
#ex2
'''
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite o começo : "))
n3 = int(input("Digite o final: "))


for i in range (n2,n3 + 1):
    result = i * n1
    print("{} X {} = {}".format(n1,i,result))
'''

#ex3
'''
n1 = int(input("Digite um numero:  "))

n2 = n1 - 1
n3 = n1

for i in range(n1 + 1):
        
   n3 = n3 * n2
  
   n2 = n2 - 1
   
   if(n2 == 0):
        break
   

print(" O Resultado de sera ", (n3))
'''
                   

#EX4


'''
for i in range(1000,10000):
    n1 = i//100
    n2 = i%100
    n3 = n1 + n2

    if (i == (n3 * n3)):
        print(i)
'''

#Ex5
'''

n1 = int(input("Qual a base: "))
n2 = int(input("Qual o expoente: "))

n3 = 1

for i in range (n2):
    n3 = n1 * n3

print(n3)

'''

#Ex6
'''
soma = 1
ant = 0

n1 = int(input("Digite um numero: "))

for i in range(n1):

    result = soma + ant
    ant =  result - ant
    soma = result
   
  
    print(result)
    '''


#ex7 
'''
n1 = int(input("Digite um numero: "))


for j in range(1,n1):
    for i in range(j-1, 0, -1):
        if j % i != 0:
            continue
        elif i == 1:
            print(j)
        elif j % i == 0:
            break
        '''
        
        
#ex7
'''
cont = 0

n1 = int(input("Digite um numero: "))

for j in range(1,n1):
    cont = 0
    for i in range(1, n1):
        if(j % i == 0 ):
            cont = cont + 1
    if (cont <= 2):
        print(j)
'''         

#DESAFIO


for i in range(10,1000):
    
    
    n1 = (i//10)
    n2 = i % 10

    if (i > 100):
        n1 = (i//100)
        n2 = ((i // 10) - (n1 * 10))
        n4 = i % 10
    else: 
        n4 = 0
       
        
    n2 = n2 * n2
    n4 = n4 * n4 * n4
    
    
    n3 = n1 + n2 + n4
   
        
    if (i == n3 ):
        print("\n--- >", i)

    












