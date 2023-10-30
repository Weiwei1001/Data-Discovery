t = set()
t.add(1)
print(t)
a = tuple(t)
print(a)
a = {(0, 0): [0, 1], (1, 0): [2], (1, 1): [3], (2, 1): [4, 5]}
print(len(a))
for i in range(len(a)):
    print(a[i].value)