numero=input("dame un numero de 10 cifras:\n")
check=True
for i in range (int(len(numero)/2)):
    if numero[i]!= numero[len(numero)-1-i]:
        check = False
if check:
    print("es capicua:")
else:
    print("no es capicua:")