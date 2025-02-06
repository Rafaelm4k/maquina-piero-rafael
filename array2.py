import random

vector1=[random.randint(0,100)for _  in range(15)]
vector2=[random.randint(0,100)for _ in range(15)]
vector3=[vector1[i]+vector2[i] for i in range(15)]
print("vecor1:",vector1)
print("vector2:",vector2)
print("vector3:",vector3)