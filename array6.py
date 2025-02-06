from pydoc import apropos

import  random
notas=[random.randint(0,10) for i in range(40)]
medianotas=sum(notas)/len(notas)
aprobados=0
suspensos=0
sobremedia=0
for i in range(len(notas)):
    if notas[i]<5:
        suspensos+=1
    else:
        aprobados+=1
    if notas[i]>medianotas:
        sobremedia+=1
print(f"los aprobados:{aprobados}")
print(f"los suspensos:{suspensos}")
print(f"los que estan sobre la media es:{sobremedia}")
