# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""Modulo con las funciones generales"""
import random

def letranumero (texto):
    """
    Convierte una letra a su numero correposdiente

    @type texto: cadena
    @param texto: cadena a convertir a numeros

    @rtype: lista
    @return: lista de numeros
    """
    alfabeto = abecedario()
    texto = texto.lower()
    i=0
    j=0
    numeros=[]

    while i<len(texto):
        while j < len(alfabeto):
            if texto[i]==alfabeto[j]:
                numeros.append(j)
            j=j+1
        j=0
        i=i+1

    return numeros

def numeroLetra(num):
    '''
    Convierte un numero a su letra correspondiente

    @type num: lista
    @param num: lista de numeros a convertir

    @rtype: cadena
    @return: cadena de los numeros convertidos a letras
    '''
    alfabeto = abecedario()
    i=0
    texto=''
    while i < len(num):
        aux = num[i]
        texto = texto + alfabeto[aux]
        i=i+1
    return texto

def abecedario ():
    """
    Alfabeto a usar

    @rtype: cadena
    @return: alfabeto a usar
    """
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    return alfabeto

def egcd(a, b):
    """
    MCD de dos numeros

    @type a: entero
    @param a: primer elemento para calcular el mcd

    @type b: entero
    @param b: segundo elemento para calcular el mcd

    @rtype: lista
    @return: Maximo común divisor y los coeficientes de Bézout
    """
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m): #inverso de a modulo m
    """
    Calcula el inverso de un numero modulo m

    @type a: entero
    @param a: numero a calcular el inverso

    @type m: entero
    @param m: modulo en el que calcular el inverso

    @rtype: entero
    @return: inverso de a modulo m
    """
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


def numeroBinario(texto):
    """
    Convierte una cadena en su respectivos numeros binarios de 5 bits

    @type texto: cadena
    @param texto: texto a convertir

    @rtype: cadena
    @return: cadena de numeros de 5 bits
    """

    numeros = letranumero(texto)

    textob = ''
    i=0

    while i < len(numeros):
        textob += format(numeros[i],'#07b')
        i=i+1
    textob = textob.replace("0b","")
    return textob

def binarioNumero(texto):
    """
    Convierte una cadena de numeros binarios de 5 bits a numeros decimales

    @type texto: cadena
    @param texto: cadena de numeros binarios de 5 bits

    @rtype: lista
    @return: cadena numeros decimales
    """
    numeros = []
    i=5
    aux = texto[0:5]
    while i<len(texto):
        if i%5==0:
            numeros.append(aux)
            aux=""
            aux = aux + texto[i]
        else:
            aux = aux + texto[i]
        i=i+1
    aux = texto[len(texto)-5:len(texto)]
    numeros.append(aux)
    i=0
    decimal = []
    while i<len(numeros):
        decimal.append(int(numeros[i],2))
        i=i+1
    return decimal


def generarPrimos(n):
    """
    Genera un primo aleatorio

    @type n: entero
    @param n: escoge entre numeros primos de 0 a 5000 o de 0 a 150

    @rtype: entero
    @return: numero primo
    """
    if n==1:
        primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, 4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999]
        w = primos[random.randrange(0,len(primos)-1)]
        return w

    if n == 2:
        primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
        w = primos[random.randrange(0,len(primos)-1)]
        return w



def listacadena(lista):
    """
    Convierte una lista en cadena

    @type lista: lista
    @param lista: lista a convertir

    @rtype: cadena
    @return: lista convertida a cadena
    """
    cad = ''
    for i in lsita:
        cad = cad + str(i) + ','

    cad = cad.rstrip(cad[len(cad)-1])
    return cad

def cadenaLista(cadena):
    """
    Convierte una cadena de numeros separados por ',' en lista

    @type cadena: cadena
    @param cadena: cadena a convertir

    @rtype: lista
    @return: cadena convertida a lista
    """

    cl = cadena.split(',') #lista de cadena
    l=[] #lista de enteros
    i=0
    for i in cl:
        l.append(int(i))

    return l

def letraNumero2D(texto):
    """
    Convierte la cadena en una cadena de numeros de dos cifras

    @type texto: cadena
    @param texto: cadena a convertir en numeros

    @rtype: cadena
    @return: cadena de numeros de dos cifras
    """
    nme = letranumero(texto);
    numero = ''
    for i in nme:
        aux = str(i)
        if len(aux) == 1:
            numero = numero + '0'+aux
        else:
            numero = numero + aux
    return numero

