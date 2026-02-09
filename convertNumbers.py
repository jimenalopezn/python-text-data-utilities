"""
Código para convertir números a binario y hexadecimal.
Implementa algoritmos manuales para cumplir con los requisitos.
"""

import sys
import time


def convert_to_binary(num):
    """Convierte un entero a binario usando el método de residuos."""
    if num == 0:
        return "0"
    is_neg = num < 0
    val = abs(num)
    binary = ""
    while val > 0:
        binary = str(val % 2) + binary
        val //= 2
    return "-" + binary if is_neg else binary


def convert_to_hexadecimal(num):
    """Convierte un entero a hexadecimal usando el método de residuos."""
    if num == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    is_neg = num < 0
    val = abs(num)
    hex_str = ""
    while val > 0:
        hex_str = hex_chars[val % 16] + hex_str
        val //= 16
    return "-" + hex_str if is_neg else hex_str


def main():
    """Función principal para procesar el archivo y mostrar resultados."""
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py archivo.txt")
        return

    start_time = time.time()
    results = []

    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            for line in file:
                raw = line.strip()
                if raw:
                    try:
                        number = int(float(raw))
                        results.append((number, convert_to_binary(number),
                                       convert_to_hexadecimal(number)))
                    except ValueError:
                        print(f"Error: dato inválido ignorado -> {raw}")
    except FileNotFoundError:
        print("Error: El archivo no existe.")
        return

    elapsed = time.time() - start_time
    header = f"{'ITEM':<5} {'NUMBER':<12} {'BINARY':<25} {'HEX':<12}"
    divider = "-" * 60
    print(header)
    print(divider)

    with open("ConvertionResults.txt", "a", encoding='utf-8') as out:
        out.write(f"\nArchivo: {sys.argv[1]}\n{header}\n{divider}\n")
        for i, (n, b, h) in enumerate(results, 1):
            row = f"{i:<5} {n:<12} {b:<25} {h:<12}"
            print(row)
            out.write(row + "\n")
        out.write(f"Tiempo de ejecución: {elapsed:.6f}s\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()