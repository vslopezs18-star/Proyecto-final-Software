from funciones import agregar_gasto, consultar_gastos, modificar_gasto, borrar_gasto

def bienvenida():
    """Esta función da la bienvenida a la app"""
    print("BIENVENIDO/A A PAPOIMONEY (Bellooo, tank yu! Tulaliloo ti amo!)")
    print("\nDescubre la forma más inteligente y sencilla de manejar tu  (BEE DO BEE DO BEE DO!)")
    print("con el sistema 50-30-20:\n")
    print("  50% para cosas necesarias (Casa-banana (vivienda), banana (comida), room-room (transporte) 🎯)")
    print("  30% para deseos (Baboi (diversión), shoppa-shoppa (compras)) 📋")
    print("  20% para ahorrar (money-bobo) 🐷")
    print("\nAutomatiza tu presupuesto, evita gastos innecesarios y toma el")
    print("control de tu bienestar financiero. ¡Comencemos a planificar! (PAPAYA!)")

# Este es el submenú de nuestro programa donde se muestran las opciones después de escoger en el menú principal

def menu_categoria(nombre_categoria, categoria_dict, sueldo):
    """Menú de operaciones para cada categoría"""
    porcentajes = {"Necesidades": 0.50, "Deseos": 0.30, "Ahorro": 0.20}
    presupuesto_max = sueldo * porcentajes[nombre_categoria]
    
    while True:
        total_gastado = sum(categoria_dict.values())
        disponible = presupuesto_max - total_gastado
        
        print(f"\n")
        print(f"📂 {nombre_categoria.upper()} - Presupuesto: ${presupuesto_max:.2f}")
        print(f"   Gastado: ${total_gastado:.2f} | Disponible: ${disponible:.2f}")
        print("\nOpciones:")
        print("  a. Agregar gasto (banana-spend)💲")
        print("  b. Consultar gastos (moni-moni check) 💰")
        print("  c. Modificar gasto (moni-mudi) ✍🏻")
        print("  d. Borrar gasto (Sa la ka!) 🗑️")
        print("  e. Volver al menú principal (Papoi) 🏡")
        
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
