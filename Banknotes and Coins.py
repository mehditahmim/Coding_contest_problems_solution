tk = float(input())
frac = tk - int(tk)
f = round(frac, 2)
n = int(tk)
ans = []

l = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]

for i in l:
    a = n // i
    ans.append(a)
    n = n - (a * i)

l1 = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
ans1 = []
f = n+f

for i in l1:
    a1 = f/i
    a1 = int(a1)
    ans1.append(a1)
    f = round(f - (a1 * i), 2)


print("NOTAS:")
for i, j in zip(ans, l):
    print("%d nota(s) de R$ %.2f" % (i, j))

print("MOEDAS:")

for d, e in zip(ans1, l1):
    print("%d moeda(s) de R$ %.2f" % (d, float(e)))
