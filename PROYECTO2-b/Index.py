# Pensamiento Comutacional seccion 11
#Fecha: 20/05/2024
#autor: Hernan Obdulio III Juarez Cantoral 
#objetivo: Realizar todas las funciones requeridas por el laboratorio de ADN entre las cuales estan Ingresar los sujetos de prueba, Ingresar la cadena de ADN de los sujetos de prueba, Contenido de GC, Resumen de secuencia de ADN, encontrar la secuencia más larga, calcular el porcentaje de similitud entre dos sujetos de prueba, mostrar el resumen de sujetos de prueba y salir
#entrada: Nombre y apellido de sujetos de prueba, Cadena de ADN 
#procesos: print, while, if, elif, else, .strip, .upper, .lower, len, all, next, .append, for, in, and, set
#salida: Lista con sujetos de prueba y ADN, contenido de GC en ADN, porcentaje de bases en cadena de ADN, Secuencia mas larga y posicion, similitud entre dos sujetos de prueba y su parentezco (relacion)


# Llamar las librerias y modulos
from funciones1.funciones_generales import porcentualidad, buscarsujeto, porcentualidad_bases, similitud_sujetos

# Definir una lista vacía para almacenar los sujetos de prueba
Lista = []

#Inicio de ciclo para la lista
opcion = ""
while opcion !=8 :
    print("----- *MENU* -----")
    print("1. Registrar Sujeto de prueba")
    print("2. Ingresar cadena de ADN")
    print("3. Contenido de GC")
    print("4. Resumen de secuencia de ADN")
    print("5. Secuencia mas larga")
    print("6. Porcentaje de similitud")
    print("7. Resumen de sujetos de prueba")
    print("8. SALIR")
    opcion = int(input("Ingrese la opción que desea ejecutar : "))

# Ingresar los sujetos de prueba 
    if opcion == 1:
            print("Registre los datos del sujeto" )
            ns = input("Ingrese el nombre del sujeto de prueba: ").strip()
            aps = input("Ingrese el apellido del sujeto de prueba: ").strip()
            Lista.append({"nombre": ns,"apellido":aps, "adn": ""})
            print("Sujeto de prueba ah registrado exitosamente.")
            

#Ingresar la cadena de ADN de los sujetos de prueba 
    elif opcion == 2:
        print("Registra la cadena de ADN")
        ns = input("Ingrese el nombre del sujeto de prueba: ").strip()
        aps = input("Ingrese el apellido del sujeto de prueba: ").strip()
        #Funcion encargada de buscar al sujeto en la lista
        sujeto = buscarsujeto(Lista,ns,aps)
        if sujeto:
            adn = input("Ingrese la cadena de ADN del sujeto de prueba: ").strip()
            adn = adn.upper()
            if len(adn) >= 13 and all(base in "ACGT" for base in adn):
                if sujeto["adn"] == "":
                    sujeto["adn"] = adn
                    print("Cadena de ADN ingresada exitosamente.")
                else:
                    respuesta = input("¿Desea reemplazar el ADN anterior? (s/n): ").strip()
                    if respuesta.lower() == "s":
                        sujeto["adn"] = adn
                        print("ADN reemplazado exitosamente.")
                    else:
                        print("ADN anterior conservado.")
            else:
                print("La cadena de ADN debe tener al menos 13 caracteres y contener solo las bases A, C, G y T.")
        else:
            print("El sujeto de prueba no existe en la lista")

#Contenido de GC
    elif opcion == 3:
        print("Contenido de GC")
        ns = input("Ingrese el nombre del sujeto de prueba: ").strip()
        aps = input("Ingrese el apellido del sujeto de prueba: ").strip()
        sujeto = buscarsujeto(Lista,ns,aps)
        if sujeto:
            adn = sujeto["adn"]
            #Funcion encargada de sacar la porcentualidad de GC en ADN
            porcentaje= porcentualidad(adn)
            print(f"El contenido de GC para el sujeto de prueba {ns} es: {porcentaje:.2f}%")
        else:
            print("El sujeto de prueba no existe en la lista")
            
