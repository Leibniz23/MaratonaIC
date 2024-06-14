// Este código foi escrito em Python e não passou por tempo, então traduzi para C++ usando o ChatGPT
// para tentar passar no tempo

#include <iostream>
#include <vector>
#include <string>

std::pair<std::string, std::string> calcular(std::vector<std::pair<int, int>>& pontos, int x) {
    for (const auto& ponto : pontos) {
        double m = -(static_cast<double>(ponto.second) / (ponto.first + 1));
        double n = -(static_cast<double>(ponto.second) / (ponto.first - 1));
        int acima_m = 0, acima_n = 0;
        for (const auto& cherry : pontos) {
            if ((static_cast<double>(cherry.second) / cherry.first) > m)
                acima_m++;
            else if ((static_cast<double>(cherry.second) / cherry.first) > n)
                acima_n++;
        }
        if (acima_m == x)
            return {std::to_string(ponto.first + 1), std::to_string(ponto.second)};
        else if (acima_n == x)
            return {std::to_string(ponto.first - 1), std::to_string(ponto.second)};
    }
    return {"", ""}; // Se nada for encontrado, retornamos strings vazias
}

int main() {
    int n;
    std::cin >> n;
    
    while (n != 0) {
        std::vector<std::pair<int, int>> pontos;
        for (int i = 0; i < 2 * n; ++i) {
            int x, y;
            std::cin >> x >> y;
            pontos.emplace_back(x, y);
        }
        auto resultado = calcular(pontos, n);
        std::cout << resultado.first << " " << resultado.second << std::endl;
        std::cin >> n;
    }
    
    return 0;
}
