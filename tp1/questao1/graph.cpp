#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <numeric>
#include <climits>
using namespace std;

// Estrutura do grafo: matriz de pares (fluxo, capacidade)
struct Aresta {
    int fluxo;
    int capacidade;
};

int BFS(vector<vector<Aresta>>& G, int s, int t, vector<int>& parent) {
    int n = G.size();
    fill(parent.begin(), parent.end(), -1);
    parent[s] = -2;

    queue<pair<int,int>> fila;
    fila.push({s, INT_MAX});

    while (!fila.empty()) {
        int u = fila.front().first;
        int fluxo = fila.front().second;
        fila.pop();

        for (int v = 0; v < n; v++) {
            if (parent[v] == -1 && G[u][v].capacidade - G[u][v].fluxo > 0) {
                parent[v] = u;
                int novo_fluxo = min(fluxo, G[u][v].capacidade - G[u][v].fluxo);
                if (v == t) return novo_fluxo;
                fila.push({v, novo_fluxo});
            }
        }
    }

    return 0;
}

int FordFulkerson(vector<vector<Aresta>>& G, int s, int t) {
    int fluxo_total = 0;
    vector<int> parent(G.size());

    while (true) {
        int fluxo = BFS(G, s, t, parent);
        if (fluxo == 0) break;
        fluxo_total += fluxo;

        int v = t;
        while (v != s) {
            int u = parent[v];
            G[u][v].fluxo += fluxo;
            G[v][u].fluxo -= fluxo;
            v = u;
        }
    }

    return fluxo_total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int nTimes, nCorrespondente, nJogos;
        if (!(cin >> nTimes >> nCorrespondente >> nJogos)) break;
        if (nTimes == 0) break;

        vector<int> pontos(nTimes, 0);
        vector<vector<int>> jogos(nTimes, vector<int>(nTimes, nCorrespondente));
        for (int i = 0; i < nTimes; i++) jogos[i][i] = 0;

        for (int i = 0; i < nJogos; i++) {
            int u, v;
            char op;
            cin >> u >> op >> v;

            if (op == '<') {
                pontos[v] += 2;
            } else {
                pontos[u] += 1;
                pontos[v] += 1;
            }

            jogos[u][v]--;
            jogos[v][u]--;
        }

        int jogosRestantes = accumulate(jogos[0].begin(), jogos[0].end(), 0);
        int pontosMax = pontos[0] + 2 * jogosRestantes;

        bool eliminado = false;
        for (int i = 1; i < nTimes; i++) {
            if (pontos[i] >= pontosMax) {
                eliminado = true;
                break;
            }
        }

        if (eliminado) {
            cout << "N\n";
            continue;
        }

        // Grafo: fonte + times + jogos + sumidouro
        // Índices: 
        // fonte = 0
        // jogos = 1..m
        // times = depois dos jogos
        // sumidouro = último nó

        int jogoCount = 0;
        for (int i = 1; i < nTimes; i++)
            for (int j = i + 1; j < nTimes; j++)
                if (jogos[i][j] > 0)
                    jogoCount++;

        int fonte = 0;
        int primeiroJogo = 1;
        int primeiroTime = primeiroJogo + jogoCount;
        int sumidouro = primeiroTime + (nTimes - 1);

        int nNos = sumidouro + 1;
        vector<vector<Aresta>> G(nNos, vector<Aresta>(nNos, {0, 0}));

        int somaTotal = 0;
        int jogoIndex = 0;

        for (int i = 1; i < nTimes; i++) {
            for (int j = i + 1; j < nTimes; j++) {
                if (jogos[i][j] == 0) continue;
                int jogoNode = primeiroJogo + jogoIndex++;
                int capacidade = 2 * jogos[i][j];
                somaTotal += capacidade;

                G[fonte][jogoNode].capacidade = capacidade;
                G[jogoNode][primeiroTime + i - 1].capacidade = capacidade;
                G[jogoNode][primeiroTime + j - 1].capacidade = capacidade;
            }
        }

        for (int i = 1; i < nTimes; i++) {
            int capacidade = pontosMax - pontos[i] - 1;
            if (capacidade < 0) capacidade = 0;
            G[primeiroTime + i - 1][sumidouro].capacidade = capacidade;
        }

        int fluxoMaximo = FordFulkerson(G, fonte, sumidouro);
        cout << (fluxoMaximo == somaTotal ? "Y\n" : "N\n");
    }

    return 0;
}