def dec2bin(a):
    """
    Convierte un entero a binario

    @type a: entero
    @param a: numero a convertir

    @rtype: cadena
    @return: numero binario
    """
    a = bin(a)
    a = a.replace("0b","")
    return a

def potencia(c,d,n):
    #potencia en modulo n
    """
    Potencia modulo n

    @type c: entero
    @param c: numero a elevar

    @type d: entero
    @param d: potencia a la que elevar c

    @type n: entero
    @param n: modulo

    @rtype: entero
    @return: c elevado a d modulo n
    """
    pote = 1
    bin = dec2bin(d)
    v = [c%n]

    i = 1
    while i < len(bin):
        aux = pow(v[i-1],2)%n
        v.append(aux)
        i = i+1
    v = v[::-1]

    i=0
    while i < len(v):
        if bin[i]=='1':
            pote = (pote * v[i])%n
        i=i+1
    return pote

def reshape(cadena, n):
    """
    Divide una cadena en una lista de elementos de longitud n

    @type cadena: cadena
    @param cadena: cadena a dividir

    @type n: entero
    @param n: longitud de los elementos de la lista

    @rtype: lista
    @return: lista con la cadena dividida
    """
    texto = cadena
    if n == -1:
        n = len(cadena)%n
    if len(texto)%n != 0:
        print 'no se puede llevar a cabo la funcion reshape'
    else:
        i = 0
        j = 0
        v = []
        vuelta = n
        vuelta1 = vuelta
        tam = len(cadena)/n
        tam1 = tam
        aux = ''

        while i < tam:
            aux = ''
            while j < vuelta:
                aux = aux + texto[j]

                j=j+1

            vuelta = vuelta+vuelta1

            v.append (aux)

            i=i+1
        return v

def prepa_num_cifrar(n, texto):
    """
    Prepara el texto para poder cifrarlo por RSA

    @type n: entero
    @param n: clave n

    @type texto: cadena
    @param texto: texto a cifrar

    @rtype: lista
    @return: lista con los numeros preparados para cifrar
    """
    numerico = len(str(n))-1
    doble = letraNumero2D(texto)

    if len(doble)%numerico != 0:
        relleno = numerico - (len(doble)%numerico)
        while relleno > 1:
            doble = doble + '30'
            relleno = relleno - 2
        if relleno == 1:
            doble = doble + '0'

    bloque = reshape(doble,numerico)

    blo = []
    for i in bloque:
        blo.append(int(i))
    return blo

def num_letra (n,cifrado):
    """
    descifra el vector para descifrarlo por RSA

    @type n: entero
    @param n: clave  n

    @type cifrado: lista
    @param cifrado: lista de numeros a descifrar

    @rtype: cadena
    @return: texto descifrado
    """
    numerico = len(str(n))-1
    doble = ''

    for i in cifrado:
        s = str(i)
        mas = numerico - len(s)
        if mas != 0:
            j = 0
            while j<mas:
                s = '0'+ s
                j = j+1
            doble = doble + s
        else:
            doble = doble + str(i)

    if len(doble) % 2 != 0:
        doble = doble[0:len(doble)-1]

    doble = reshape(doble,2)
    intdoble = []
    for i in doble:
        intdoble.append(int(i))

    cont = 0
    i = 0
    aux = 0
    while i < len(intdoble):
        if intdoble[i]==30:
            i = len(intdoble)
            aux = 1
            cont = cont + 1
        i = i+1
    i = 0

    if aux == 1 :
        while i<cont:
            intdoble.remove(30)
            i=i+1

    desci = numeroLetra(intdoble)

    return desci



def hash(s, M):
    """
    Funcion Hash

    @type s: cadena
    @param s: cadena con la que realizar el hash

    @type M: entero
    @param M: modulo de la funcion

    @rtype: entero
    @return: resumen del mensaje
    """

    sum = 0
    mult = 1
    j = 0
    for i in s:
        if j == 4:
            mult = 1
        sum = sum + (ord(i)*mult)
        mult = mult*50
        j = j+1

    return abs(sum)%M
