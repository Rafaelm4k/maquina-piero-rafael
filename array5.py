alumnos=int(input("ingresa la cantidad de los alumnos:\n"))
estaturas=[]
for i in range(alumnos):
    estaturas.append(int(input("ingresa  la estaura de los alumnos:\n")))
    sumaestaura=sum(estaturas)
    mediaestaura=sumaestaura/len(estaturas)
    mayor_media=0
    menor_media=0
for i in range(len(estaturas)):
    if estaturas[i]>mediaestaura:
        mayor_media+=1
    elif estaturas[i]>mediaestaura:
        mayor_media+=1
    else:
        menor_media+=1
print(f"la media de todos los alumnos es:{mediaestaura}")
print(f"los que pasan la media: {mayor_media}")
print(f"los que estan por debajo de la media: {menor_media}")
