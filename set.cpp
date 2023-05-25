#include "set.h"

template<class T>
Set<T>::Set()
{
}

template<class T>
void Set<T>::append(T item)
{
	for (T elt : this->data)
	{
		if (item == elt)
			return;
	}

	this->data.push_back(item);
}

template<class T>
T Set<T>::operator[](int index) const
{
	return this->data[index];
}

template<class T>
std::size_t Set<T>::len() const
{
    return this->data.size();
}
