#!/bin/python3
# Función para convertir un nombre en el formato deseado
def formatear_nombre(nombre):
    partes = nombre.split(".")
    if len(partes) == 2:
        nombre_completo = partes[0].capitalize() + " " + partes[1].capitalize()
        inicial_punto_apellido = partes[0][0].capitalize() + "." + partes[1].capitalize()
        inicial_apellido = partes[0][0].capitalize()  + partes[1]
        return nombre + "\n" + nombre_completo + "\n" + inicial_apellido + "\n" + inicial_punto_apellido + "\n"
    else:
        return nombre + "\n"  # El formato no es válido, se conserva sin cambios

# Nombre del archivo de entrada y salida
archivo_entrada = "usuarios.txt"
archivo_salida = "usuarios_formateados.txt"

# Abrir el archivo de entrada en modo lectura
with open(archivo_entrada, "r") as entrada:
    # Leer líneas del archivo de entrada
    lineas = entrada.readlines()

# Abrir el archivo de salida en modo escritura
with open(archivo_salida, "w") as salida:
    for linea in lineas:
        # Eliminar caracteres de nueva línea al final de cada línea
        linea = linea.strip()
        # Formatear el nombre y escribirlo en el archivo de salida
        linea_formateada = formatear_nombre(linea)
        salida.write(linea_formateada)

print(f"Se ha generado el archivo '{archivo_salida}' con los nombres formateados en nuevas líneas.")
