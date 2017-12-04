#include <iostream>

int lone_sum(int a, int b, int c){
	int i = 0;
	if (a == b){
		if (a == c){
			return i;
		}
		else if (a != c){
			i = c;
			return i;
		}
	}
	if (a != b){
		if (b == c){
			i = a;
			return i;
		}
		else if (a == c){
			i = b;
			return i;
		}
		else if (b != c){
			i = a + b + c;
			return i;
		}
	}
}

int main(){
	int a = lone_sum(1, 2, 3);
	int b = lone_sum(5, 2, 1);
	int c = lone_sum(5, 5, 1);
	int d = lone_sum(3, 6, 4);
	int e = lone_sum(10, 10, 1);
	std::cout << std::boolalpha << a << std::endl;
	std::cout << std::boolalpha << b << std::endl;
	std::cout << std::boolalpha << c << std::endl;
	std::cout << std::boolalpha << d << std::endl;
	std::cout << std::boolalpha << e << std::endl;
}