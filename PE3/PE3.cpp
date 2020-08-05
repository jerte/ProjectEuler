#include<stdio.h>

int largest_prime_factor(long n) {
	int largest = 1;
	int i = 2;
	while( n!= 1 ) {
		while( n % i ==0 ) {
			if( i > largest ) {
				largest = i;
			}
			n = n / i;
		}
		i += 1;
	}
	return largest;
}

int main() {
	printf("%d\n", largest_prime_factor(600851475143));
	return 0;
}

// answer = 6857
