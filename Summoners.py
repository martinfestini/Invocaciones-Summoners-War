import sys, random
from math import factorial

#Constantes:

nat3ms, noNat3s = 0.915, 0.085
nat4ms, noNat4ms = 0.08, 0.92
nat5ms, noNat5ms = 0.005, 0.995
nat3Lyd, noNat3Lyd = 0.9365, 0.0635
nat4Lyd, noNat4Lyd = 0.06, 0.94
nat5Lyd, noNat5Lyd = 0.0035, 0.9965
nat4leg = 0.935
nat5leg = 0.065

ms=""
fires=""
winds=""
waters=""
piedritas=""
lyds=""
lydPieces=""
leg=""
legPieces=""
tras=""
ifrits=""
mss=0

def menu():
        
	print("Este programa esta pensado para facilitar el cálculo de probabilidades al momento de invocar.")
	print("La lista de códigos es:")
	print("1 = Cargar datos.")
	print("2 = Simular Invocación.")
	print("3 = Probabilidad de no conseguir ningun 5nat (exceptuando trascendences).")
	print("4 = Probabilidad de conseguir N cantidad de 5nats (exceptuando trascendences).")
	print("5 = Probabilidad de conseguir al menos N cantidad de 5nats (exceptuando trascendences).")
	print("6 = Cantidad de 5 nats mas probable a salir.")
	print("7 = Probabilidad de que salga un cierto mob específico.")
	print("8 = Lista de todas las probabilidades de que salga al menos N cantidad de 5nats desde 0 hasta N (Puede tardar mucho)")
	print("9 = Calcular la cantidad de mana necesaria.")
	print("Enter = Cerrar el programa.")
	codigo =""
	while codigo =="":
		codigo = input("Ingrese el código de la actividad que deséa realizar, para la mayoría hará falta Cargar datos")
	codigo = int(codigo)

	if codigo == 1:
		cargarDatos()
	elif codigo == 2:
		simularInvocacion()
	elif codigo == 3:
		no5nats()
	elif codigo == 4:
		n=int(input("Que cantidad de 5nats?"))
		calcularCantidadFija(n)
	elif codigo == 5:
		alMenosN()
	elif codigo == 6:
		promedio()
	elif codigo == 7:
		mobEspecifico()
	elif codigo == 8:
		probCompleta()
	elif codigo == 9:
		manaTotal()
	else:
		sys.exit()

def cargarDatos():

	global ms
	global fires
	global winds
	global waters
	global piedritas
	global lyds
	global lydPieces
	global leg
	global legPieces
	global tras
	global ifrits
	global mss

	ms=""
	fires=""
	winds=""
	waters=""
	piedritas=""
	lyds=""
	lydpieces=""
	leg=""
	legpieces=""
	tras=""
	ifrits=""
	mss=0
	
	while ms =="":
	        ms = (input("¿Cuantos pergaminos misticos va a invocar?"))                              #MISTICALS
	ms = int(ms)

	while fires=="":
	         fires = (input("¿Cuantos pergaminos de fuego va a invocar"))                           #FUEGOS
	fires = int(fires)

	while winds =="":
		winds = (input("¿Cuantos pergaminos de viento va a invocar?"))                         #VIENTOS
	winds = int(winds)

	while waters=="":
		waters = (input("¿Cuantos pergaminos de agua va a invocar?"))                          #AGUAS
	waters = int(waters)
        
	while piedritas=="":
		piedritas = (input("¿Cuantas piedritas va a invocar"))                                 #PIEDRITAS
	piedritas = int(piedritas)

	restoPiedritas = piedritas%50
	piedritas = piedritas//50

	mss=(ms+winds+waters+fires+piedritas)

	rotacion = []

	if piedritas !=0:
		for x in range(16):
			mobrotacion=input("Ingrese el siguiente bicho de la rotacion (en orden de lectura):")
			rotacion.append(mobrotacion)

	while lyds =="":
		lyds = (input("¿Cuantos lyds va a invocar?"))                                          #LIGHT AND DARKS
	lyds = int(lyds)

	while lydPieces =="":
		lydPieces = (input("¿Cuantas piezas de lyd va a invocar?"))
	lydPieces = int(lydPieces)

	lydPiecesResto = lydPieces%50
	lyds = lyds+(lydPieces//50)

	while leg=="":
		leg = (input("¿Cuantos pergaminos legendarios va a invocar?"))                         #LEGENDARIOS
	leg = int(leg)

	while legPieces =="":
		legPieces = (input("¿Cuantas piezas de pergamino legendario va a invocar?"))
	legPieces = int(legPieces)

	legPiecesResto = legPieces%50
	leg=leg+(legPieces//50)

	while tras =="":
		tras = (input("¿Cuantos pergaminos trascendentes va a invocar?"))                      #TRASCENDENTES
	tras = int(tras)

	while ifrits =="":
		ifrits = (input("¿Cuantos Ifrits va a invocar?"))                                      #IFRITS
	ifrits = int(ifrits)
	
	print(ms,fires,winds,waters,piedritas,lyds,leg,tras,ifrits,rotacion)

	
################## ACA TERMINA CargarDatos ####################################################

def no5nats():
	chance = calcularCantidadFija(0)
	print("la chance es ",chance)
	return chance
	menu()

def manaTotal():
	manaTotal = ms*10000 + fires*10000 + winds*10000 + waters*10000 + piedritas*10000 + lyds*10000 + leg*50000 + tras*100000 + ifrits*1000
	print(manaTotal)
	menu()

def alMenosN():
        n=int(input("¿La chance de al menos cuantos 5 nats quiere calcular?"))
        chance=1
        for x in range(n-1):
            z=calcularCantidadFija(x)
            print(z)
            chance=chance-z
            print(chance)
        print("la chance es",chance)

def calcularCantidadFija(n):
    a1=0
    a2=1
    b1=0
    b2=1
    c1=0
    c2=1
    if n==0:
        a2=noNat5ms**mss
        b2=noNat5Lyd**lyds
        c2=nat4leg**leg
        chance=a2*b2*c2
        return(chance)
        print("la chance es",chance)
    if mss>0:
        a1=(factorial(mss))/(factorial(mss-n)*factorial(n))*(nat5ms**n)*(noNat5ms**(mss-n))
        a2=noNat5ms**mss
    if lyds>0:
        b1=(factorial(lyds))/(factorial(lyds-n)*factorial(n))*(nat5Lyd**n)*(noNat5Lyd**(lyds-n))
        b2=noNat5Lyd**lyds
    if leg>0:
        c1=(factorial(leg))/(factorial(leg-n)*factorial(n))*(nat5leg**n)*(nat4leg**(leg-n))
        c2=nat4leg**leg
    
    chance=(a1*b2*c2)+(a2*b1*c2)+(a2*b2*c1)
    print("la chance es ",chance)
    return chance


#x= cantidad de exitos
#n= numero de intentos
#p= probabilidad de exito
#q= probabilidad de fracaso
 
#P(x)= (n!/(x!(n-x)!))*p^x*q^(n-x)

menucontador = 0

while menucontador==0:
        menu()

