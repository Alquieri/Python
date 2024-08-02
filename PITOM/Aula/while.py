


# While true
''' while True:
     op = input("s ou n: ").lower()
     if op == "s" or op == "n":
         print ("ok")
         break
     print("lalala")

op = input("s ou n: ").lower()'''



# while com condição

'''while op != "s" and op != "n":

    print("Erro")
    op = input("s ou n: ").lower()

print("ok")'''
 
 # while q escolhe
'''num = int(input("-->"))

i = 1

while i<= num:
    print(i)
    i += 1'''

n1 = int(input("Digite um numero:  "))

n2 = n1 - 1

n3 = n1

while n2 >= 1:
   
   n3 = n3 * n2
   n2-=1

print(" O Resultado de sera ", (n2))