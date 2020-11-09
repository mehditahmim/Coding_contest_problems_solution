a, b, c = map(int, input().split())
if a < b and a < c:
    if b < c:
        print(a)
        print(b)
        print("%d\n" % c)

    else:
        print(a)
        print(c)
        print("%d\n" % b)


elif b < a and b < c:
    if a < c:
        print(b)
        print(a)
        print("%d\n" % c)

    else:

        print(b)
        print(c)
        print("%d\n" % a)

elif c < a and c < b:
    if a < b:
        print(c)
        print(a)
        print("%d\n" % b)
    else:
        print(c)
        print(b)
        print("%d\n" % a)
print(a)
print(b)
