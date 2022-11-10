edad = 17


#if edad < 18:
    #raise Exception('Eres menor para usar el programa')

print('continuacion')

class AgeException(Exception):
    pass

try:
    'texto' + 5
    if edad < 18:
        raise AgeException('Eres menor para usar el programa')
except Exception:
    print('se lanzo el error')
