#edad = input("ingrese su edad:\n")
if int(edad)>18:
    print("tu eres mayor de edad")
elif int(edad)== 18:
    print("tu tienes 18 a;os exactos")
else:
    print("tu eres menor de edad")

#edad = int(input("ingrese su edad:\n"))

#if edad>18:
    #print('Tu eres mayor de edad')
#elif edad==18:
    #print('Tu tienes 18 a;os exactos')
#else:
    #print('Tu eres menor de edad')

#condicional anidada
edad_parseada = int(edad)

if edad_parseada > 18:
    if edad_parseada == 20:
        print('Tienes 20')

if edad_parseada > 18:
    pass
else:
    print(' No puedes entrar')

nombre = 'RAFAEL'
if nombre.upper().strip() !='RAFAEL':
    print('Que bueno que no eres Rafael Bienvenido')
else:
    print('Que no puedes entrar')


