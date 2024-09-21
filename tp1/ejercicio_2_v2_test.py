from time import time
from ejercicio_2_v2 import greedy
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
# print(greedy(MAPA_1, n=4))

# [(5, 2), (1, 6), (6, 7), (0, 0)]
# print(greedy(MAPA_2, n=9))


NS = [16, 32, 64, 128, 256]

for N in NS:
    edificios = int(0.2 * N**2)
    mapa = list(set([(random.randint(0, N-1), random.randint(0, N-1)) for _ in range(edificios)]))

    # print(mapa)

    start_time = time()
    result = greedy(mapa, n=N)
    end_time = time() - start_time

    # print(len(result))
    print(f"Elapsed: {end_time} seconds.")


# Elapsed: 0.0010013580322265625 seconds.
# Elapsed: 0.016596317291259766 seconds.
# Elapsed: 0.2564847469329834 seconds.
# Elapsed: 4.357736825942993 seconds.
# Elapsed: 67.72359251976013 seconds.