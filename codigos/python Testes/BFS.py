import networkx as nx
import random
from collections import deque

def bfs_limited(G, start, max_dist=6):
    dist = {v: float("inf") for v in G.nodes()}
    dist[start] = 0
    fila = deque([start])

    while fila:
        u = fila.popleft()
        if dist[u] == max_dist:
            continue
        for v in G.neighbors(u):
            if dist[v] == float("inf"):
                dist[v] = dist[u] + 1
                fila.append(v)

    return dist


def seis_graus(G, max_dist=6):
    for s in G.nodes():
        dist = bfs_limited(G, s, max_dist=max_dist)
        if any(d == float("inf") for d in dist.values()):
            return False
    return True


# ---------------- Simulação ---------------- #

# Criar uma rede aleatória com 5000 usuários
# Modelo Erdős–Rényi G(n, p)
n = 50000   # número de usuários
p = 0.05  # probabilidade de amizade entre dois usuários

print("Gerando rede...")
G = nx.erdos_renyi_graph(n, p)

print("Número de usuários:", G.number_of_nodes())
print("Número de amizades:", G.number_of_edges())

# Rodar o teste dos seis graus
print("Verificando teoria dos seis graus...")
resultado = seis_graus(G)

print("A teoria dos seis graus vale?", resultado)
