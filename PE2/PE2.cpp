#include<stdio.h>

int even_fib_sum_under(int n) {
	int f1 = 1;
	int f2 = 1;
	int sum=0;
	while( f1+f2 < n ) {
		int temp = f2;
		f2 = f1+f2;
		f1 = temp;
		
		if( f2 % 2==0 ) {
			sum += f2;
		}
	}
	return sum;
}

int main() {
	printf("%d\n", even_fib_sum_under(4000000));
	return 0;
}

// answer: 4613732
