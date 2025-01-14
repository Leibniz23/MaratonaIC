// Código feito pelo Samuel (PED) antes da aula

#include <bits/stdc++.h>
#define MAX 1000
using namespace std;

typedef pair<int, int> coord;

bool taken[MAX][MAX];
int h[MAX][MAX];
priority_queue <pair<int,coord>> pq;
vector<coord> possible_neighbors = {
    {-1, 0}, {0,-1}, {1,0}, {0,1}
};
void process(int i, int j, int M, int N){
    taken[i][j] = true;
    for (auto &[diff_i, diff_j]:possible_neighbors){
        int row=i+diff_i, col=j+diff_j;
        if (row >=0 && row < M && col>=0 && col < N && !taken[row][col]){
            int w = max(0, h[row][col] - h[i][j]);
            pq.push({-w, {row,col}});
        }
    }
}

int prim(int source_i, int source_j, int M, int N){
    process(source_i, source_j, M, N);
    int max_csr = 0;
    while (!pq.empty() && !taken[M-1][N-1]){
        auto [w, ij] = pq.top(); pq.pop();
        w = -w;
        auto &[i, j] = ij;
        if (taken[i][j]) continue;
        max_csr = max(w, max_csr);
        process(i, j, M, N);
    }
    return max_csr;
}

int main() {
    int M, N;
    cin >> M >> N;
    for(int i = 0; i < M; i++){
        for (int j = 0; j < N; j++){
            cin >> h[i][j];
            taken[i][j] = false;
        }
    }
    cout << prim(0, 0, M, N) << endl;
    return 0;
}