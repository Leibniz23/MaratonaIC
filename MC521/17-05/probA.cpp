// Este código foi escrito por mim mesmo em Python, mas estava dando TLE, então usei o chat GPT apenas para trasformar em C++
//

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int INF = 2147483647;

vector<int> dijkstra(vector<vector<pair<int, int>>>& g, int s) {
    int n = g.size();
    vector<int> dist(n, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
    dist[s] = 0;
    heap.push({0, s});
    
    while (!heap.empty()) {
        auto [key, v] = heap.top();
        heap.pop();
        for (auto& adj : g[v]) {
            int u = adj.first;
            int w = adj.second;
            if (dist[u] > dist[v] + w) {
                dist[u] = dist[v] + w;
                heap.push({dist[u], u});
            }
        }
    }
    return dist;
}

int main() {
    int n;
    cin >> n;
    int count = 1;
    for (int i = 0; i < n; ++i) {
        int vertex, edges, s, t;
        cin >> vertex >> edges >> s >> t;
        vector<vector<pair<int, int>>> g(vertex);
        for (int j = 0; j < edges; ++j) {
            int u, v, w;
            cin >> u >> v >> w;
            g[u].emplace_back(v, w);
            g[v].emplace_back(u, w);
        }
        vector<int> dist = dijkstra(g, s);
        int result = dist[t];
        if (result >= INF) {
            cout << "Case #" << count << ": unreachable" << endl;
        } else {
            cout << "Case #" << count << ": " << result << endl;
        }
        count++;
    }
    return 0;
}