import math

a, b, c = map(float, input().split())
if b**2 - 4*a*c > 0 and 2*a > 0:
    ans1 = -b + math.sqrt(b ** 2 - 4 * a * c)
    ans2 = -b - math.sqrt(b ** 2 - 4 * a * c)
    print("R1 = %.5f" % (ans1 / (2 * a)))
    print("R2 = %.5f" % (ans2 / (2 * a)))

else:
    print("Impossivel calcular")
