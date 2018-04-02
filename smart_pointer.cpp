/*
 * Smart pointer implementation
 */
#include <iostream>

template <class T>
class smartPtr
{
public:
	explicit smartPtr(T *p=NULL){
		ptr = p;
	}
	~smartPtr(){
		delete ptr; 
	}

	//override derefence operator
	T & operator *(){
		return *ptr;
	}

	//override arrow operator
	T * operator -> (){
		return ptr;
	}
private:
	T *ptr;
};

int main(){
	smartPtr<int> ptr(new int());
	*ptr = 20;
	std::cout<<*ptr<<std::endl;
	return 0;
}
