
a = int(input("coeficiente pricipal: "))
b = int(input("coeficiente secundário: "))
c = int(input("termo independente: "))

def raizquad(val):
    return val**0.5

delta = b ** 2 - 4 * a * c
x_ver = -b/2*a
y_ver = -delta/4*a

if delta >= 0:
    raiz1 = (-b + raizquad(delta)) / (2 * a)
    raiz2 = (-b - raizquad(delta)) / (2 * a)
else:
    print('delta negativo')
    exit()
    
print(raiz1)
print(raiz2)

print(delta)
print(x_ver)
print(y_ver)



