#include <iostream>
#include <typeinfo>
#include <bits/cpp_type_traits.h>

using namespace std;

void printss(__true_type* type)
{
	cout << "true_type" << endl;
}

int main()
{
	typedef __is_integer<int>::__type* type;
	printss(type());
}
