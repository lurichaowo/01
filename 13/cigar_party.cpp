#include <iostream>

bool cigar_party(int cigars, bool is_weekend){
	if (cigars < 40){
		return false;
	}
	if (is_weekend && cigars >= 40){
		return true;
	}
	else if (!is_weekend){
		if (cigars >= 40 && cigars <= 60){
			return true;
		}
		else if (cigars < 40 || cigars > 60){
			return false;
		}
	}
}

int main(){
	bool a = cigar_party(30, true);
	bool b = cigar_party(50, true);
	bool c = cigar_party(55, false);
	bool d = cigar_party(70, true);
	bool e = cigar_party(75, false);
	std::cout << std::boolalpha << a << std::endl;
	std::cout << std::boolalpha << b << std::endl;
	std::cout << std::boolalpha << c << std::endl;
	std::cout << std::boolalpha << d << std::endl;
	std::cout << std::boolalpha << e << std::endl;
}