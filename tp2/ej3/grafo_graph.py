import matplotlib.pyplot as plt
import networkx as nx

# Datos del grafo
edges = [
    (1, 4, 15),
    (2, 3, 15),
    (3, 6, 20),
    (2, 4, 10),
    (2, 5, 10),
    (2, 6, 10),
    (4, 5, 5),
    (5, 6, 5)
]

# Crear el grafo
G = nx.Graph()

# Agregar los bordes al grafo
for u, v, cost in edges:
    G.add_edge(u, v, weight=cost)

# Posiciones para los nodos
pos = nx.spring_layout(G, k=0.9)

# Dibujar el grafo
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_color='black', font_weight='bold')

# Dibujar las etiquetas de los bordes
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Mostrar la gráfica
plt.title("Grafo de Costos")
plt.axis('off')  # Ocultar el eje
plt.show()
