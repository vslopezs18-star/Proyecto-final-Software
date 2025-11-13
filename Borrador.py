#Crear una aplicacion que se centre en la organizacion de gastos a traves del sistema 50-30-20.
#•	50% para necesidades esenciales, como vivienda, alimentación y transporte.
#•	30% para deseos o gastos personales, como entretenimiento o compras no esenciales.
#•	20% para ahorro o pago de deudas.

#Paso numero uno: Preguntarle al cliente/usuario, la cantidad de dinera que el posee con una función
#Paso numero dos: Dividir esos gastos en el sistema
#Paso numero tres: Definir en que distribuira exactamente su dinero en cada seccion 

def bienvenida():
    """Esta función da la bienvenida a la app"""
    print("Bienvenido/a a PapoiMoney")
    print("Descubre la forma más inteligente y sencilla de manejar tu dinero con el sistema 50-30-20:") 
    print(f"\t50% para Necesidades Esenciales (vivienda, comida, transporte.") 
    print(f"\t30% para Deseos (entretenimiento, gastos personales.")
    print(f"\t20% para Ahorro.")
    print(f"\tAutomatiza tu presupuesto, evita gastos innecesarios y toma el control de tu bienestar financiero. ¡Comencemos a planificar!")

bienvenida()

Sueldo = float(input("Para empezar ingrese la cantidad de dinero que posee: $"))

Necesidades = []
Deseos = []
Ahorro = []

presupuesto_necesidades = Sueldo * 0.50
presupuesto_deseos = Sueldo * 0.30
presupuesto_ahorro = Sueldo * 0.20

""""print(f"\nTu presupuesto se distribuye así:")
print(f"Necesidades: ${presupuesto_necesidades:.2f}")
print(f"Deseos: ${presupuesto_deseos:.2f}")
print(f"Ahorro: ${presupuesto_ahorro:.2f}\n")"""

distribucion=True
while distribucion is True:
    sección = int(input("Secciones: \n 1. Necesidades Esenciales (ej. vivienda, comida, transporte), \n 2. Deseos (entretenimiento, gastos personales). \n 3. Ahorro \n 4. Salir \n Digite la sección a la que desea entrar: "))
    if sección == 4:
        distribucion = False
    elif sección == 1:
            elección = (input(" \n a.Agregar categorías \n b.Consular categorías \n c.Modificar categorías \n d. Borrar categorías "))
            if elección == "a":
                categoría = input("Ingrese la categoría a agregar: ")
                Necesidades.append(categoría)
            elif elección == "b":
                print(Necesidades)
            elif elección == 3:
                if len(Necesidades) == 0:
                    print("Actualmente no hay categorías creadas en Necesidades por el momento.")
            else:
                for v in range(len(Necesidades)):
                    print(f"{[v].capitalize()}: ${[v]:.2f}")= input("Digite el nombre nuevo: ")
                if len(Necesidades) == 0:
                 print("Actualmente no hay categorías en Necesidades")
                else:
                    for v in range(len(Necesidades)):
                        print(f"Actualmente hay {len(Necesidades)} en Necesidades")
        
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