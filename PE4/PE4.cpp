#include<string>
#include<iostream>
using namespace std;

bool is_palindrome(int n) {
  string n_str = to_string(n);
  string::reverse_iterator rit=n_str.rbegin();
  string::iterator it=n_str.begin();

  
  for(int i=0; i<n_str.length()/2; i++) {
    if(*it != *rit) {
      return false;
    }
    it++; rit++;
  }

  return true;
}

int main() {
  int largest = 323;
  
  for(int i=999; i>99; i--) {
    for(int j=999; j>99; j--) {
      if(i*j > largest && is_palindrome(i*j)) {
	largest = i*j;
      }
    }
  }
  cout << largest << endl;
  return 0;
}
