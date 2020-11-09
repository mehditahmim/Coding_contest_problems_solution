a = input()
p = ([int(i) for i in a.split()])
max = p[0]
for i in range(0, 3):
    if p[i] > max:
        max = p[i]

print("%d eh o maior" % (max))
