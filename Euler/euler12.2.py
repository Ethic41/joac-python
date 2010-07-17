from math import *

def triangleGenerator():
	a = 0
	b = 0
	while True:
		a += 1
		b += a
		yield a

def getdivisores(numero):
	counter = 2
	#divisor = 2
	for divisor in xrange(2, int(sqrt(numero)+1)):
		if not numero%divisor:
			counter += 2
	return counter

divisores = 0	
numero = triangleGenerator()
a = 0
b = 0
while divisores < 500:
	b += 1
	a += b
	divisores = getdivisores(a)
	#print a, divisores
	if not b%1000:
		print a, divisores
print "Numero: %d \t Iteraciones: %d \t Divisores: %d" % (a, b, divisores)		
