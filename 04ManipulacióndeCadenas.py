def procesar_cadena(cadena, letra_a_reemplazar, letra_reemplazo):
    cadena_minusculas = cadena.lower()
    cadena_reemplazada = cadena_minusculas.replace(letra_a_reemplazar, letra_reemplazo)
    lista_palabras = cadena_reemplazada.split()
    print("Cadena modificada:", cadena_reemplazada)
    print("Lista de palabras:", lista_palabras)
    
cadena = "Hola Mundo, Python es Genial"
letra_a_reemplazar = 'o'
letra_reemplazo = 'a'
procesar_cadena(cadena, letra_a_reemplazar, letra_reemplazo)