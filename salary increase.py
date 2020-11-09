sal = float(input())

if 0 <= sal <= 400:
    in_sal = sal + (0.15 * sal)
    dif = in_sal - sal
    print("Novo salario: %.2f" % (in_sal))
    print("Reajuste ganho: %.2f" % (dif))
    print("Em percentual: 15 %")

elif 400 < sal <= 800:
    in_sal = sal + (1.2 * sal)
    dif = in_sal - sal
    print("Novo salario: %.2f" % (in_sal))
    print("Reajuste ganho: %.2f" % (dif))
    print("Em percentual: 12 %")

elif 800 < sal <= 1200:
    in_sal = sal + (0.1 * sal)
    dif = in_sal - sal
    print("Novo salario: %.2f" % (in_sal))
    print("Reajuste ganho: %.2f" % (dif))
    print("Em percentual: 10 %")

elif 1200 < sal <= 2000:
    in_sal = sal + (0.07 * sal)
    dif = in_sal - sal
    print("Novo salario: %.2f" % (in_sal))
    print("Reajuste ganho: %.2f" % (dif))
    print("Em percentual: 7 %")


else:
    in_sal = sal + (0.04 * sal)
    dif = in_sal - sal
    print("Novo salario: %.2f" % (in_sal))
    print("Reajuste ganho: %.2f" % (dif))
    print("Em percentual: 4 %")
