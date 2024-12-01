import math

def knapsack_approx(weights, values, capacity, epsilon):
    n = len(values)

    # Calcular el valor máximo v* (máximo de los valores)
    v_star = max(values)

    # Calcular el parámetro de redondeo b
    b = int(epsilon / (2 * n) * v_star)

    # Redondear los valores de los elementos
    rounded_values = [math.ceil(value / b) * b for value in values]  # Redondeamos a múltiplos superiores de b
    scaled_values = [int(value / b) for value in rounded_values]  # Se construye el arreglo de valores escalados
    
    print(f"Valores originales: {values}")
    print(f"Valores redondeados: {rounded_values}")
    print(f"Valores escalados: {scaled_values}")

    # Resolver el problema de la mochila usando el algoritmo de programación dinámica con los valores escalados
    max_value = sum(scaled_values)
    matrix = [[0] * (max_value + 1) for _ in range(n + 1)]


    scaled_values_current_sum = 0
    # Llenar la matriz M
    for i in range(1, n + 1):
        scaled_values_current_sum += scaled_values[i - 1]
        for j in range(1, max_value + 1):
            if j > scaled_values_current_sum:  # Si el valor excede la suma de los primeros i elementos
                matrix[i][j] = weights[i - 1] + matrix[i - 1][j]
            else:
                matrix[i][j] = min(matrix[i - 1][j], weights[i - 1] + matrix[i - 1][max(0, j - scaled_values[i - 1])])

    # Reconstrucción de la solución
    
    extraCapacity = capacity * (1 + epsilon) # Según la consigna se puede exceder la capacidad en funcion de epsilon

    solutionIndex = 0
    for j in range(max_value, 0, -1):
        if matrix[n][j] <= extraCapacity:
            solutionIndex = j
            break

    selectedItems = []
    totalWeight = 0
    totalValue = 0

    for i in range(n, 0, -1):
        if solutionIndex <= 0:
            break
        # Si el peso del elemento actual es diferente al peso del elemento anterior significa que el elemento actual fue seleccionado
        if matrix[i][solutionIndex] != matrix[i - 1][solutionIndex]:
            selectedItems.append(i)
            totalWeight += weights[i - 1]
            totalValue += values[i - 1]
            solutionIndex -= scaled_values[i - 1]

    result = {
        "selectedItems": selectedItems,
        "totalValue": totalValue,
        "totalWeight": totalWeight
    }

    return result


# Pesos de los items
weights = [1, 7, 4, 5, 6, 8, 4, 7, 8, 4]
# Valores de los items
values = [15, 21, 35, 48, 53, 63, 74, 87, 99, 102]
# Capacidad máxima de la mochila
capacity = 25
# Parámetro de precisión epsilon (ε)
epsilon = 0.5

# Imprimir los datos de entrada

print("Datos de entrada")
print("=====================================")


for i in range(len(values)):
    print(f"Item {i + 1} - Peso: {weights[i]} - Valor: {values[i]}")

print("\nCapacidad de la mochila:", capacity)

print("\nEpsilon:", epsilon)


# Ejecutar la función de aproximación
result = knapsack_approx(weights, values, capacity, epsilon)

# Imprimir el valor óptimo aproximado
print("\nResultado")
print("=====================================")

for i in result["selectedItems"]:
    print(f"Item {i} - Peso: {weights[i - 1]} - Valor: {values[i - 1]}")

print("Valor total:", result["totalValue"])
print("Peso total:", result["totalWeight"])



