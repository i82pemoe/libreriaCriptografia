# -*- coding: utf-8 -*-
#!/usr/bin/env python
""" Modulo con las clases de cifrado"""
import funciones
from fractions import *
import random
class Cesar:
	"""
	Cifrado Cesar
	"""
	def __init__(self):
		"""
		Constructor de clase
		"""
		self.k = 3
		self.texto = ""
		self.abc = funciones.abecedario()

	def setK(self,k):
		"""
		Modificar de k

		@type k: entero
		@param k: valor de la clave
		"""
		self.k=k

	def setTexto(self,texto):
		"""
		Modificador del texto

		@type texto: cadena
		@param texto: texto a cifrar
		"""
		self.texto = texto

	def cifrar(self):
		"""
		Cifrado del texto por el método César

		@rtype: cadena
		@return: texto cifrado
		"""
		mensaje = funciones.letranumero(self.texto)
		cifrado = []
		for i in mensaje:
			aux = i
			cifrado.append((aux+self.k)%len(self.abc))
		textocifrado = funciones.numeroLetra(cifrado)
		return textocifrado

	def descifrar(self):
		"""
		Descifrado del texto por el método César

		@rtype: cadena
		@return: texto descifrado
		"""
		mensaje = funciones.letranumero(self.texto)
		cifrado = []
		for i in mensaje:
			aux = i
			cifrado.append((aux-self.k)%len(self.abc))
		textocifrado = funciones.numeroLetra(cifrado)
		return textocifrado

class Afin:
	"""
	Cifrado Afín
	"""
	def __init__(self):
		"""
		Constructor de clase
		"""
		self.a = 14
		self.d= 7
		self.texto = ""
		self.abc=funciones.abecedario()

	def setA(self,a):
		"""
		Modificador de la clave a

		@type a: entero
		@param a: valor de a
		"""
		self.a = a

	def setD(self,d):
		"""
		Modificador de la clave d

		@type d: entero
		@param d: valor de d
		"""
		self.d = d

	def setTexto(self,texto):
		"""
		Modificar del texto

		@type texto: cadena
		@param texto: cadena a cifrar
		"""
		self.texto = texto

	def cifrar(self):
		"""
		Cifrado del texto por el método afín

		@rtype: cadena
		@return: texto cifrado
		"""
		tam = len (self.abc)
		mcd = gcd(self.a, tam)
		if mcd == 1:
			texto = funciones.letranumero(self.texto)
			cifrado = []
			for i in texto:
				aux = i
				cifrado.append((self.a*aux+self.d)%tam)
			textocifrado = funciones.numeroLetra(cifrado)
			return textocifrado

	def descifrar(self):
		"""
		Descifrado del texto por el método afín

		@rtype: cadena
		@return: texto descifrado
		"""
		tam = len (self.abc)
		mcd, u, v = funciones.egcd(tam, self.a);
		if mcd == 1:
			texto = funciones.letranumero(self.texto)
			v = v%tam
			des = []
			for i in texto:
				aux = i
				des.append((v*(aux-self.d)%tam))
			textodes = funciones.numeroLetra(des)
			return textodes



