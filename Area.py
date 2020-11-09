a, b, c = map(float, input().split())

tri = 0.5 * a * c
circ = 3.14159 * c**2
trap = 0.5*(a+b)*c
sq = b**2
rect = a*b

print("TRIANGULO: %.3f" % (tri))
print("CIRCULO: %.3f" % (circ))
print("TRAPEZIO: %.3f" % (trap))
print("QUADRADO: %.3f" % (sq))
print("RETANGULO: %.3f" % (rect))
