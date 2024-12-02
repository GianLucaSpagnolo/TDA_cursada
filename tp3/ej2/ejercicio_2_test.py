import os
import ejercicio_2 as ej2
import sys


def test_ejercicio_2(weights, values, capacity, epsilon):
    print("Datos de entrada")
    print("=====================================")

    for i in range(len(values)):
        print(f"Item {i + 1} - Peso: {weights[i]} - Valor: {values[i]}")

    print("\nCapacidad de la mochila:", capacity)
    print("\nEpsilon:", epsilon)

    # Ejecutar la función de aproximación
    result = ej2.knapsack_approx(weights, values, capacity, epsilon)

    # Imprimir el valor óptimo aproximado
    print("\nResultado")
    print("=====================================")

    for i in result["selectedItems"]:
        print(f"Item {i} - Peso: {weights[i - 1]} - Valor: {values[i - 1]}")

    print("Valor total:", result["totalValue"])
    print("Peso total:", result["totalWeight"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python ejercicio_2_test.py <archivo>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename) as f:
        epsilon = float(f.readline().strip())
        capacity = int(f.readline().strip())
        element_count = int(f.readline().strip())
        weights = []
        values = []

        for _ in range(element_count):
            weight, value = map(int, f.readline().strip().split(","))
            weights.append(weight)
            values.append(value)

        test_ejercicio_2(weights, values, capacity, epsilon)
