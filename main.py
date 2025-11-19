from 

def bienvenida():
    """Esta función da la bienvenida a la app"""
    print("BIENVENIDO/A A PAPOIMONEY")
    print("\nDescubre la forma más inteligente y sencilla de manejar tu dinero")
    print("con el sistema 50-30-20:\n")
    print("  💰 50% para Necesidades Esenciales (vivienda, comida, transporte)")
    print("  🎯 30% para Deseos (entretenimiento, gastos personales)")
    print("  🏦 20% para Ahorro")
    print("\nAutomatiza tu presupuesto, evita gastos innecesarios y toma el")
    print("control de tu bienestar financiero. ¡Comencemos a planificar!")

def main():
    """Función principal de la aplicación"""
    bienvenida()
    
    # Solicitamos el sueldo
    sueldo_valido = False
    
    while sueldo_valido == False:
        sueldo_texto = input("Para empezar ingrese la cantidad de dinero que posee: $").strip()
        
        # Verificamos si está vacío
        if sueldo_texto == "":
            print("⚠️  Por favor ingrese un monto válido.")
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
                print("⚠️  Por favor ingrese un monto válido.")
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
                        print("⚠️  Por favor ingrese un monto válido.")
                else:
                    print("⚠️  Por favor ingrese un monto válido.")
    
    # Diccionarios para almacenar los gastos
    
    necesidades = {}
    deseos = {}
    ahorro = {}
    
    # Menú principal
    while True:
        mostrar_presupuesto(sueldo, necesidades, deseos, ahorro)
    
        print("MENÚ PRINCIPAL")
        print("\n")
        print("1. 💰 Necesidades Esenciales (vivienda, comida, transporte)")
        print("2. 🎯 Deseos (entretenimiento, gastos personales)")
        print("3. 🏦 Ahorro")
        print("4. 📊 Ver resumen completo")
        print("5. 🚪 Salir")
    
        seccion_valida = False
    
        while seccion_valida == False:
            seccion_texto = input("\nDigite la sección a la que desea entrar: ").strip()
        
        # Verificar si está vacío
        if seccion_texto == "":
            print("⚠️  Por favor ingrese un número válido.")
        else:
            # Verificar si todos los caracteres son dígitos
            es_numero = True
            posicion = 0
            
            while posicion < len(seccion_texto) and es_numero == True:
                caracter = seccion_texto[posicion]
                
                if caracter not in '0123456789':
                    es_numero = False
                
                posicion = posicion + 1
            
            if es_numero == True:
                seccion = int(seccion_texto)
                
                # Verificar si está en el rango válido
                if 1 <= seccion <= 5:
                    seccion_valida = True
                else:
                    print("⚠️  Opción no válida. Por favor seleccione 1-5.")
            else:
                print("⚠️  Por favor ingrese un número válido.")
    
            # Ejecutar la opción elegida
        if seccion == 5:
            print("\n" + "=" * 70)
            print("✅ Gracias por usar PapoiMoney. ¡Hasta pronto!")
            print("=" * 70)
            break
        elif seccion == 1:
            menu_categoria("Necesidades", necesidades, sueldo)
        elif seccion == 2:
            menu_categoria("Deseos", deseos, sueldo)
        elif seccion == 3:
            menu_categoria("Ahorro", ahorro, sueldo)
        elif seccion == 4:
        # Cuando el usuario elige 4, simplemente vuelve al inicio del bucle
        # y mostrar_presupuesto() se ejecuta automáticamente
            print("\n✅ Mostrando resumen completo...")

# Ejecutamos la aplicación
if __name__ == "__main__":
    main()