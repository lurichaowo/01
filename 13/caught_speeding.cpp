#include <iostream>

int caught_speeding(int spd, bool is_bday){
	int i = 0;
	if (is_bday){
		if (spd <= 65){
			return i;
		}
		else if (spd > 85){
			i = 2;
			return i;
		}
		else{
			i = 1;
			return i;
		}
	}
	else if (!is_bday){
		if (spd <= 60){
			return i;
		}
		else if (spd > 80){
			i = 2;
			return i;
		}
		else{
			i = 1;
			return i;
		}
	}
}

int main(){
	bool a = caught_speeding(50, true);
	bool b = caught_speeding(60, true);
	bool c = caught_speeding(70, false);
	bool d = caught_speeding(80, true);
	bool e = caught_speeding(90, false);
	std::cout << std::boolalpha << a << std::endl;
	std::cout << std::boolalpha << b << std::endl;
	std::cout << std::boolalpha << c << std::endl;
	std::cout << std::boolalpha << d << std::endl;
	std::cout << std::boolalpha << e << std::endl;
}