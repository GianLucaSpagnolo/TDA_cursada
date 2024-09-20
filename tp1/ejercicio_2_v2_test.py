from time import time
from ejercicio_2 import posiciones_restaurante
import random


MAPA_1 = [
    (1,1),
    (3,2),
    (3,3)
]

MAPA_2 = [
    (0,0),
    (0,5),
    (1,2),
    (1,6),
    (2,5),
    (2,8),
    (3,3),
    (3,6),
    (4,0),
    (5,2),
    (5,5),
    (6,4),
    (6,7),
    (7,1),
    (7,4),
    (8,7)
]


# Contraejemplo: para x=1, el optimo seria por ejemplo (2,2)
# [(3, 2), (1, 1)]
# print(posiciones_restaurante(MAPA_1, n=4, x=1))

# [(5, 2), (1, 6), (6, 7), (0, 0)]
# print(posiciones_restaurante(MAPA_2, n=9, x=2))


N = 160
edificios = int(0.2 * N**2)
mapa = list(set([(random.randint(0, N-1), random.randint(0, N-1)) for _ in range(edificios)]))

# print(mapa)

start_time = time()
result = posiciones_restaurante(mapa, n=N)
end_time = time() - start_time

print(len(result))
print(f"Elapsed: {end_time} seconds.")


# N = 10   ->  0.0
# n = 20   ->  0.006158113479614258
# n = 40   ->  0.2549169063568115
# n = 80   -> 14.387941598892212