# Resumen de secuencia de ADN 
    elif opcion == 4:
        print("Resumen de secuencia de ADN")
        ns = input("Ingrese el nombre del sujeto de prueba: ").strip()
        aps = input("Ingrese el apellido del sujeto de prueba: ").strip()
        #Funcion encargada de buscar al sujeto en la lista
        sujeto = buscarsujeto(Lista,ns,aps)
        if sujeto:
            adn = sujeto["adn"]
            bases = set(adn)
            for base in bases:
                #Funcion encargada de sacar el porcentaje de las bases en la cadena total de ADN
                porcentaje_bases = porcentualidad_bases(adn,base)
                print(f"Porcentaje de {base}: {porcentaje_bases:.2f}%")
        else:
            print("El sujeto de prueba no existe en la lista")

    # Encontrar la secuencia más larga
    elif opcion == 5:
        print("Secuencia mas larga")
        ns = input("Ingrese el nombre del sujeto de prueba: ").strip()
        aps = input("Ingrese el apellido del sujeto de prueba: ").strip()
        #Funcion encargada de buscar al sujeto en la lista
        sujeto = buscarsujeto(Lista,ns,aps)
        if sujeto:
            adn = sujeto["adn"]
            secuencia_larga = ""                   
            secuencia_actual = ""
            for base in adn:
                if base == secuencia_actual[-1:]:
                    secuencia_actual += base
                else:
                    secuencia_actual = base
                if len(secuencia_actual) > len(secuencia_larga):
                    secuencia_larga = secuencia_actual
            posicion_inicio = adn.index(secuencia_larga) + 1
            print(f"Secuencia más larga para el sujeto de prueba {ns}:")
            print(f"Posición de inicio: {posicion_inicio}")
            print(f"Secuencia: {secuencia_larga}")
        else:
            print("El sujeto de prueba no existe.")

    # Función para calcular el porcentaje de similitud entre dos sujetos de prueba
    elif opcion == 6:
        print("Porcentaje de similitud entre sujetos de prueba")
        nombre1 = input("Ingrese el nombre del primer sujeto de prueba: ").strip()
        apellido1 = input("Ingrese el apellido del primer sujeto de prueba: ").strip()
        nombre2 = input("Ingrese el nombre del segundo sujeto de prueba: ").strip()
        apellido2 = input("Ingrese el apellido del segundo sujeto de prueba: ").strip()
        #Funcion encargada de buscar al sujeto en la lista
        sujeto1 = buscarsujeto(Lista,nombre1,apellido1)
        sujeto2 = buscarsujeto(Lista,nombre2,apellido2)
        if sujeto1 and sujeto2:
            secuencia1 = sujeto1["adn"]
            secuencia2 = sujeto2["adn"]
            #Funcion de calcular la relacion a partir de su similitud de ADN
            porcentaje= similitud_sujetos(secuencia1,secuencia2)
            print(f"El porcentaje de similitud entre los sujetos de prueba {nombre1} y {nombre2} es: {porcentaje:.2f}%")
            if porcentaje >= 50:
                print("Posible relación: padre o hijo")
            elif porcentaje >= 25 and porcentaje <= 49:
                print("Posible relación: abuelo, nieto, tío o tía, sobrino, medio hermano")
            elif porcentaje >= 12.5 and porcentaje <= 24:
                print("Posible relación: primo hermano, bisabuelo, bisnieto, tío abuelo o tía abuela, sobrino abuelo o sobrina nieta, medio tío o tía, medio sobrino o sobrina")
            elif porcentaje <= 12.5:
                print("Sin relación")
        else:
            print("Por lo menos un sujeto de prueba no existe en la lista")

    # Función para mostrar el resumen de sujetos de prueba
    elif opcion == 7:
        print("Resumen de sujetos de prueba:")
        print("La informacion de la lista completa de los sujetos de prueba es: ")
        for sujeto in Lista:
            print(f"Nombre: {sujeto['nombre']}")
            print(f"Apellido: {sujeto['apellido']}")
            print(f"Secuencia de ADN: {sujeto['adn']}")
            print()
            
    #SALIR del programa
    elif opcion == 8:
        print("BYE...BYE..")

    else:
        print("Seleccione una opcion que sea correcta de ejecutar")