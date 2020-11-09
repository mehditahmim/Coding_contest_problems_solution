a, b, c, d = map(int, input().split())
min = d - b


if a < c and min >= 0:
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (c-a, min))

elif a < c and min < 0:
    hr = (c-a)-1
    min = (60-b)+d
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hr, min))


elif a > c and min >= 0:
    hr = 24 - (a - c)
    min = d - b
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hr, min))

elif a > c and min < 0:
    hr = (24 - (a-c))-1
    min = (60 - b) + d
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hr, min))

elif a == c and min < 0:
    hr = (24 - (a-c))-1
    min = (60 - b) + d
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hr, min))

elif a == c and min > 0:
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (0, min))

else:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
