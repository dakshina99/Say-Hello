import random

with open("Index.txt") as f:
    a = list(map(lambda x: x.strip("\n"), f.readlines()))

while(a):
    inp = int(input())
    if inp == 0:break
    index = random.choice(a)
    a.remove(index)
    print("Its your turn :",index)


