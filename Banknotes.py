n = int(input())

ans = []

l = [100, 50, 20, 10, 5, 2, 1]
print(n)
for i in l:

    a = n//i
    ans.append(a)
    n = n - (a*i)


print("%d nota(s) de R$ 100,00" % (ans[0]))
print("%d nota(s) de R$ 50,00" % (ans[1]))
print("%d nota(s) de R$ 20,00" % (ans[2]))
print("%d nota(s) de R$ 10,00" % (ans[3]))
print("%d nota(s) de R$ 5,00" % (ans[4]))
print("%d nota(s) de R$ 2,00" % (ans[5]))
print("%d nota(s) de R$ 1,00" % (ans[6]))
