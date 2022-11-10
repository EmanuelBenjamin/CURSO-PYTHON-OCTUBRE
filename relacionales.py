# ==
color = 'azul'
print(color == 'azul')
print(color == 'rojo')

#!= diferente que
print(color != 'rojo')

# > mayor que
altura = 172
altura_minima = 150
print(altura > altura_minima)
# < menor que
print(altura < altura_minima)

# >= mayor o igual que
print(altura >= altura_minima)

precio = 100
IVA = 0.12
impuesto = precio * IVA
impuesto = precio * IVA
print(impuesto)

# <=
print(altura >= altura_minima)

def abrir_puerta(altura,edad):
    ALTURA_MINIMA = 150
    EDAD_MINIMA = 15
    EDAD_MAXIMA = 80

    if altura <= ALTURA_MINIMA:
        print('No Alcanza')
        return
    if edad <= EDAD_MINIMA:
        print('Muy Joven')
        return
    if edad >= EDAD_MAXIMA:
        print('Muy grande')
        return
    print('Pase Adelante')
abrir_puerta(155, 13)
