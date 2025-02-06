vector=[i]
for i in range (10):
    vector.append(int(input("ingresa los numeros:")))
longitudpar=0
sumapar=0
longitudinpar=0
sumaimpar=0
for i in range(len(vector)):
    if vector[i]%2==0:
        sumapar+=vector[i]
        longitudpar+=1
    else:
        sumaimpar+=vector[i]
        longitudinpar+=1
print(f"la media de los pares es: {sumapar/longitudpar}")
print(f"la me dia de los impares es :{sumaimpar/longitudinpar}")