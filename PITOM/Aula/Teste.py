print("ola")
hora = 1 
min = 2 


'''print( "O valor 1 é : { } \nO valor 2 é {} ".format(n1,n2))'''

print("\n{}h:{}min\n".format(hora, min))
print("{:02d}h:{:02d}min".format(hora,min))

#conta letra
'''txt = "sapo não lava o pé"

print(txt.count('a'))'''

#chr retorna a letra correspondente - ord retorna o numero
''' print(ord("a"))
print(chr(97))


l1 = input("Digite um letra ")
l2 = ord(l1) + 5

print(chr(l2))'''


l1 = input("Digite uma letra: ")



if ord(l1) >= 65 and ord(l1) <=  90:
     
    l2 = ord(l1) + 32
    
elif ord(l1) >= 97 and ord(l1) <=  120:
    l2 = ord(l1) - 32

print(chr(l2))



