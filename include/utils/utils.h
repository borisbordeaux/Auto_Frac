#ifndef AUTOFRAC_UTILS_H
#define AUTOFRAC_UTILS_H

#include <algorithm>
#include <iostream>

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

}

#endif //AUTOFRAC_UTILS_H
