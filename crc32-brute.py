import itertools
import binascii
import argparse

# Función para generar todas las posibles combinaciones de 5 letras del alfabeto en inglés
def generate_combinations():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+="
    for combination in itertools.product(alphabet, repeat=5):
        yield ''.join(combination)

# Función para calcular el CRC32 de una cadena
def crc32(string):
    return binascii.crc32(string.encode())

# Parseo de argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Calcula el CRC32 de todas las posibles combinaciones de 5 letras del alfabeto en inglés.")
parser.add_argument("target_crc32", type=str, help="Valor de CRC32 que se va a buscar.")
args = parser.parse_args()

# Ciclo principal
for combination in generate_combinations():
    if crc32(combination) == int(args.target_crc32, 16):
        print(f"La cadena que genera el CRC32 {args.target_crc32} es: {combination}")
        break
else:
    print(f"No se encontró ninguna cadena que genere el CRC32 {args.target_crc32}")
