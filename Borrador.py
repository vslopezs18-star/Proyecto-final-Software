#Crear una aplicacion que se centre en la organizacion de gastos a traves del sistema 50-30-20.
#•	50% para necesidades esenciales, como vivienda, alimentación y transporte.
#•	30% para deseos o gastos personales, como entretenimiento o compras no esenciales.
#•	20% para ahorro o pago de deudas.

#Paso numero uno: Preguntarle al cliente/usuario, la cantidad de dinera que el posee 
#Paso numero dos: Dividir esos gastos en el sistema
#Paso numero tres: Definir en que distribuira exactamente su dinero en cada seccion 

Sueldo=float(input("Ingrese la cantidad de dinero que usted posee: "))
print("La distribucion esta dada por: \n 50% para necesidades esenciales, como vivienda, alimentación y transporte. \n 30% para deseos o gastos personales, como entretenimiento o compras no esenciales. \n 20% para ahorro o pago de deudas.")

distribucion=True
while distribucion is True:
    eleccion=int(input("Digite la opcion a elegir (1-3): "))
    if eleccion == 1:
        print()