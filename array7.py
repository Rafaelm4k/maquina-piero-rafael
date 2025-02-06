import  random
vector=[random.randint(0,100) for i in range(100)]
vector.sort()
print(vector)
numero=(int(input("dame un numero:\n")))
pos =0
for i  in range(len(vector)):
    if numero<vector[i]:
        pos=i
        break
vector=vector[:pos]+[numero]+vector[pos:]
print(vector)