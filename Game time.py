a, b = map(int, input().split())
count = 0
if a == b:
    print("O JOGO DUROU 24 HORA(S)")
elif a > b:
    a = 24 - a
    print("O JOGO DUROU %d HORA(S)" % (a+b))

else:
    print("O JOGO DUROU %d HORA(S)" % (b-a))
