#FOR range

'''
for i in range(31):
    if i % 2 == 0:
        print(i)
'''


'''i=0
for i in range(0,31,2) :
    print(i)'''

#fazer tabuleiro
'''
j = int(input("Digite um numero: "))

for i in range(j):
    for i in range(j):
        print("x", end = " ")
    print(" ") 
''' 


for i in range(10):
    n1 = int(input("--->"))

    if n1 == 0:
        break
    elif n1 < 0:
        continue
print("i =", i)
    