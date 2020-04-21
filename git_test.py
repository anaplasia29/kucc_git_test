def gen(y):
    print(type(y))
    for x in range(y):
        yield x


#gen(100)
for i in gen(100):
    print(i)

while True:
    print("Hello World")
for j in range(100):
    print(j)

while True:
    break

print("new world")