#a**2+bx+c
a = 1
b = -9
c = 20

D1 = b**2
D2 = 4*a*c
D = D1 - D2
print(D)
if D < 0:
    print("Коренів немає оскільки Дискримінант менший за 0: ", D)
elif D > 0:
    p1 = -b+D**0.5
    r1 = -b-D**0.5
    p2 = 2*a
    x1 = p1/p2
    x2 = r1/p2
    print(x1, ": X1")
    print(x2, ": X2")
else:
    p1 = -b+D**0.5
    r1 = -b-D**0.5
    p2 = 2*a
    x1 = p1/p2
    x2 = r1/p2
    print(x1, ": X1")
    print(x2, ": X2")
