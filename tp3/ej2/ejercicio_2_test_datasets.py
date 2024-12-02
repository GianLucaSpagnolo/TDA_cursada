import os
import time
import ejercicio_2 as ej2


datasets = [
    # { "epsilon1" : "...", "capacity1": "...", "elementCount1": "...", "elements": [ (weight1, value1), (weight1, value2), ... ] },
    # { "epsilon2" : "...", "capacity2": "...", "elementCount2": "...", "elements": [ (weight1, value1), (weight1, value2), ... ] },
]


path = os.path.dirname(os.path.abspath(__file__))

for epsilon in os.listdir(path):
    epsilon_path = os.path.join(path, epsilon)
    if os.path.isdir(epsilon_path):
        for filename in os.listdir(epsilon_path):
            if filename.endswith(".csv"):
                with open(os.path.join(epsilon_path, filename)) as f:
                    epsilon_value = float(f.readline().strip())
                    capacity = int(f.readline().strip())
                    element_count = int(f.readline().strip())
                    elements = []
                    for _ in range(element_count):
                        weight, value = map(int, f.readline().strip().split(","))
                        elements.append((weight, value))
                    datasets.append({
                        "epsilon": epsilon_value,
                        "capacity": capacity,
                        "elementCount": element_count,
                        "elements": elements
                    })


for dataset in datasets:

    epsilon = dataset['epsilon']
    capacity = dataset['capacity']

    print("------------------------------------------")
    print(f"Epsilon: {epsilon}")
    print(f"Capacity: {capacity}")
    print(f"Element count: {dataset['elementCount']}\n")

    start_time = time.time()

    solution = ej2.knapsack_approx(
        [e[0] for e in dataset["elements"]], 
        [e[1] for e in dataset["elements"]], 
        dataset["capacity"], 
        dataset["epsilon"]
    )

    elapsed_time = time.time() - start_time

    print(solution)

    # asserts
    # assert solution["totalValue"] >= optimal_value
    assert solution["totalWeight"] <= (1 + epsilon) * capacity

    print(f"Elapsed time: {elapsed_time}")

    print("------------------------------------------")

