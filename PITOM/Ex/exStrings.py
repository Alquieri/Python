
#exercicio 1 

'''nome = input("digite seu nome completo com todas as letras minusculas: ")

print(nome.title())

cont = (len(nome) - (nome.count(' ')))

print(" Seu nome tem ", cont ,"letras")'''

#exercico 2

'''temp = int(input("digite o tempo em segundos: "))

hora = temp//3600

min = (temp%3600)//60

seg = (temp%3600)%60



print("{:02d}h {:02d}min {:02d}seg". format(hora,min,seg) )'''

#exercicio3 
'''n1 = float(input("Digite um numero  "))
n2 = float(input("Digite outro "))
n3 = float(input("Digite outro "))


media = (n1 + n2 + n3)/3


print(media)'''



#exercecio 4

'''n1 = int(input("Digite um numero: "))

if  (n1 % 2) == 0:

    print ("O numero é par ")

else :
    print ("O numero é impar ")'''
    
    
#exercicio 5

'''n1 = int(input("Digite o Primeiro numero: "))
n2 = int(input("Digite o Segundo numero: "))

if n1 > n2 :
    print(" O maior é o primerio ")
elif n1 < n2 :
     print("O maior é o segundo")
else : 
    print("São iguais")'''


#exercicio 6

'''l1 = input("Digite F ou M: ")

if l1 == "F":
    print("feminino")
elif l1 == "M":
    print("Masculino")
else :
    print("Caracter invalido")'''
    
#exercico7

'''n1 = int(input("Digite o primeiro  numero  "))
n2 = int(input("Digite o segundo   numero  "))
n3 = int(input("Digite o terceiro  numero  "))


if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n3 and n3 > n1:
    maior = n2
else:
    maior = n3
    
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3 and n3 < n1:
    menor = n2
else:
    menor = n3
    
print(" o maior numero é: ", maior)
print(" o menor numero é: ", menor)'''


#exercicio8

n1 = int(input("Digite um numero interio menor que 1000: "))


'''if n1 < 1000:
    cent = n1//100
    dez = (n1//10) - (cent *10)
    seg = (n1 - (dez * 10)) - (cent * 100)
    print("{} Centenas {} Dezenas {} Unidades".format(cent,dez,seg))
else :
    print("erro")'''


#exercicio9

'''kwk = float(input("Digite o quanto de kwk foi consumida: "))
tipo = input("digite o tipo(R, C ou I): ")

tipo = tipo.upper()


if tipo == "R":
    if kwk <= 500:
        valor = kwk * 0.40
    else :
        valor = kwk * 0.65
elif tipo == "C":
    if kwk <= 1000:
        valor = kwk * 0.55
    else :
        valor = kwk * 0.60
elif tipo == "I":
    if kwk <= 5000:
        valor = kwk * 0.55
    else :
        valor = kwk * 0.60
else :
    print("erro")
        
print("Valor a pagar: R$",valor)'''

#Exercicio10

'''n1 = int(input("Digite o primeiro  numero  "))
n2 = int(input("Digite o segundo   numero  "))
op = input("digte a operaçao (+,-,* ou /) ")


if op == "+":
    result = n1 + n2
elif op == "-":
   result = n1 - n2
elif op == "*":
   result = n1 * n2
elif op == "/":
    if n2 != 0 and n1 != 0 :
       result = n1 / n2
    else:
        print ("erro") 
else:
    print("erro")
    
print("O resultado sera: ", result)'''

#exercicio11

'''l1 = input("Digite uma letra: ")
l1 = ord(l1)
if l1 >= 65 and l1 <=  90:    
    l1 = l1 + 32
elif l1 >= 97 and l1 <=  120:
    l1 = l1 - 32

print(chr(l1))'''



  


            



    
    



























