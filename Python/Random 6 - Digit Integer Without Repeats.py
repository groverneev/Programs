import random
y = 0
while y != 1:
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    e = random.randint(0, 9)
    f = random.randint(0, 9)
    if a != b and a != c and a != d and a != e and a != f:
        if b != c and b != d and b != e and b != f:
            if c != d and c != e and c != f:
                if d != e and d != f:
                    if e != f:
                        y = 1
a = str(a)
b = str(b)
c = str(c)
d = str(d)
e = str(e)
f = str(f)
print(a+b+c+d+e+f)
