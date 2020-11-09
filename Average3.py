a, b, c, d = map(float, input().split())

avg1 = (a * 2 + b * 3 + c * 4 + d * 1) / 10

print("Media: %.1f" % (avg1))

if avg1 >= 7.0:
    print("Aluno aprovado.")

elif avg1 < 5.0:
    print("Aluno reprovado.")

elif 5.0 <= avg1 <= 6.9:
    print("Aluno em exame.")
    sc = float(input())
    print("Nota do exame: %.1f" % (sc))
    avg2 = (avg1 + sc) / 2
    if avg2 >= 5.0:
        print("Aluno aprovado.")
    elif avg2 <= 4.9:
        print("Aluno reprovado.")
    print("Media final: %.1f" % (avg2))
