#include<iostream>  // cout/cin
#include<map>     
#include<math.h>    // sqrt
using namespace std;

bool is_prime(int n) {
  int sq = (int) sqrt(n) + 1;
  for(int i=2; i<sq; i++) {
    if(n%i==0) {
      return false;
    }
  }
  return true;
}

int main() {
  //prime factors numbers 1-20
  //multiply
  map<int, int> prime_factor_count;
  
  for(int i=2; i<21; i++) {
    int j=i;
    int prime_divisor=2;
    while(j!=1) {
      int prime_divisor_count=0;
      while(j%prime_divisor==0) {
	prime_divisor_count++;
	j=j/prime_divisor;
      }
      if(prime_factor_count.count(prime_divisor)) {
	if(prime_factor_count[prime_divisor] < prime_divisor_count) {
	  prime_factor_count[prime_divisor] = prime_divisor_count;
	}
      } else {
	prime_factor_count[prime_divisor] = prime_divisor_count;
      }
      if(prime_divisor==2) {
        prime_divisor++;
      } else {
	prime_divisor += 2;
      }
      while(!is_prime(prime_divisor)) {
	prime_divisor+=2;
      }
    }
  }
  // unpack prime_factor_count
  int value=1;
  for(map<int,int>::iterator it=prime_factor_count.begin();
      it!=prime_factor_count.end(); it++) {
    for(int i=0; i<it->second; i++) {
      value = value * it->first;
    }
  }
  cout << value << endl;
  return 0;
}   
