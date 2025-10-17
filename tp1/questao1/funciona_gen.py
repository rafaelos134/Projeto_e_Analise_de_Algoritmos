from collections import deque

def BFS(G, inicio, fim):
    parent = {no: None for no in G}
    fila = deque([inicio])
    path_found = False
    
    while fila:
        u = fila.popleft()
        if u == fim:
            path_found = True
            break
        
        for v, (fluxo, capacidade) in G[u].items():
            if parent[v] is None and capacidade - fluxo > 0:
                parent[v] = u
                fila.append(v)
    
    if not path_found:
        return 0, []

    
    caminho = []
    fluxo_gargalo = float('inf')
    v = fim
    while v != inicio:
        u = parent[v]
        fluxo_gargalo = min(fluxo_gargalo, G[u][v][1] - G[u][v][0])
        caminho.append(v)
        v = u
    caminho.append(inicio)
    
    return fluxo_gargalo, list(reversed(caminho))


def FordFulkerson(G, s, t):
    fluxo_total = 0
    while True:
        fluxo_minimo, caminho = BFS(G, s, t)
        if fluxo_minimo == 0:
            break
        
        fluxo_total += fluxo_minimo
        
        for i in range(len(caminho) - 1):
            u, v = caminho[i], caminho[i+1]
            G[u][v][0] += fluxo_minimo
            G[v][u][0] -= fluxo_minimo
            
    return fluxo_total

def add_aresta(G, u, v, capacidade):
    if u not in G: G[u] = {}
    if v not in G: G[v] = {}
    G[u][v] = [0, capacidade] 
    G[v][u] = [0, 0]        

def main():
    while True:
        try:
            linha = input()
            if not linha: break
            n_times, n_correspondentes, n_jogos = map(int, linha.split())
        except (IOError, ValueError):
            break

        if n_times == 0:
            break

        pontos = [0] * n_times
        jogos_restantes = [[n_correspondentes] * n_times for _ in range(n_times)]

        for i in range(n_times):
            jogos_restantes[i][i] = 0

        for _ in range(n_jogos):
            u, op, v = input().split()
            u, v = int(u), int(v)
            
            if op == '<': # v venceu u
                pontos[v] += 2
            else: # empate
                pontos[u] += 1
                pontos[v] += 1
            
            jogos_restantes[u][v] -= 1
            jogos_restantes[v][u] -= 1

        
        jogos_restantes_time0 = sum(jogos_restantes[0])
        pontuacao_maxima_time0 = pontos[0] + (2 * jogos_restantes_time0)

        impossivel = False
        for i in range(1, n_times):
            if pontos[i] >= pontuacao_maxima_time0:
                impossivel = True
                break
        if impossivel:
            print("N")
            continue

        
        fonte = 's'
        sumidouro = 't'
        T = {}
        
        soma_pontos_disponiveis = 0

        
        for i in range(1, n_times):
            for j in range(i + 1, n_times):
                if jogos_restantes[i][j] > 0:
                    node_jogo = f"jogo_{i}_{j}"
                    capacidade_jogo = 2 * jogos_restantes[i][j]
                    soma_pontos_disponiveis += capacidade_jogo
                    
                    add_aresta(T, fonte, node_jogo, capacidade_jogo)
                    add_aresta(T, node_jogo, f"time_{i}", capacidade_jogo)
                    add_aresta(T, node_jogo, f"time_{j}", capacidade_jogo)

      
        if not T:
            print("Y")
            continue

        
        for i in range(1, n_times):
            
            capacidade = pontuacao_maxima_time0 - pontos[i] - 1
            if capacidade < 0:
                capacidade = 0
            add_aresta(T, f"time_{i}", sumidouro, capacidade)
        
        fluxo_maximo = FordFulkerson(T, fonte, sumidouro)

       
        if fluxo_maximo >= soma_pontos_disponiveis:
            print("Y")
        else:
            print("N")

if __name__ == "__main__":

    main()
