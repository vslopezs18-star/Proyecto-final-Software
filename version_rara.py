# PapoiMoney - Aplicación de gestión de presupuesto con sistema 50-30-20
# Sistema: 50% Necesidades, 30% Deseos, 20% Ahorro

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

def mostrar_presupuesto(sueldo, necesidades_dict, deseos_dict, ahorro_dict):
    """Muestra el resumen del presupuesto y gastos actuales"""
    presupuesto_necesidades = sueldo * 0.50
    presupuesto_deseos = sueldo * 0.30
    presupuesto_ahorro = sueldo * 0.20
    
    # Calcular totales gastados
    total_necesidades = sum(necesidades_dict.values())
    total_deseos = sum(deseos_dict.values())
    total_ahorro = sum(ahorro_dict.values())
    
    print("\n")
    print(" " * 25 + "RESUMEN DE PRESUPUESTO")
    print(f"\n💵 Ingreso Total: ${sueldo:.2f}\n")
    
    print(f"{'Categoría':<25} {'Presupuesto':<15} {'Gastado':<15} {'Disponible':<15}")

    print(f"{'Necesidades (50%)':<25} ${presupuesto_necesidades:<14.2f} ${total_necesidades:<14.2f} ${presupuesto_necesidades - total_necesidades:<14.2f}")
    print(f"{'Deseos (30%)':<25} ${presupuesto_deseos:<14.2f} ${total_deseos:<14.2f} ${presupuesto_deseos - total_deseos:<14.2f}")
    print(f"{'Ahorro (20%)':<25} ${presupuesto_ahorro:<14.2f} ${total_ahorro:<14.2f} ${presupuesto_ahorro - total_ahorro:<14.2f}")
    print("\n")

def agregar_gasto(categoria_dict, nombre_categoria, presupuesto_max, total_gastado):
    """Agrega un gasto a una categoría específica"""
    concepto = input(f"\nIngrese el concepto del gasto en {nombre_categoria}: ").strip()
    
    # Validar el monto con bucle while
    monto_valido = False
    
    while monto_valido == False:
        monto_texto = input(f"Ingrese el monto para '{concepto}': $").strip()
        
        # Verificar si el texto está vacío
        if monto_texto == "":
            print("⚠️  Por favor ingrese un monto válido.")
        else:
            # Verificar caracteres válidos
            es_numero = True
            tiene_punto = False
            posicion = 0
            
            while posicion < len(monto_texto) and es_numero == True:
                caracter = monto_texto[posicion]
                
                # Permitir signo negativo solo al inicio
                if caracter == '-' and posicion == 0:
                    # No pasa nada, porque es válido
                    es_numero = True
                # Permitir solo un punto decimal
                elif caracter == '.':
                    if tiene_punto == True:
                        es_numero = False
                    else:
                        tiene_punto = True
                # Verificamos si es dígito
                elif caracter in '0123456789':
                    # Es válido
                    es_numero = True
                else:
                    es_numero = False
                
                posicion = posicion + 1 
            
            if es_numero == True:
                monto = float(monto_texto)
                monto_valido = True
            else:
                print("⚠️  Por favor ingrese un monto válido.")
    
    # Validar que el monto sea mayor a 0
    if monto <= 0:
        print("⚠️  El monto debe ser mayor a 0.")
        return total_gastado
    
    nuevo_total = total_gastado + monto
    
    if nuevo_total > presupuesto_max:
        print(f"\n⚠️  ADVERTENCIA: Este gasto excede tu presupuesto de {nombre_categoria}!")
        print(f"   Presupuesto: ${presupuesto_max:.2f}")
        print(f"   Total gastado: ${nuevo_total:.2f}")
        print(f"   Exceso: ${nuevo_total - presupuesto_max:.2f}")
        
        confirmacion = input("\n¿Deseas agregar este gasto de todas formas? (s/n): ").lower()
        if confirmacion != 's':
            print("✅ Gasto no agregado.")
            return total_gastado
    
    categoria_dict[concepto] = monto
    print(f"✅ Gasto '{concepto}' de ${monto:.2f} agregado exitosamente a {nombre_categoria}.")
    return nuevo_total

