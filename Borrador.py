#Crear una aplicacion que se centre en la organizacion de gastos a traves del sistema 50-30-20.
#•	50% para necesidades esenciales, como vivienda, alimentación y transporte.
#•	30% para deseos o gastos personales, como entretenimiento o compras no esenciales.
#•	20% para ahorro o pago de deudas.

#Paso numero uno: Preguntarle al cliente/usuario, la cantidad de dinera que el posee 
#Paso numero dos: Dividir esos gastos en el sistema
#Paso numero tres: Definir en que distribuira exactamente su dinero en cada seccion 

print("Bienvenido/a a PapoiMoney \n Descubre la forma más inteligente y sencilla de manejar tu dinero con el sistema 50-30-20: \n 50% para Necesidades Esenciales (vivienda, comida, transporte). \n 30% para Deseos (entretenimiento, gastos personales). \n 20% para Ahorro o Deudas. \n Automatiza tu presupuesto, evita gastos innecesarios y toma el control de tu bienestar financiero. ¡Comencemos a planificar!")

Sueldo = 0
if Sueldo>0:
        Sueldo.append(float(input("Para empezar ingrese la cantidad de dinero que posee: ")))
        print(Sueldo)
        
"""print("La distribucion esta dada por: \n 50% para necesidades esenciales, como vivienda, alimentación y transporte. \n 30% para deseos o gastos personales, como entretenimiento o compras no esenciales. \n 20% para ahorro o pago de deudas.")

distribucion=True
while distribucion is True:
    eleccion=int(input("Digite la opcion a elegir (1-3): "))
    if eleccion == 1:
        print()"""
        
"""while menu_iniciado: 
    opción = int(input("1.Agregar, 2.Consular, 3.Modificar, 4. Borrar, 5. Salir"))
    if opción == 5:
      menu_iniciado = False # Aquí le decimos que si la opción es 5 entonces el menú se cierra
    elif opción == 1:
        alumnos.append(input("Digite el nombre del alumno: "))
        print(alumnos)
    elif opción == 2:
      for a in alumnos: # Este es cuando suponemos que ya tenemos una lista completa vamos a decir que para cada a en alumnos va a ser primero uno, luego dos y así
          print(a)
    elif opción == 3:
        indice = int(input("Digite el numero del alumno (1-3): "))
        nuevo = input("Digite el nombre nuevo: ")
        alumnos[indice-1] = nuevo
    elif opción == 4:
        indice = int(input("Digite el número del alumno (1-3) a popear: "))
        alumno_borrado = alumnos.pop(indice-1) # Aquí estamos guardando al que borramos
        print(f"Hemos borrado a : {alumno_borrado}")
    else:
        print("Esa opción no es válida.")
print("Gracias por usar nuestro sistema.")"""