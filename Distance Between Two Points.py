import math
a, b = map(float, input().split())
c, d = map(float, input().split())

dis = math.sqrt((c-a)**2 + (d-b)**2)

print("%.4f" % (dis))
