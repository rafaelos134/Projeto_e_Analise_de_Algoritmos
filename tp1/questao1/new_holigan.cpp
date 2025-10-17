#include <iostream>
#include <vector>

struct graph{
    int pontucao;
    int v;
    int flux;
    int limite;
};


void addAresta(std::vector <graph> G[], int u, int v,int flux, int limit, int pontuacao){
    G[u].push_back({pontuacao,v,flux,limit});
    // G[v].push_back(graph (u,flux,limit));
}




int main() {

    int nTimes;
    int nCorrespondente;
    int nJogos;

    std::cin >> nTimes;
    std::cin >> nCorrespondente;
    std::cin >> nJogos;

    std::vector<graph> G[nTimes];
    std::vector<graph> T[nTimes];


    for (int i = 0; i < nTimes; i++) {
        for (int j = i+1; j < nTimes; j++) {
            if (i != j) {
                addAresta(G, i, j, 0, nCorrespondente,0);
            }
        }
    }

    for (int i = 0; i < nJogos; i++){
        int flux;
        int nodeU;
        std::string operador;
        int nodeV;

        std::cin >> nodeU;
        std::cin >> operador;
        std::cin >> nodeV;
    
        if (operador == "<"){
            // Caso ganhe o fluxo e definido para 2
            flux = 2;
        }else{
            // Caso empate o fluxo e definido para 1
            flux = 1;
        }


        for (auto &aresta : G[nodeU]) {
            if (std::get<0>(aresta) == nodeV) {
                std::get<1>(aresta) += flux;     
                break;
            }
    }

    }





}