def consultar_gastos(categoria_dict, nombre_categoria):
    """Consulta y muestra todos los gastos de una categoría"""
    if len(categoria_dict) == 0:
        print(f"\n📋 No hay gastos registrados en {nombre_categoria}.")
    else:
        print("\n")
        print(f"📋 GASTOS EN {nombre_categoria.upper()}")
        print("\n")
        total = 0
        for i, (concepto, monto) in enumerate(categoria_dict.items(), 1):
            print(f"{i}. {concepto.capitalize()}: ${monto:.2f}")
            total += monto
        print("\n")
        print(f"{"TOTAL:"} ${total:.2f}")
        print("\n")

def modificar_gasto(categoria_dict, nombre_categoria):
    """Modifica un gasto existente"""
    if len(categoria_dict) == 0:
        print(f"\n⚠️  No hay gastos en {nombre_categoria} para modificar.")
        return 
    
    consultar_gastos(categoria_dict, nombre_categoria)
    
    conceptos = list(categoria_dict.keys())
    print("Conceptos disponibles:")
    for i, concepto in enumerate(conceptos, 1):
        print(f"{i}. {concepto}")
    
    # Validamos el índice
    indice_valido = False
    
    while indice_valido == False:
        indice_texto = input("\nDigite el número del gasto a modificar: ").strip()
        
        # Verificamos si está vacío
        if indice_texto == "":
            print("⚠️  Entrada inválida.")
        else:
            # Verificamos si todos los caracteres son dígitos
            es_numero = True
            posicion = 0
            
            while posicion < len(indice_texto) and es_numero == True:
                caracter = indice_texto[posicion]
                
                if caracter not in '0123456789':
                    es_numero = False
                
                posicion = posicion + 1
            
            if es_numero == True:
                indice = int(indice_texto) - 1
                
                # Verificamos si el índice está en el rango válido
                if 0 <= indice < len(conceptos):
                    indice_valido = True
                else:
                    print("⚠️  Número inválido.")
            else:
                print("⚠️  Entrada inválida.")
    
    # Ahora modificamos el gasto
    concepto_viejo = conceptos[indice]
    print(f"\nPor lo tanto el {concepto_viejo} pasa a ser ${categoria_dict[concepto_viejo]:.2f}")
    
    nuevo_concepto = input("Ingrese el nuevo concepto (Enter para mantener): ").strip()
    nuevo_monto = input("Ingrese el nuevo monto (Enter para mantener): $").strip()
    
    # Modificamos el concepto si el usuario escribió algo
    if nuevo_concepto != "":
        categoria_dict[nuevo_concepto] = categoria_dict.pop(concepto_viejo)
        concepto_viejo = nuevo_concepto
    
    # Modificar el monto si el usuario escribió algo
    if nuevo_monto != "":
        # Corroboramos que el monto sea un número válido
        monto_valido = False
        
        while monto_valido == False:
            # Contamos cuántos puntos tiene
            cantidad_puntos = 0
            pos_punto = 0
            
            while pos_punto < len(nuevo_monto):
                if nuevo_monto[pos_punto] == '.':
                    cantidad_puntos = cantidad_puntos + 1
                pos_punto = pos_punto + 1
            
            # Verificamos si tiene más de un punto
            if cantidad_puntos > 1:
                nuevo_monto = input("⚠️  Monto inválido. Ingrese el nuevo monto: $").strip()
            else:
                # Convertimos el texto a lista para poder usar remove
                lista_caracteres = list(nuevo_monto)
                
                # Quitamos el punto en dado caso existe
                if '.' in lista_caracteres:
                    lista_caracteres.remove('.')
                
                # Quitamos el signo negativo si está al inicio
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
                        categoria_dict[concepto_viejo] = float(nuevo_monto)
                        monto_valido = True
                    else:
                        nuevo_monto = input("⚠️  Monto inválido. Ingrese el nuevo monto: $").strip()
                else:
                    nuevo_monto = input("⚠️  Monto inválido. Ingrese el nuevo monto: $").strip()
    
    print(f"✅ Gasto modificado exitosamente.")

