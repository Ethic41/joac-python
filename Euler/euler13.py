file = open('cienNumeros.txt', 'r')
listado = file.readlines()
file.close()
listado = [int(a[0:50]) for a in listado]
total = 0
for numero in listado: 
	total += numero
cadena=str(total)
print cadena[0:10]
	
