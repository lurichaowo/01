#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

std::string line(int l, std::string c){
  string a = "";
  for (int i = 0; i < l; ++i)
  {
    a = a + c[i];
  }
  return a;
}

std::string rect(int w, int h) {
  string r = "";
  for (int i = 0; i < w; ++i)
  {

    for (int j = 0; j < h; ++j)
    {
      r = r + "*";
    }
    r = r + "\n";   
  }
  return r;
}

/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
  string b = "";
  /*for (int i = 0; i < h; ++i)
  {
    for (int j = i; j >= 0; --j)
    {
      b = b + "*";
    }
    b = b + " \n";
  }    */
  for (int i = 0; i < h; ++i)
  {
    int stars = i + 1;
    while(stars > 0){
      b = b + "*";
      stars--;
    }
    int spaces = h - i -1;
    while (spaces > 0){
      b = b+ " ";
      spaces--;
    } 
    b = b + "\n";
  }
  return b;
}


/*
   *
  ***
 *****
 */
std::string tri2(int h) {
  string c = "";
  h = h+1;
  for (int i = 0; i < h; ++i){
    int spaces = h - i - 1; // # of spaces in each line is equal to h-i-1
    while (spaces > 0){
      c = c + " ";
      spaces--;
    }
    int stars = (i*2)-1; // # of stars = (h*2)-1
    while (stars > 0){
      c = c + "*";
      stars--;
    }
    c = c + "\n";
  }
  return c;
}

/*
  *
 **
***
 */
std::string tri3(int h) {
  string d = "";
  for (int i = 0; i < h; ++i)
  {
    int spaces = h - i -1;
    while (spaces > 0){
      d = d+ " ";
      spaces--;
    }
    int stars = i + 1;
    while(stars > 0){
      d = d + "*";
      stars--;
    } 
    d = d + "\n";
  }
  return d;
}
int main(){
  string s="hello";
  cout<<s<<endl;
  cout << line(3,s) << endl;
  cout << rect(3,5) << endl;
  cout << tri1(4) << endl;
  cout << tri2(3) << endl;
  cout << tri3(3) << endl;
}

