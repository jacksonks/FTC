import re
entrada = str(input())
lista = []
lista.append(entrada)

def login(a):
    if(re.match(r'^[a-z]*[a-zA-Z]*$', a)):
        return True
    else:
        return False
    
if((login(lista[0]) == True)):
    print(True)
elif((login(lista[0]) == False)):
    print(False)