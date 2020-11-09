a = input()
b = input()

p = ([float(i) for i in a.split()])
q = ([float(i) for i in b.split()])

print("VALOR A PAGAR: R$ %.2f" % (p[1]*p[2]+q[1]*q[2]))
