import  random
vector=[]
for i in range (10):
    vector.append(random.randint(0,100))
for i in range (len(vector)):
    if vector[i]%2==0:
        print(f"{i}: {vector[i]}")
