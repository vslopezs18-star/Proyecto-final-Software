# Aquí se encuentran todas las funciones base para la ejecución del programa

def mostrar_presupuesto(sueldo, necesidades_dict, deseos_dict, ahorro_dict):
    """Muestra el resumen del presupuesto y gastos actuales"""
    # Nuestro programa calcula el 50% del sueldo para necesidades
    presupuesto_necesidades = sueldo * 0.50
    # Calcula el 30% del sueldo para deseos
    presupuesto_deseos = sueldo * 0.30
    # Calcula el 20% del sueldo para ahorro
    presupuesto_ahorro = sueldo * 0.20
    
    # Luego, suma todos los valores del diccionario de necesidades para obtener el total gastado
    total_necesidades = sum(necesidades_dict.values())
    # Suma todos los valores del diccionario de deseos
    total_deseos = sum(deseos_dict.values())
    # Suma todos los valores del diccionario de ahorro
    total_ahorro = sum(ahorro_dict.values())
    
    # Imprime líneas en blanco para separación visual 
    print("\n")
    
    # Imprime el título del resumen centrado usando espacios
    print(" " * 25 + "RESUMEN DE PRESUPUESTO")
    
    # Este prrint muestra el ingreso total con formato de dos decimales
    print(f"\n💵 Ingreso Total: ${sueldo:.2f}\n")
    
    # Imprime el encabezado de la tabla con columnas alineadas a la izquierda
    print(f"{'Categoría':<25} {'Presupuesto':<15} {'Gastado':<15} {'Disponible':<15}")

    # Imprime la fila de Necesidades con los montos calculados y formateados
    # El programa resta el total gastado del presupuesto para mostrar lo disponible
    print(f"{'Necesidades (50%)':<25} ${presupuesto_necesidades:<14.2f} ${total_necesidades:<14.2f} ${presupuesto_necesidades - total_necesidades:<14.2f}")
    
    # Imprime la fila de Deseos con sus respectivos montos
    print(f"{'Deseos (30%)':<25} ${presupuesto_deseos:<14.2f} ${total_deseos:<14.2f} ${presupuesto_deseos - total_deseos:<14.2f}")
    
    # Imprime la fila de Ahorro con sus respectivos montos
    print(f"{'Ahorro (20%)':<25} ${presupuesto_ahorro:<14.2f} ${total_ahorro:<14.2f} ${presupuesto_ahorro - total_ahorro:<14.2f}")
    
    # Imprime dos líneas en blanco para separación final
    print("\n")