class Mochila:
	"""
	Cifrado mochila o de Merkle-Hellman
	"""
	def __init__(self):
		"""
		Constructor de la clase
		"""
		self.mochila = [12,64,109,254,455] #privada
		self.m = 986 #privada
		self.w = 503 #publica
		self.public = [120,640,597,568,113] #publica
		self.texto = ""
		self.abc=funciones.abecedario()

	def setMochila(self,mochila):
		"""
		Modificador de la clave mochila

		@type mochila: lista
		@param mochila: valor de la clave mochila
		"""
		self.mochila = mochila

	def setM(self,m):
		"""
		Modificador de la clave m

		@type m: entero
		@param m: valor de la clave m
		"""
		self.m = m

	def setW(self,w):
		"""
		Modificador de la clave w

		@type w: entero
		@param w: valor de la clave w
		"""
		self.w = w

	def setPublic(self,public):
		"""
		Modificador de la clave publica

		@type public: lista
		@param public: valor de la lista publica
		"""
		self.public = public

	def setTexto(self,texto):
		"""
		Modificador del texto a cifrar/descifrar

		@type texto: cadena
		@param texto: texto a cifrar/descifrar
		"""
		self.texto = texto

	def setClaves(self,mochila,m,w,public):
		"""
		Modificador de todas las claves

		@type mochila: cadena
		@param mochila: cadena con los valores de la mochila

		@type m: entero
		@param m: valor de la clave m

		@type w: entero
		@param w: valor de la clave w

		@type public: cadena
		@param public: cadena con los valroes de la clave publica
		"""
		self.setM(m)
		self.setW(w)
		mochila = funciones.cadenaLista(mochila)
		self.setMochila(mochila)
		public = funciones.cadenaLista(public)
		self.setPublic(public)



	def cifrar(self):
		"""
		Cifrado por el método mochila

		@rtype: lista
		@return: lista con los valores del cifrado
		"""
		texto = funciones.numeroBinario(self.texto)
		tam = len(self.public)
		if (len(texto) % tam) !=0:
			i = 0
			while i<=(len(texto) % tam):
				texto = texto + '0'
				i = i+1

		i = 0
		j = 0
		suma = 0
		textocifrado = ''
		aux = []
		while i<len(texto):
			if j == tam:
				j = 0
				suma = 0
			if texto[i]=='1':
				suma = suma+self.public[j]
			if j == tam-1:
				suma = suma%self.m
				aux.append(suma)
			i = i+1
			j = j+1

		i = 0
		while i < len(aux):
			aux[i]=str(aux[i])
			textocifrado += aux[i]
			textocifrado += ','
			i = i+1
		textocifrado = textocifrado[0:len(textocifrado)-1]
		textocifrado = funciones.cadenaLista(textocifrado)
		return textocifrado

	def descifrar(self):
		"""
		Descifrado por el método mochila

		@rtype: cadena
		@return: texto descifrado
		"""
		texto = self.texto
		inv = funciones.modinv(self.w,self.m)
		i = 0
		while i < len(texto):
			texto[i] = (texto[i]*inv)%self.m
			i = i+1

		numeros = self.descifraNumero(texto,self.mochila)
		numeros = funciones.binarioNumero(numeros)
		descifrado = funciones.numeroLetra(numeros)

		return descifrado

	def generarClave(self):
		"""
		Genera las claves aleatoriamente y las modifica en la clase
		"""
		tam = 5
		aleatorio = random.randrange(1,100)
		mochila = [aleatorio]
		suma = aleatorio
		for i in range(tam-1):
			suma = suma+mochila[i]
			numero = suma + random.randrange(1,100)
			mochila.append(numero)

		m = mochila[tam-1]*2 + random.randrange(1,200)
		w = funciones.generarPrimos(1)
		b = []
		for i in range(tam):
			numero = (w*mochila[i])%m
			b.append(numero)

		self.setM(m)
		self.setW(w)
		self.setPublic(b)
		self.setMochila(mochila)

	def descifraNumero (self,texto, mochila):
	   
	    """
		Consigue la cadena de binarios para descifrar

		@rtype: cadena
		@return: cadena con los numeros binarios para descifrar el texto
	    """
	    i = 0
	    numero=''
	    while i < len(texto):
	        j=len(mochila)-1
	        aux=''
	        res = texto[i]
	        while j >=0:
	            if mochila[j] <= res:
	                res = res-mochila[j]
	                aux = '1'+aux
	            else:
	                aux = '0'+aux
	            j=j-1
	        numero = numero+aux
	        i=i+1

	    return numero


class RSA:
	"""
	Cifrado RSA
	"""
	def __init__(self):
		"""
		Constructor de clase
		"""
		self.n = 1711 #privada y publica
		self.e = 961 #publica
		self.d = 921 #privada
		self.texto = ""

	def setN(self,n):
		"""
		Modificador de la clave n

		@type n: entero
		@param n: valor de la clave n
		"""
		self.n = n

	def setE(self,e):
		"""
		Modificador de la clave e

		@type e: entero
		@param e: valor de la clave e
		"""
		self.e = e

	def setD(self,d):
		"""
		Modificador de la clave d

		@type d: entero
		@param d: valor de la clave d
		"""
		self.d = d

	def setTexto(self,texto):
		"""
		Modificador del texto  a cifrar

		@type texto: cadena
		@param texto: texto a descifrar
		"""
		self.texto = texto

	def cifrar(self,e,n,texto):
		"""
		Cifrado por el método RSA

		@type e: entero
		@param e: valor de e

		@type n: entero
		@param n: valor de la clave n

		@type texto: cadena
		@param texto: texto a cifrar

		@rtype: lista
		@return: valores del texto cifrado
		"""
		blo = funciones.prepa_num_cifrar(n,texto)
		cifrado = []
		for i in blo:
			cifrado.append(funciones.potencia(i,e,n))

		return cifrado

	def descifrar(self,d,n,cifrado):
		"""
		Descifrado por el método RSA

		@type d: entero
		@param d: clave d

		@type n: entero
		@param n: clave n

		@type cifrado: lista
		@param cifrado: lista con los valores a descifrar

		@rtype: cadena
		@return: texto descifrado
		"""
		descifro = []
		for i in cifrado:
			descifro.append(funciones.potencia(i,d,n))
		descifrado = funciones.num_letra(n,descifro)
		return descifrado

	def generarFirma(self, texto):
		"""
		Genera una firma digital por RSA

		@type texto: cadena
		@param texto: texto con el que generar la firma

		@rtype: entero
		@return: valor de la firma digital
		"""
		n = self.n
		M = funciones.hash(self.texto, n)
		S = funciones.potencia(M,self.d,n)
		return S

	def generarClave(self):
		"""
		Generacion de claves para RSA
		"""
		p = funciones.generarPrimos(2)
		q = funciones.generarPrimos(2)
		while p == q:
			q = funciones.generarPrimos(2)

		n = p*q
		phi = (p-1)*(q-1)
		e = random.randrange(50,phi-1)
		[gcd,u,v] = funciones.egcd(phi,e)

		while True:
			e = random.randrange(1,phi-1)
			[gcd,u,v] = funciones.egcd(phi,e)
			if gcd == 1:
				break

		d = funciones.modinv(e,phi)
		self.setN(n)
		self.setD(d)
		self.setE(e)
