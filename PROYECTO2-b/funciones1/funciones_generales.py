# Funcion encargada de porcentualidad de GC en ADN 
def porcentualidad(adn):
    contador = adn.count("G") + adn.count("C")
    porcentualidad = (contador / len(adn))*100
    return porcentualidad

# Funcion Encargada de buscar al sujeto de prueba en la lista 
def buscarsujeto(Lista,nombre,apellido):
    buscarsujeto = next((s for s in Lista if (s["nombre"].upper() == nombre.upper() and s["apellido"].upper() == apellido.upper()) ), None)
    return buscarsujeto

# Funcion encargada de sacar la porcentualidad de cada una de las bases en la cadena completa de ADN 
def porcentualidad_bases(adn,base):
    contador_base = adn.count(base)
    porcentualidad_bases = (contador_base / len(adn))*100
    return porcentualidad_bases

# Funcion encargada encontrar la relacion de parentezco entre dos sujetos de prueba 
def similitud_sujetos(secuencia1,secuencia2):
    parentezco = sum(base1 == base2 for base1, base2 in zip(secuencia1, secuencia2))
    parentezco_sujetos = (parentezco / len(secuencia1)) * 100
    return parentezco_sujetos
