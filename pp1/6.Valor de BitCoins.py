import re
entrada = str(input())
lista = []
lista = entrada.split(" ")

def bit (f):
    if(re.match(r'(\A[B][$\b])', f)):
        if(re.match(r'([0-9]{1,}[\.][0-9]{2}$)', f)):
            return True
        else:
            return False
    else:
        return False

if((bit(lista) == True)):
    print(True)
elif((bit(lista) == False)):
    print(False)