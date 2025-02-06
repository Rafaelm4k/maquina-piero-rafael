vector=[]
for i in range(10):
    continuar=True
    while continuar:
        numeros=int(input(f"ingresa los datos numero {i+1}:\n"))
        vector.append(numeros)
        continuar=False
valor_maximo=max(vector)
numero_veces=vector.count(valor_maximo)
print(f"el maximo es {valor_maximo}")
print(f"aparece {numero_veces}")
