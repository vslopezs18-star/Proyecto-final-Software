from submenú import bienvenida, menu_categoria
from funciones import mostrar_presupuesto

# PapoiMoney - Nuestra aplicación es de gestión de presupuesto con sistema 50-30-20
# Sistema: 50% Necesidades, 30% Deseos, 20% Ahorro

def main():
    """Función principal de la aplicación"""
    bienvenida()
    
    # Solicitamos el sueldo
    sueldo_valido = False
    
    while sueldo_valido == False:
        sueldo_texto = input("Para empezar ingrese la cantidad de dinero que posee: $").strip()
        
        # Verificamos si está vacío
        if sueldo_texto == "":
            print("⚠️  Por favor ingrese un monto válido. (Oh poop)")
        else:
            # Contamos cuántos puntos tiene
            cantidad_puntos = 0
            pos_punto = 0
            
            while pos_punto < len(sueldo_texto):
                if sueldo_texto[pos_punto] == '.':
                    cantidad_puntos = cantidad_puntos + 1
                pos_punto = pos_punto + 1
            
            # Verificamos si tiene más de un punto
            if cantidad_puntos > 1:
                print("⚠️  Por favor ingrese un monto válido. (Oh poop)")
            else:
                # Convertir a lista para que usemos remove
                lista_caracteres = list(sueldo_texto)
                
                # Se quita el punto si existe
                if '.' in lista_caracteres:
                    lista_caracteres.remove('.')
                
                # Quitar el signo negativo si está al inicio
                if len(lista_caracteres) > 0 and lista_caracteres[0] == '-':
                    lista_caracteres.remove('-')
                
                # Verificamos que todos sean dígitos
                if len(lista_caracteres) > 0:
                    todos_digitos = True
                    pos = 0
                    
                    while pos < len(lista_caracteres) and todos_digitos == True:
                        if lista_caracteres[pos] not in '0123456789':
                            todos_digitos = False
                        pos = pos + 1
                    
                    if todos_digitos == True:
                        sueldo = float(sueldo_texto)
                        
                        # Vemos que sea mayor a 0
                        if sueldo <= 0:
                            print("⚠️  Por favor ingrese una cantidad mayor a 0.")
                        else:
                            sueldo_valido = True
                    else:
                        print("⚠️  Por favor ingrese un monto válido.  (Oh poop)")
                else:
                    print("⚠️  Por favor ingrese un monto válido.  (Oh poop)")
    
    # Diccionarios para almacenar los gastos
    
    necesidades = {}
    deseos = {}
    ahorro = {}
    
    # Menú principal
    while True:
        mostrar_presupuesto(sueldo, necesidades, deseos, ahorro)
    
        print("MENÚ PRINCIPAL")
        print("\n")
        print("1. 🎯 Necesidades Esenciales (Casa-banana (vivienda), banana (comida), room-room (transporte))")
        print("2. 📋 Deseos (Baboi (entretenimiento), shoppa-shoppa (compras))")
        print("3. 🐷 Ahorro (money-bobo)")
        print("4. 📊 Ver resumen completo (Shorty-banana)")
        print("5. 🚪 Salir (Pado)")
        print("\n")
    
        seccion_valida = False
    
        while seccion_valida == False:
            seccion_texto = input("\nDigite la sección a la que desea entrar: ").strip()
        
        # Verificamos si está vacío
            if seccion_texto == "":
                print("⚠️  Por favor ingrese un número válido. (Oh poop)")
            else:
            # Verificamos si todos los caracteres son dígitos
                es_numero = True
                posicion = 0
            
            while posicion < len(seccion_texto) and es_numero == True:
                if seccion_texto[posicion] not in '0123456789':
                    es_numero = False
                posicion = posicion + 1
            
            if es_numero == True:
                seccion = int(seccion_texto)
                
                # Vemos si está en el rango válido (1-5)
                if 1 <= seccion <= 5:
                    seccion_valida = True
                else:
                    print("⚠️  Opción no válida. Por favor seleccione 1-5. (Stupa! Stupa!)")
            else:
                print("⚠️  Por favor ingrese un número válido. (Oh poop)")
    
    # Luego se ejecuta la opción seleccionada
        if seccion == 5:
                print("\n")
                print("✅ Gracias por usar PapoiMoney. ¡Hasta pronto! (POOPAYE! TULALILOO TI AMOO! BANANA-BYEE)")
                print("\n")
                break
    
        if seccion == 1:
            menu_categoria("Necesidades", necesidades, sueldo)

        if seccion == 2:
            menu_categoria("Deseos", deseos, sueldo)
    
        if seccion == 3:
            menu_categoria("Ahorro", ahorro, sueldo)
    
        if seccion == 4:
        # El resumen ya se muestra al inicio del bucle
        # El bucle volverá al inicio y mostrará el resumen automáticamente
            print("")
# Ejecutamos la aplicación
if __name__ == "__main__":
    main()