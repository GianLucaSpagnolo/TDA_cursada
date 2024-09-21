from time import time
import random
from ejercicio_2_v2 import greedy2


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
# print(greedy2(MAPA_2, n=9))


NS = [16, 32, 64, 128, 256]

for N in NS:
    edificios = int(0.2 * N**2)
    mapa = list(set([(random.randint(0, N-1), random.randint(0, N-1)) for _ in range(edificios)]))

    # print(mapa)

    # start_time1 = time()
    # result1 = sorted(list(greedy(mapa, n=N)))
    # end_time1 = time() - start_time1
    
    start_time2 = time()
    result2 = sorted(list(greedy2(mapa, n=N)))
    end_time2 = time() - start_time2

    # print(result1)
    # print(f"Greedy 1 --> Elapsed: {end_time1} seconds.")
    print(result2)
    print(f"Greedy 2 --> Elapsed: {end_time2} seconds.")
