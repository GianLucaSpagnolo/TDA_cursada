from ejercicio_2 import posiciones_restaurante

MAPA_1 = [
    [" ","X"," "," ","X"," "],
    ["X"," "," "," "," "," "],
    [" "," "," "," "," "," "],
    ["X"," "," "," "," ","X"],
    [" "," "," ","X"," "," "],
    [" "," "," "," ","X"," "]
]

MAPA_2 = [
    [" "," "," "," "],
    [" ","X"," "," "],
    [" "," "," "," "],
    [" "," ","X","X"],
]

MAPA_3 = [
    [" ","X"," "," "," "," "],
    ["X"," "," "," ","X"," "],
    [" "," "," "," "," "," "],
    ["X"," "," ","X"," "," "],
    [" ","X"," "," "," "," "],
    [" "," "," "," "," ","X"]
]

# Poner los mapas ordenados por numero!
# [MAPA_K, [(X1, EXPECTED_SIZE_1), (X2, EXPECTED_SIZE_2), ...]]
TESTS = [
    [MAPA_1, [(1, 4), (2, 2)]],
    [MAPA_2, [(1, 1)]],
    [MAPA_3, [(1, 4)]],
]

i = 0

for test_set in TESTS:
    i += 1
    name = f"MAPA_{i}"
    mapa = test_set[0]
    configs = test_set[1]
    for config in configs:
        X = config[0]
        expected_size = config[1]

        restaurantes = posiciones_restaurante(mapa, X)
        try:
            assert len(restaurantes) == expected_size
            print(f"Test with X = {X} for map {name} passed successfully!")
        except AssertionError:
            print(f"---- Could not find the optimal case for X = {X} and map {name} ----")
        