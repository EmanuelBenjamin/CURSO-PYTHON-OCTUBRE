import pytest
import flask
import sys
import os
import logicos
#sys.path.append('./modulo_interior')
from modulo_interior import interior, objeto_interior
from modulo_interior.interior import saludo
from logicos import verificar_edad,EDAD_MINIMA
from logicos import *
import modulo_main


#import generaciones as g

generaciones = 1

#print(logicos.edad)
#logicos.verificar_edad()

#print(EDAD_MINIMA)
#print(EDAD_MAXIMA)

print(interior.saludo)
print(objeto_interior)
#print(sys.path)
print(os.getenv('PYTHONPATH'))
print(saludo)

#os.environ['PYTHONPATH']='valor diferente'
print(os.getenv('PYTHONPATH'))
#print(dir())
print(modulo_main.saludar('erick'))

try:
    import moduloquenoexiste
except ModuleNotFoundError as e:
    print('Disculpe, este modulo no esta disponible', e)