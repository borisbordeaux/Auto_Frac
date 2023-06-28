#ifndef AUTOFRAC_UTILS_H
#define AUTOFRAC_UTILS_H

#include <algorithm>
#include <iostream>
#include <sstream>

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
std::vector<T> shiftVector(std::vector<T> const& vec) {
    std::vector<T> res;
    res.reserve(vec.size());
    for (std::size_t i = 1; i < vec.size(); ++i) {
        res.emplace_back(vec[i]);
    }
    res.emplace_back(vec[0]);
    return res;
}

inline std::vector<std::string> split(std::string const& str, char const& delimitor) {
    std::vector<std::string> strings;
    std::istringstream f(str);
    std::string s;
    while (std::getline(f, s, delimitor)) {
        strings.push_back(s);
    }
    return strings;
}

}

#endif //AUTOFRAC_UTILS_H
