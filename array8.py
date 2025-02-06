import  random
vector=[random.randint(0,100) for i in range(10)]
vector.sort()
print(vector)
pos =int(input(f"introduce un numero:\n"))
vector=vector[:pos]+vector[(pos+1):]
print(vector)