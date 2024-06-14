// O seguinte codigo foi originalmente feito em python e posteriormente passado para C++
// usando IA, já que a versão em Python não passou por tempo

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int n_q;
    cin >> n_q;
    
    while (n_q > 0) {
        int n;
        cin >> n;
        
        vector<int> result(n, 1);
        vector<string> query(n);
        
        for (int i = 0; i < n; ++i) {
            cin >> query[i];
        }
        
        for (int i = 0; i < n; ++i) {
            int atual = stoi(query[i]) - 1;
            while (atual != i) {
                atual = stoi(query[atual]) - 1;
                result[i]++;
            }
        }
        
        for (int i = 0; i < n; ++i) {
            cout << result[i] << " ";
        }
        cout << endl;
        n_q--;
    }
    
    return 0;
}