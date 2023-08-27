nombre = "Abner Ernesto Izaguirre Corrales"
edad = 18
cohorte = 45

print(f"Mi nombre es, {nombre}",f"Tengo {edad} años",f"Y pertenezco a la cohorte {cohorte}")

#En Python, los enteros (integers) y los números de punto flotante (floats) tienen límites máximos y mínimos:
#En sistemas de 32 bits, los enteros suelen tener un límite de -2,147,483,648 a 2,147,483,647
#En sistemas de 64 bits, los enteros tienen limites mucho mayores, alrededor de -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807
#Los números de ounto flotante en python tienen un límite típico de +1.8 x 10^308, pero pueden perder precisión en cálculos con números 
#muy grandes o muy cercanos a cero.

print("A continuacion veremos la solucion de la suma de los primeros 100 números pares")
inicio = 0
final = 100
suma = 0
while inicio <= final:
    if inicio % 2 == 0:
        #print(inicio)
        suma= suma+inicio
        inicio+=1
        print("Suma de las primeras 100 n pares es:",suma)