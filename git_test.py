def gen(y):
    print(type(y))
    for x in range(y):
        yield x


#gen(100)
for i in gen(100):
    print(i)

for j in range(100):
    print(j)

while True:
    break

def printHello():
    print("hello world")


def fact(x):
    a = 1
    for i in range(2,x):
        a *= x
    return a