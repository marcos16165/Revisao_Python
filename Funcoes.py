#SOMA

def soma(a, b):
    soma = a + b
    return soma

#DIVISÃO

def divide(a, b):
    if a != 0 and b !=0:
        divide = a / b
        return divide
    else:
        return None

#ÁREA DO TRIÂNGULO

def areaTri(base,altura):
    area = (base*altura) / 2
    return area

#ÁREA DO CÍRCULO

def areaCirc(raio):
    area = 3.1415 * (raio**2)
    return area

#SENO

def seno(catops, hipotenusa):
    seno = catops / hipotenusa
    return seno

#POTÊNCIA

def potencia(a,b):
    potencia = a ** b
    return potencia
