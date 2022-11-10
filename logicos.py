edad = 14
nombre = 'Andrea'
EDAD_MINIMA = 15
EDAD_MAXIMA = 85

def verificar_edad():
    if edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
        print('No puede entrar')

    if edad == 15 and nombre == 'Carmen':
        print('Carmen no puedes entrar')

condicion = edad == 15 and nombre == 'Carmen'
#print(not condicion)

x = 2
y = 5
#print(not x > y)