def agregar_gasto(categoria_dict, nombre_categoria, presupuesto_max, total_gastado):
    """Agrega un gasto a una categoría específica"""
    # Nuestro programa solicita al usuario que ingrese el concepto del gasto
    # Usa el método strip() para eliminar espacios en blanco al inicio y final, evitando errores de dedo
    concepto = input(f"\nIngrese el concepto del gasto en {nombre_categoria}: ").strip()
    
    # Nuestro programa inicializa una variable bandera (booleana) en False para controlar el bucle de validación
    monto_valido = False
    
    # Inicia un bucle que se repetirá mientras el monto no sea válido
    while monto_valido == False:
        # Le solicita al usuario que ingrese el monto del gasto a agregar
        monto_texto = input(f"Ingrese el monto para '{concepto}': $").strip()
        
        # Nuestro programa verifica si el usuario no ingresó nada
        if monto_texto == "":
            # Muestra un mensaje de advertencia si la entrada está vacía (para avanzar debe llenar el monto)
            print("⚠️  Por favor ingrese un monto válido.")
        else:
            # Si hay texto, comienza a validar que sea un número e inicializa una booleana asumiendo que es un número válido
            es_numero = True
            # Inicializa una bandera para verificar si ya encontró un punto decimal
            tiene_punto = False
            # Comienza a revisar cada caracter desde la posición 0 (clave para evitar resultados no deseados)
            posicion = 0
            
            # Recorre cada caracter del texto mientras no llegue al final y mientras siga siendo un número válido
            while posicion < len(monto_texto) and es_numero == True:
                # Obtiene el caracter en la posición actual, iniciando en 0
                caracter = monto_texto[posicion]
                
                # Verifica si el caracter es un signo negativo y está al inicio
                if caracter == '-' and posicion == 0:
                    # El programa permite el signo negativo solo al inicio y no cambia es_numero, permanece True
                    es_numero = True
                # Verifica si el caracter es un punto decimal
                elif caracter == '.':
                    # Si ya había encontrado un punto antes, el número no es válido, ya que solo se admite un punto decimal
                    if tiene_punto == True:
                        es_numero = False
                    else:
                        # Si es el primer punto, lo marca como encontrado, porque se señaló como False
                        tiene_punto = True
                # Verifica si el caracter es un dígito del 0 al 9 (evalua uno por uno)
                elif caracter in '0123456789':
                    # El programa confirma que es válido manteniendo es_numero en True
                    es_numero = True
                else:
                    # Si el caracter no es ninguno de los anteriores, marca como inválido (#$%&*)
                    es_numero = False
                
                # Avanza a la siguiente posición y repite el proceso
                posicion = posicion + 1 
            
            # Después de revisar todos los caracteres, verifica si el texto es un número válido, ya que se abre como un string
            if es_numero == True:
                # Convierte el texto a un número decimal (float)
                monto = float(monto_texto)
                
                # Marca que el monto es válido para salir del bucle, después de verificar que es número
                monto_valido = True
            else:
                # Si no es válido, muestra un mensaje de error y el bucle se repite
                print("⚠️  Por favor ingrese un monto válido.")
    
    # Nuestro programa valida que el monto sea mayor a cero
    if monto <= 0:
        # Si el monto es cero o negativo, muestra un mensaje de error
        print("⚠️  El monto debe ser mayor a 0.")
        
        # Retorna el total gastado sin cambios (no agrega el gasto)
        return total_gastado
    
    # Calcula cuál sería el nuevo total si se agrega este gasto para mantener el control
    nuevo_total = total_gastado + monto
    
    # Nuestro programa verifica si el nuevo total excedería el presupuesto máximo (potenciar la toma de decisiones)
    if nuevo_total > presupuesto_max:
        print(f"\n⚠️  ADVERTENCIA: Este gasto excede tu presupuesto de {nombre_categoria}!")
        # Muestra el presupuesto máximo permitido
        print(f"   Presupuesto: ${presupuesto_max:.2f}")
        # Muestra cuál sería el total gastado con este nuevo gasto
        print(f"   Total gastado: ${nuevo_total:.2f}")
        # Calcula y muestra cuánto se estaría excediendo para optimizar su gestión
        print(f"   Exceso: ${nuevo_total - presupuesto_max:.2f}")
        
        # Solicita confirmación al usuario si desea agregar el gasto de todas formas (a veces es inevitable)
        # Usamos el método lower() para convertir la respuesta a minúsculas y evitar problemas si se escribe en mayuscula o no
        confirmacion = input("\n¿Deseas agregar este gasto de todas formas? (si/no): ").lower()
        
        # Si el usuario no responde "si" mostrara un mensaje confirmando que no se agregó el gasto
        if confirmacion != 'si':
            print("✅ Gasto no agregado.")
            # Retorna el total gastado sin cambios
            return total_gastado
    
    # Nuestro programa agrega el gasto al diccionario usando el concepto como clave y el monto como valor
    categoria_dict[concepto] = monto
    print(f"✅ Gasto '{concepto}' de ${monto:.2f} agregado exitosamente a {nombre_categoria}.")
    # Retorna el nuevo total gastado actualizado
    return nuevo_total


def consultar_gastos(categoria_dict, nombre_categoria):
    """Consulta y muestra todos los gastos de una categoría"""
    # Nuestro programa verifica si el diccionario de la categoría está vacío y si no hay gastos registrados, muestra un mensaje informativo
    if len(categoria_dict) == 0:
        print(f"\n📋 No hay gastos registrados en {nombre_categoria}.")
    else:
        # Si hay gastos, imprime líneas en blanco para separación
        print("\n")
        # Muestra el título de la sección con el nombre de la categoría en mayúsculas
        print(f"📋 GASTOS EN {nombre_categoria.upper()}")
        print("\n")
        
        # Inicializa una variable para acumular el total de gastos
        total = 0
        
        # Nuestro programa recorre cada concepto-monto que exista en el diccionario
        # Usamos enumerate() para agregar un número secuencial comenzando desde 1
        for i, (concepto, monto) in enumerate(categoria_dict.items(), 1):
            # Imprime el número, el concepto capitalizado y el monto formateado para mostrar los datos adecuadamente
            print(f"{i}. {concepto.capitalize()}: ${monto:.2f}")
            
            # Acumula el monto al total
            total += monto
        # Imprime líneas en blanco para separación
        print("\n")
        # Muestra el total acumulado de todos los gastos formateado
        print(f"{"TOTAL:"} ${total:.2f}")
        print("\n")


