"""
Módulo para contar la frecuencia de palabras en un archivo de texto.
"""

import sys
import time


def count_words(filename):
    """Lee el archivo y cuenta la frecuencia de cada palabra manualmente."""
    word_freq = {}
    start_time = time.time()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    clean_word = word.strip('.,"?!():;').lower()
                    if clean_word:
                        if clean_word in word_freq:
                            word_freq[clean_word] += 1
                        else:
                            word_freq[clean_word] = 1
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe.")
        return None, 0

    elapsed_time = time.time() - start_time
    return word_freq, elapsed_time


def main():
    """Función principal para ejecutar el conteo y guardar resultados."""
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py archivo.txt")
        return

    filename = sys.argv[1]
    word_freq, elapsed = count_words(filename)

    if word_freq is None:
        return

    header = f"{'WORD':<15} {'FREQUENCY':<10}"
    divider = "-" * 30
    print(f"\nResultados para: {filename}")
    print(header)
    print(divider)

    with open("WordCountResults.txt", "a", encoding='utf-8') as out_file:
        out_file.write(f"\nResultados para: {filename}\n")
        out_file.write(f"{header}\n{divider}\n")
        sorted_words = sorted(word_freq.items())
        for word, count in sorted_words:
            line = f"{word:<15} {count:<10}"
            print(line)
            out_file.write(line + "\n")
        time_msg = f"\nTiempo de ejecución: {elapsed:.6f} segundos\n"
        print(time_msg)
        out_file.write(time_msg + "=" * 30 + "\n")


if __name__ == "__main__":
    main()