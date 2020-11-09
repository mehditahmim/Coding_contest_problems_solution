code, unit = map(int, input().split())

if code == 1:
    print("Total: R$ %.2f" % (unit*4.00))

elif code == 2:
    print("Total: R$ %.2f" % (unit*4.50))

elif code == 3:
    print("Total: R$ %.2f" % (unit*5.00))

elif code == 4:
    print("Total: R$ %.2f" % (unit*2.00))

else:
    print("Total: R$ %.2f" % (unit*1.50))
