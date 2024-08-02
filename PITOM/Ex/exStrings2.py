#Exercicio 1
'''
nome = (input("Digite seu nome: "))

#nome = "Aelin Tricolor de Henrique Chaves "
n = nome.split()

for i in n:
    if len(i) == 2:
        print(i, end = " ")
    else:
        print(i[0],end = ". ")'''

#Exercico 2

'''nome = (input("Digite seu nome: "))


n = nome.split()
print(n[-1], end = " ")

for i in n:
    if len(i) == 2:
        continue
    else:
        if(n[-1] == i):
            break

        print(i[0],end = ". ")'''
      
    

'''
Dominios = ["@gmail.com", "@hotmail.com", "@outlook.com", "@live.com", "@yahoo.com", "@ymail.com", "@icloud.com", "@terra.com.br", "@uol.com.br"]


while True: 
    nome = (input("Digite seu email: "))
    Aoba = nome.find("@")
    
    if nome[Aoba:] in Dominios:
            print(nome)
            break
    elif(Aoba == -1 ): 
        print("Email invalido")
        continue
        
    else:
        print("Dominio não presente")
        n2 = int(input("1 continuar, 2 Digitar outro email: "))
        if(n2 == 1):
                print("ok")
                break
        elif(n2 == 2):
             continue
        else:
            print("Errou")
   '''  
   
#ex4


"""
    cont = 0
    cpf = (input("Digite seu CPF: "))
    
    if(cpf.isnumeric() is True and len(cpf) == 11):
        
        print("{}.{}.{}-{} ".format(cpf[:3],cpf[3:6],cpf[6:9],cpf[9:11]))
        
        while True:
            n1 = input("O valor digitado está correto ?")
            if(n1 == "s"):
                print("Ebaa")
                cont = 1
                break
            elif(n1 == "n"):
                break
            else:
                print("Valor invalido")
                
    if (cont == 1):
        break
          
            
    else:
        print("digite seu cpf corretamente")
        continue"""
     
     
''' 
while True:
    cpf = (input("Digite seu CPF: "))


    if(cpf[3] == "." and cpf[7] == "."  and cpf.find("-") == 11 and len(cpf) == 14):
        print(cpf)
        
        while True:
                n1 = input("O valor digitado está correto ?")
                if(n1 == "s"):
                    print("Ebaa")
                    cont = 1
                    break
                elif(n1 == "n"):
                    break
                else:
                    print("Valor invalido")
                    
        if (cont == 1):
                 break

                    
        else:
            print("digite seu cpf corretamente")
        continue
    else:
            print("Formato invalido !")
    
       '''   

 

    
#exercicio 6

txt = input("Digitru uma frase: ").upper()
listi = []
cont = 0
cont2 = 0

for i in range (len(txt)):
    cont = 0
 
    

    for j in range (len(txt)):
        
        if(txt[i] == txt[j]):
            cont +=1
    if(txt[i] not in listi):
        listi.append(txt[i])
        print(txt[i], cont)
    
    

            

           













