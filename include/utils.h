#ifndef AUTOFRAC_UTILS_H
#define AUTOFRAC_UTILS_H

#include <algorithm>
#include <iostream>

namespace frac {

class Utils {
public:
    static std::string to_string(float value) {
        std::string res = std::to_string(value);
        std::replace(res.begin(), res.end(), ',', '.');
        return res;
    }

    template<typename T>
    static T mod(T a, T b) {
        return (a % b + b) % b;
    }
};

} // frac

#endif //AUTOFRAC_UTILS_H
