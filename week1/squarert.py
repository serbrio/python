import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

# ax^2 + bx + c = 0

d = (b**2) - (4*a*c)

if d < 0:
    print("no roots. sorry")
elif d is 0:
    x = -(b / (2*a))
    print(int(x))
    print(int(x))
else:
    x1 = (-b + ((b**2 - 4*a*c)**0.5)) / 2*a
    x2 = (-b - ((b**2 - 4*a*c)**0.5)) / 2*a
    print(int(x1))
    print(int(x2))



