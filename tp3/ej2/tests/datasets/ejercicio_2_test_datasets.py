import os
from ...ejercicio_2 import knapsack_approx


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
    solution = knapsack_approx(
        [e[0] for e in dataset["elements"]], 
        [e[1] for e in dataset["elements"]], 
        dataset["capacity"], 
        dataset["epsilon"]
    )

    print(solution)

    # ...

