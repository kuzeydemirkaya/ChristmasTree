y = int(input("Bir sayi gir:"))
for i in range(0, y):
    a = i + 1
    c = 2*i + 1
    b = y - a
    if i <= 5:
        print(" " * b + "*" * c)
    elif 5 < i < 20:
        i = i - 6
        d = i + 1
        e = 2*i + 1
        f = y - d
        print(" " * f + "*" * e)
    elif i >= 20:
        i = i - 20
        g = i + 1
        h = 2*i + 1
        j = y - g
        print(" " * j + "*" * h)
