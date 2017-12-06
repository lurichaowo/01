#include <iostream>
#include <string>
#include <algorithm>

using std::cout;
using std::endl;
using std::string;

bool is_vowel(char a){
	if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u'){
		return true;
	}
	else {
		return false;
	}
}

std::string piglatin(std:: string str){
	int l = str.length();
	for (int i = 0; i < l; ++i)
	{
		str[i] = tolower(str[i]);
	}
	string s;
	if (is_vowel(str[0])){
		s = str + "ay";
		return s;
	}
	else{
		s = str.substr(1,l) + str[0] + "ay";
		return s;
	}
}

int main(){
	cout << piglatin("HIPPO") << endl;
	cout << piglatin("aunt") << endl;
}