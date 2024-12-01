import ejercicio_2 as ej2

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
result = ej2.knapsack_approx(weights, values, capacity, epsilon)

# Imprimir el valor óptimo aproximado
print("\nResultado")
print("=====================================")

for i in result["selectedItems"]:
    print(f"Item {i} - Peso: {weights[i - 1]} - Valor: {values[i - 1]}")

print("Valor total:", result["totalValue"])
print("Peso total:", result["totalWeight"])