def modificar_gasto(categoria_dict, nombre_categoria):
    """Modifica un gasto existente"""
    # Nuestro programa verifica si el diccionario está vacío y si no hay gastos, muestra un mensaje y sale de la función
    if len(categoria_dict) == 0:
        print(f"\n⚠️  No hay gastos en {nombre_categoria} para modificar.")
        return 
    
    # Llama a la función para mostrar todos los gastos actuales
    consultar_gastos(categoria_dict, nombre_categoria)
    
    # Convierte las claves del diccionario en una lista para poder acceder por índice, volviendo más interactivo el menú
    conceptos = list(categoria_dict.keys())
    print("Conceptos disponibles:")
    # Recorre la lista de conceptos comenzando desde 1
    for listador, concepto in enumerate(conceptos, 1):
        # Imprime cada concepto con su número de iterable listador
        print(f"{listador}. {concepto}")
    
    # Inicializa un booleano para validar el índice ingresado
    indice_valido = False
    
    # Inicia un bucle que se repetirá hasta que el índice sea válido
    while indice_valido == False:
        indice_texto = input("\nDigite el número del gasto a modificar: ").strip()
        
        # Verifica si el usuario no ingresó nada y muestra un mensaje si esta vacío
        if indice_texto == "":
            print("⚠️  Entrada inválida.")
        else:
            # Si hay texto, nuestro programa comienza a validar que sea un número
            es_numero = True
            posicion = 0
            
            # Recorre cada caracter del texto ingresado y obtiene el caracter en la posición actual
            while posicion < len(indice_texto) and es_numero == True:
                caracter = indice_texto[posicion]
                
                # Verifica si el caracter NO es un dígito
                if caracter not in '0123456789':
                    # Marca como no válido
                    es_numero = False
                
                # Avanza a la siguiente posición
                posicion = posicion + 1
            
            # Si todos los caracteres son dígitos, convierte el texto a número entero y resta 1 (porque las listas empiezan en 0)
            if es_numero == True:
                indice = int(indice_texto) - 1
                
                # Verifica si el índice está dentro del rango válido de la lista y marca el índice como válido para salir del bucle
                if 0 <= indice < len(conceptos):
                    indice_valido = True
                else:
                    # Si el número está fuera de rango, muestra un error
                    print("⚠️  Número inválido.")
            else:
                # Si no todos los caracteres son dígitos, muestra un error
                print("⚠️  Entrada inválida.")
    
    # Obtiene el concepto del gasto seleccionado usando el índice ya validado
    concepto_viejo = conceptos[indice]
    
    # Muestra el concepto y monto actual del gasto seleccionado
    print(f"\nPor lo tanto el {concepto_viejo} pasa a ser ${categoria_dict[concepto_viejo]:.2f}")
    
    # Solicita al usuario un nuevo concepto (puede dejarlo en blanco para mantener el actual)
    nuevo_concepto = input("Ingrese el nuevo concepto (Enter para mantener): ").strip()
    
    # Solicita al usuario un nuevo monto (puede dejarlo en blanco para mantener el actual)
    nuevo_monto = input("Ingrese el nuevo monto (Enter para mantener): $").strip()
    
    # Verifica si el usuario ingresó un nuevo concepto
    if nuevo_concepto != "":
        # Nuestro elimina la entrada con el concepto viejo y crea una nueva con el concepto nuevo 
        # Usamos el método pop() para eliminar y retornar el valor, que luego se asigna a la nueva clave
        categoria_dict[nuevo_concepto] = categoria_dict.pop(concepto_viejo)
        
        # Actualiza el concepto_viejo para usar en las siguientes operaciones
        concepto_viejo = nuevo_concepto
    
    # Verifica si el usuario ingresó un nuevo monto e inicializa un booleano para validar el monto
    if nuevo_monto != "":
        monto_valido = False
        
        # Inicia un bucle para validar el formato del monto
        while monto_valido == False:
            # Cuenta cuántos puntos decimales tiene el texto y su posición
            cantidad_puntos = 0
            pos_punto = 0
            
            # Recorre cada caracter para contar los puntos y encontrar su posición
            while pos_punto < len(nuevo_monto):
                if nuevo_monto[pos_punto] == '.':
                    cantidad_puntos = cantidad_puntos + 1
                pos_punto = pos_punto + 1
            
            # Verifica si tiene más de un punto decimal
            if cantidad_puntos > 1:
                # Si tiene múltiples puntos, solicita nuevamente el monto (no es valido agregar más de uno)
                nuevo_monto = input("⚠️  Monto inválido. Ingrese el nuevo monto: $").strip()
            else:
                # Convierte el texto a una lista de caracteres para poder manipularlo facilmente
                lista_caracteres = list(nuevo_monto)
                
                # Si hay un punto en la lista, lo elimina para validar solo los dígitos
                if '.' in lista_caracteres:
                    lista_caracteres.remove('.')
                
                # Si hay un signo negativo al inicio, lo elimina para validar solo los dígitos
                if len(lista_caracteres) > 0 and lista_caracteres[0] == '-':
                    lista_caracteres.remove('-')
                
                # Verifica si quedaron caracteres después de quitar el punto y el signo
                if len(lista_caracteres) > 0:
                    # Inicializa una bandera asumiendo que todos son dígitos
                    todos_digitos = True
                    pos = 0
                    
                    # Recorre cada caracter restante
                    while pos < len(lista_caracteres) and todos_digitos == True:
                        # Verifica si el caracter NO es un dígito
                        if lista_caracteres[pos] not in '0123456789':
                            todos_digitos = False
                        pos = pos + 1
                    
                    # Si todos los caracteres son dígitos
                    if todos_digitos == True:
                        # Actualiza el valor en el diccionario convirtiendo el texto a número decimal
                        categoria_dict[concepto_viejo] = float(nuevo_monto)
                        
                        # Marca el monto como válido para salir del bucle
                        monto_valido = True
                    else:
                        # Si hay caracteres que no son dígitos, solicita nuevamente el monto
                        nuevo_monto = input("⚠️  Monto inválido. Ingrese el nuevo monto: $").strip()
                else:
                    # Si no quedaron caracteres, solicita nuevamente el monto
                    nuevo_monto = input("⚠️  Monto inválido. Ingrese el nuevo monto: $").strip()
    
    # Muestra un mensaje de confirmación de que el gasto fue modificado exitosamente
    print(f"✅ Gasto modificado exitosamente.")
    
