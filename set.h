#ifndef AS_SET_H
#define AS_SET_H

#include <vector>

template<class T>
class Set
{
	public:
		Set();
		void append(T item);
		T operator[](int index) const;
        std::size_t len() const;

	private:
		std::vector<T> data;
};

#endif // AS_SET_H
