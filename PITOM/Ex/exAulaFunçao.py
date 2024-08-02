#ExHoras
'''
def horasFormatadas(hora):
    if(int(hora[0]) > 12):
        nhora = int(hora[0]) - 12
        print(f"{nhora}:{hora[1]} pm")

    elif(int(hora[0]) < 12) :
        print(f"{hora[0]}:{hora[1]} am")

    elif(int(hora[0]) == 12 and int(hora[1]) > 0):
           print(f"{hora[0]}:{hora[1]} pm")


while True:
    try:
        hora = input("Digite a hora no formato padrão: ")
        if(hora[2] == ":" and len(hora) == 5):
            hora = hora.split(':')
            if (int(hora[0]) <= 23 and  int(hora[1]) <= 59):
                horasFormatadas(hora)
                break
            else:
                raise IndexError
        else:
            raise IndexError
    except(IndexError):
        print("seu bananao")'''








