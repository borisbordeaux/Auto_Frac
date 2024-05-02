#ifndef AUTOFRAC_UTILS_H
#define AUTOFRAC_UTILS_H

#include <algorithm>
#include <sstream>
#include <vector>

namespace frac::utils {

inline std::string to_string(float value) {
    std::string res = std::to_string(value);
    std::replace(res.begin(), res.end(), ',', '.');
    return res;
}

template<typename T>
inline T mod(T a, T b) {
    return (a % b + b) % b;
}

template<typename T>
inline T pow(T base, T up) {
    if (up == static_cast<T>(0)) {
        return static_cast<T>(1);
    } else {
        return base * pow(base, up - static_cast<T>(1));
    }
}

template<typename T>
std::vector<T> shiftVector(std::vector<T> const& vec) {
    std::vector<T> res;
    res.reserve(vec.size());
    for (std::size_t i = 1; i < vec.size(); ++i) {
        res.emplace_back(vec[i]);
    }
    res.emplace_back(vec[0]);
    return res;
}

inline std::vector<std::string> split(std::string const& str, char const& delimiter) {
    std::vector<std::string> strings;
    std::istringstream f(str);
    std::string s;
    while (std::getline(f, s, delimiter)) {
        strings.push_back(s);
    }
    return strings;
}

inline std::vector<std::string> split(std::string const& str, std::string const& delimiter) {
    std::vector<std::string> strings;
    std::size_t start = 0, end;
    while ((end = str.find(delimiter, start)) != std::string::npos) {
        strings.push_back(str.substr(start, end - start));
        start = end + delimiter.length();
    }
    strings.push_back(str.substr(start));
    return strings;
}

inline std::vector<float> get_bezier_transformation(unsigned int i, unsigned int n) {
    float denominator = static_cast<float>(n * n);
    return { static_cast<float>((i - n) * (i - n)) / denominator,
             static_cast<float>((i - n) * (1 + i - n)) / denominator,
             static_cast<float>((1 + i - n) * (1 + i - n)) / denominator,
             static_cast<float>(2 * i * (n - i)) / denominator,
             static_cast<float>(n + 2 * i * n - 2 * i * (i + 1)) / denominator,
             static_cast<float>(-2 * (1 + i - n) * (1 + i)) / denominator,
             static_cast<float>(i * i) / denominator,
             static_cast<float>(i * (1 + i)) / denominator,
             static_cast<float>((i + 1) * (i + 1)) / denominator
    };
}

inline std::pair<float, float> coordOfPointOnQuadCurveAt(float t, float p0x, float p0y, float p1x, float p1y, float p2x, float p2y) {
    return { (1.0f - t) * (1.0f - t) * p0x + 2.0f * t * (1.0f - t) * p1x + t * t * p2x, (1.0f - t) * (1.0f - t) * p0y + 2.0f * t * (1.0f - t) * p1y + t * t * p2y };
}

inline std::pair<float, float> coordOfPointOnLineAt(float t, float p0x, float p0y, float p1x, float p1y) {
    return { (1 - t) * p0x + t * p1x, (1 - t) * p0y + t * p1y };
}

}

#endif //AUTOFRAC_UTILS_H
