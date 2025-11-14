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
        print(f"\n{'='*50}")
        print(f"📋 GASTOS EN {nombre_categoria.upper()}")
        print(f"{'='*50}")
        total = 0
        for i, (concepto, monto) in enumerate(categoria_dict.items(), 1):
            print(f"{i}. {concepto.capitalize()}: ${monto:.2f}")
            total += monto
        print(f"{'-'*50}")
        print(f"{'TOTAL:':<30} ${total:.2f}")
        print(f"{'='*50}\n")

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
    
    try:
        indice = int(input("\nDigite el número del gasto a modificar: ")) - 1
        if 0 <= indice < len(conceptos):
            concepto_viejo = conceptos[indice]
            print(f"\nModificando: {concepto_viejo} (${categoria_dict[concepto_viejo]:.2f})")
            
            nuevo_concepto = input("Ingrese el nuevo concepto (Enter para mantener): ").strip()
            nuevo_monto = input("Ingrese el nuevo monto (Enter para mantener): $").strip()
            
            if nuevo_concepto:
                categoria_dict[nuevo_concepto] = categoria_dict.pop(concepto_viejo)
                concepto_viejo = nuevo_concepto
            
            if nuevo_monto:
                categoria_dict[concepto_viejo] = float(nuevo_monto)
            
            print(f"✅ Gasto modificado exitosamente.")
        else:
            print("⚠️  Número inválido.")
    except (ValueError, IndexError):
        print("⚠️  Entrada inválida.")

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