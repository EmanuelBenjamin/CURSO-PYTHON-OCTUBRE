def sumar():
    return 3 + 4
print(f"la respuesta es: {sumar()}")

numero = sumar()

if numero == 5:
    print("si es 5")
elif numero == 7:
    print("haaa era un siete")
else:
    print("no es un 5")
#reservadas tipo bucle
x = 0
while x < 3: #mientras x sea menor a 3 va a hacer algo (que va a hacer: imprimir el numero)
    print(x)
    x += 1

print(range(3)) #ejecuta un rango

for i in range(3):
    print(i)
print("separacion")
for i in range(3):
    if i == 1:
        continue
    print(i)

print("separacion")
for i in range(3):
    if i == 1:
        break
    print(i)

#valores se representan con los valores TRUE  Y FALSE

#print(True)
#print(False)

def isAdult(edad):
    return edad >= 18

print(isAdult(15))
print(isAdult(20))

#print(None)

def vacia():
    pass

print(vacia())

print(True and True)
print(True or False)
print(not True)

if not isAdult(15):
    print('no es un adulto')