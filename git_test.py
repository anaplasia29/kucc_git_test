def gen(y):
    print(type(y))
    for x in range(y):
        yield x


#gen(100)
for i in gen(100):
    print(i)
"""
print(gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100)
,gen(100))"""