def borrar_gasto(categoria_dict, nombre_categoria):
    """Borra un gasto de una categoría"""
    
   # Verifica si el diccionario de categoría está vacío
    if len(categoria_dict) == 0:
        print(f"\n⚠️  No hay gastos en {nombre_categoria} para borrar.")
        return
    
    # Llama a la función para mostrar los gastos disponibles en la categoría
    consultar_gastos(categoria_dict, nombre_categoria)
    
    # Extrae las claves del diccionario y las convierte en lista
    conceptos = list(categoria_dict.keys())
    
    # Validamos para iniciar el bucle
    indice_valido = False
    
    # Se inicia un bucle que se repetirá hasta obtener un índice válido
    while indice_valido == False:
        indice_texto = input("\nDigite el número del gasto a borrar: ").strip()
        
        # Verificamos si el usuario ingresó un contenido "vacío"
        if indice_texto == "":
            # Si lo ingresado no posee caracteres, muestra mensaje
            print("⚠️  Entrada inválida. (Tatata bala tu!)")
        else:
            # Verificamos que la entrada sean dígitos
            es_numero = True
            #Iniciamos con el contador en la posición en cero como referencia
            posicion = 0
            
            # Corrobora cada caracter de la entrada para validar que sea un dígito
            while posicion < len(indice_texto) and es_numero == True:
                caracter = indice_texto[posicion]
                
             # Descarta que el caracter no sea un dígito del 0 al 9  
                if caracter not in '0123456789':
                    es_numero = False 
             
            # Aumenta la posición para verificar el siguiente caracter    
                posicion = posicion + 1
             
            # Verifica si todos los caracteres son dígitos válidos
            if es_numero == True:
                # Determina el input a número entero y resta 1 para ajustar el índice
                indice = int(indice_texto) - 1
                
                # Por último, verifica si el índice se encuentra en el rango válido de la lista
                if 0 <= indice < len(conceptos):
                    indice_valido = True # Termina el bucle 
                else:
                    # Si el número está fuera de rango, muestra mensaje de error
                    print("⚠️  Número inválido.")
            else:
                print("⚠️  Entrada inválida. (Tatata bala tu!)") # También, muestra mensaje de error si la entrada contiene caracteres no numéricos
    
   # Obtiene el concepto del gasto usando el índice validado
    concepto = conceptos[indice]
    
     # Elimina el gasto del diccionario y guarda el monton en una variable
    monto = categoria_dict.pop(concepto)
    
    # Muestra mensaje de confirmación con el concepto y el monto eliminados
    print(f"✅ Gasto '{concepto}' de ${monto:.2f} eliminado exitosamente.")
