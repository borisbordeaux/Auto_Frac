#ifndef AUTOFRAC_SET_H
#define AUTOFRAC_SET_H

#include <algorithm>
#include <vector>

namespace frac {

template<typename T>
class UniqueVector {
public:
    void add(T const& elt);
    std::size_t size() const;
    T const& operator[](std::size_t index) const;
    std::vector<T> const& data() const;
    void clear();

private:
    std::vector<T> m_data;
};

template<typename T>
void frac::UniqueVector<T>::clear() {
    this->m_data.clear();
}

template<typename T>
std::vector<T> const& frac::UniqueVector<T>::data() const {
    return this->m_data;
}

template<typename T>
void frac::UniqueVector<T>::add(T const& elt) {
    if (std::find(this->m_data.begin(), this->m_data.end(), elt) == this->m_data.end()) {
        this->m_data.emplace_back(elt);
    }
}

template<typename T>
std::size_t frac::UniqueVector<T>::size() const {
    return this->m_data.size();
}

template<typename T>
T const& frac::UniqueVector<T>::operator[](std::size_t index) const {
    return this->m_data[index];
}

} // frac

#endif //AUTOFRAC_SET_H
