def q0(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3):
    if(fita1[cabeca1] == "a"):
        fita2.append(fita1[cabeca1])
        cabeca1 = cabeca1 + 1
        cabeca2 = cabeca2 + 1
        cabeca3 = cabeca3 + 0
        q0(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)
    elif(fita1[cabeca1] == "b"):
        fita2.append(fita1[cabeca1])
        cabeca1 = cabeca1 + 1
        cabeca2 = cabeca2 + 1
        cabeca3 = cabeca3 + 0
        q1(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)
    else:
        print(fita1+"REJEITA")

def q1(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3):
    if(fita1[cabeca1] == "b"):
        fita2.append(fita1[cabeca1])
        cabeca1 = cabeca1 + 1
        cabeca2 = cabeca2 + 1
        cabeca3 = cabeca3 + 0
        q1(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)
    elif(fita1[cabeca1] == "c"):
        fita3.append(fita1[cabeca1])
        cabeca1 = cabeca1 + 1
        cabeca2 = cabeca2 + 0
        cabeca3 = cabeca3 + 1
        q2(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)
    else:
        print(fita1+"REJEITA")
        
def q2(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3):
    if(fita1[cabeca1] == "c"):
        fita3.append(fita1[cabeca1])
        cabeca1 = cabeca1 + 1
        cabeca2 = cabeca2 + 0
        cabeca3 = cabeca3 + 1
        q2(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)
    elif(fita1[cabeca1] == "d"):
        fita3.append(fita1[cabeca1])
        cabeca1 = cabeca1 + 1
        cabeca2 = cabeca2 + 0
        cabeca3 = cabeca3 + 1
        q5(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)
    else:
        print(fita1+"REJEITA")
        
def q5(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3):
    if(fita1[cabeca1] == "d"):
        fita3.append(fita1[cabeca1])
        cabeca1 = cabeca1 + 1
        cabeca2 = cabeca2 + 0
        cabeca3 = cabeca3 + 1
        q5(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)
    elif(fita1[cabeca1] == "e"):
        cabeca1 = cabeca1 + 0
        cabeca2 = cabeca2 - 1
        cabeca3 = cabeca3 - 1
        q6(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)
    else:
        print(fita1+"REJEITA")    
        
def q6(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3):
    white = " "
    branco = -1    
    if(fita1[cabeca1] == "e" and fita2[cabeca2] == "b" and fita3[cabeca3] == "d"):
        cabeca1 = cabeca1 + 1
        cabeca2 = cabeca2 - 1
        cabeca3 = cabeca3 - 1
        q6(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)
    elif(fita1[cabeca1] == "f" and fita2[cabeca2] == "a" and fita3[cabeca3] == "c"):
        cabeca1 = cabeca1 + 1
        cabeca2 = cabeca2 - 1
        cabeca3 = cabeca3 - 1
        q6(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)
    elif(fita1[cabeca1] == white and cabeca2 == branco and cabeca3 == branco):
        q3(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)        
    else:
        print(fita1+"REJEITA")
            
def q3(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3):
    print(fita1+"ACEITA")
    
entrada = str(input())
fita1 = []
fita2 = []
fita3 = []
cabeca1 = 0
cabeca2 = 0
cabeca3 = 0
entrada = entrada.strip()
fita1 = entrada + " "
q0(fita1,fita2,fita3,cabeca1,cabeca2,cabeca3)