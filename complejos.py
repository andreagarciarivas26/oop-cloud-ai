#Operaciones números complejos

#1. Suma

def suma (c1,c2):

    real=c1[0]+c2[0]
    imaginaria=c1[1]+c2[1]
    return (real,imaginaria)
    
print("La suma de los dos números complejos", suma((5,-4),(1,2)))

#2. Resta

def resta (c1,c2):

    real=c1[0]-c2[0]
    imaginaria=c1[1]-c2[1]
    return (real,imaginaria)
    
print("La resta de los dos números complejos es:", resta((5,-4),(1,2)))

#3. Multiplicación

def product (c1,c2):
    real=c1[0]*c2[0]-c1[1]*c2[1]
    imaginaria=c1[0]*c2[1]+c1[1]*c2[0]
    return (real,imaginaria)
print("La multiplicación de los dos números complejos es:", product((5,-4),(1,2)))

#4. División

def division (c1,c2):
    real=(c1[0]*c2[0]+c1[1]*c2[1])/(c2[0]*c2[0]+c2[1]*c2[1])
    imaginaria=(c1[1]*c2[0]-c1[0]*c2[1])/(c2[0]*c2[0]+c2[1]*c2[1])
    return(real,imaginaria)
print("la división de dos números complejos es:", division((5,-4),(1,2)))

#5. Módulo

def modulo (c1):
    valor=(c1[0]**2+c1[1]**2)**0.5
    return(valor)
print("el módulo del número imaginario es:", modulo((5,4)))

#6. Conjugado

def conjugado (c1):
    real=c1[0]
    imaginario=-1*c1[1]
    return(real,imaginario)
print("El conjugado del número imaginario es:", conjugado((3,2)))

#7. Conversión de cartesiano a polar

PI = 3.141592653589793


def arctan(x):
    resultado = 0

    for n in range(20):
        termino = ((-1)**n) * (x**(2*n + 1)) / (2*n + 1)
        resultado = resultado + termino

    return resultado


def atan2(b, a):

    if a > 0:
        return arctan(b / a)

    elif a < 0 and b >= 0:
        return arctan(b / a) + PI

    elif a < 0 and b < 0:
        return arctan(b / a) - PI

    elif a == 0 and b > 0:
        return PI / 2

    elif a == 0 and b < 0:
        return -PI / 2

    else:
        return 0


def polar(c):

    a = c[0]
    b = c[1]

    r = (a**2 + b**2)**0.5
    theta = atan2(b, a)

    return (r, theta)


print("Forma polar:", polar((1,0)))


# 8. Cálculo de la fase de un número complejo

PI = 3.141592653589793


def arctan(x):
    resultado = 0

    for n in range(20):
        termino = ((-1)**n) * (x**(2*n + 1)) / (2*n + 1)
        resultado = resultado + termino

    return resultado


def atan2(b, a):

    if a > 0:
        return arctan(b / a)

    elif a < 0 and b >= 0:
        return arctan(b / a) + PI

    elif a < 0 and b < 0:
        return arctan(b / a) - PI

    elif a == 0 and b > 0:
        return PI / 2

    elif a == 0 and b < 0:
        return -PI / 2

    else:
        return 0


def fase(c):

    a = c[0]
    b = c[1]

    theta = atan2(b, a)

    return theta


print("Fase del número complejo:", fase((1, 0)))