def borrar_gasto(categoria_dict, nombre_categoria):
    """Borra un gasto de una categoría"""
    if len(categoria_dict) == 0:
        print(f"\n⚠️  No hay gastos en {nombre_categoria} para borrar.")
        return
    
    consultar_gastos(categoria_dict, nombre_categoria)
    
    conceptos = list(categoria_dict.keys())
    try:
        indice = int(input("\nDigite el número del gasto a borrar: ")) - 1
        if 0 <= indice < len(conceptos):
            concepto = conceptos[indice]
            monto = categoria_dict.pop(concepto)
            print(f"✅ Gasto '{concepto}' de ${monto:.2f} eliminado exitosamente.")
        else:
            print("⚠️  Número inválido.")
    except (ValueError, IndexError):
        print("⚠️  Entrada inválida.")

def menu_categoria(nombre_categoria, categoria_dict, sueldo):
    """Menú de operaciones para cada categoría"""
    porcentajes = {"Necesidades": 0.50, "Deseos": 0.30, "Ahorro": 0.20}
    presupuesto_max = sueldo * porcentajes[nombre_categoria]
    
    while True:
        total_gastado = sum(categoria_dict.values())
        disponible = presupuesto_max - total_gastado
        
        print(f"\n{'='*60}")
        print(f"📂 {nombre_categoria.upper()} - Presupuesto: ${presupuesto_max:.2f}")
        print(f"   Gastado: ${total_gastado:.2f} | Disponible: ${disponible:.2f}")
        print(f"{'='*60}")
        print("\nOpciones:")
        print("  a. Agregar gasto")
        print("  b. Consultar gastos")
        print("  c. Modificar gasto")
        print("  d. Borrar gasto")
        print("  e. Volver al menú principal")
        
        eleccion = input("\nSeleccione una opción: ").lower().strip()
        
        if eleccion == "e":
            break
        elif eleccion == "a":
            total_gastado = agregar_gasto(categoria_dict, nombre_categoria, presupuesto_max, total_gastado)
        elif eleccion == "b":
            consultar_gastos(categoria_dict, nombre_categoria)
        elif eleccion == "c":
            modificar_gasto(categoria_dict, nombre_categoria)
        elif eleccion == "d":
            borrar_gasto(categoria_dict, nombre_categoria)
        else:
            print("⚠️  Opción no válida.")

def main():
    """Función principal de la aplicación"""
    bienvenida()
    
    # Solicitar el sueldo
    while True:
        try:
            sueldo = float(input("Para empezar ingrese la cantidad de dinero que posee: $"))
            if sueldo <= 0:
                print("⚠️  Por favor ingrese una cantidad mayor a 0.")
                continue
            break
        except ValueError:
            print("⚠️  Por favor ingrese un monto válido.")
    
    # Diccionarios para almacenar gastos (concepto: monto)
    necesidades = {}
    deseos = {}
    ahorro = {}
    
    # Menú principal
    while True:
        mostrar_presupuesto(sueldo, necesidades, deseos, ahorro)
        
        print("MENÚ PRINCIPAL")
        print("=" * 70)
        print("1. 💰 Necesidades Esenciales (vivienda, comida, transporte)")
        print("2. 🎯 Deseos (entretenimiento, gastos personales)")
        print("3. 🏦 Ahorro")
        print("4. 📊 Ver resumen completo")
        print("5. 🚪 Salir")
        print("=" * 70)
        
        try:
            seccion = int(input("\nDigite la sección a la que desea entrar: "))
            
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
                continue  # El resumen ya se muestra al inicio del bucle
            else:
                print("⚠️  Opción no válida. Por favor seleccione 1-5.")
        except ValueError:
            print("⚠️  Por favor ingrese un número válido.")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()