// Find the sum of all the multiples of 3 or 5 below 1000

#include<stdio.h>

int i_sum_1_to_n(int n) {
	return n * (n+1)/2;
}
int three_five_sum_below(int n) {
	int threes = (n-1) / 3;
	int fives = (n-1)/5;
	int fifteens = (n-1)/15;
	return (3 * i_sum_1_to_n(threes)) + (5 * i_sum_1_to_n(fives)) - 
		   (15 * i_sum_1_to_n(fifteens));
}
int main() {
	int i = three_five_sum_below(1000);
	printf("%d\n", i);
	return 0;
}

// Answer: 233168
