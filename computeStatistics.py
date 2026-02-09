"""
Para calcular estadísticas descriptivas desde un archivo de texto.
"""

import sys
import time


def calculate_statistics(numbers):
    """
    Calcula estadísticas poblacionales: media, mediana, moda, varianza y desviación éstandar.
    """
    n_count = len(numbers)
    if n_count == 0:
        return None

    # Media
    mean_val = sum(numbers) / n_count

    # Mediana
    sorted_numbers = sorted(numbers)
    if n_count % 2 == 0:
        median_val = (sorted_numbers[n_count // 2 - 1] +
                      sorted_numbers[n_count // 2]) / 2
    else:
        median_val = sorted_numbers[n_count // 2]

    # Moda
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_f = max(counts.values())

    if max_f == 1 and n_count > 1:
        mode_val = "#N/A"
    else:
        modes = [k for k, v in counts.items() if v == max_f]
        mode_val = modes[0]

    # Varianza Poblacional
    variance_p = sum((x - mean_val) ** 2 for x in numbers) / n_count - 1

    # Desviación Estándar Poblacional
    std_dev_p = variance_p ** 0.5

    return n_count, mean_val, median_val, mode_val, std_dev_p, variance_p


def main():
    """
    Función principal para la ejecución desde línea de comandos.
    """
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py archivo.txt")
        return

    filename = sys.argv[1]
    numbers = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    val = line.strip()
                    if val:
                        numbers.append(float(val))
                except ValueError:
                    print(f"Error: dato inválido  -> {val}")
    except FileNotFoundError:
        print(f"Error: el archivo {filename} no existe.")
        return

    stats = calculate_statistics(numbers)
    elapsed_time = time.time() - start_time

    if stats:
        output = (
            f"Archivo: {filename}\n"
            f"Conteo: {stats[0]}\n"
            f"Promedio: {round(stats[1], 2)}\n"
            f"Mediana: {stats[2]}\n"
            f"Moda: {stats[3]}\n"
            f"Desviación estándar: {round(stats[4], 6)}\n"
            f"Varianza: {round(stats[5], 4)}\n"
            f"Tiempo de ejecución: {elapsed_time:.4f} seconds\n"
        )
        print(output)
        with open("StatisticsResults.txt", "a", encoding='utf-8') as out_file:
            out_file.write(output + "-"*30 + "\n")


if __name__ == "__main__":
    main()