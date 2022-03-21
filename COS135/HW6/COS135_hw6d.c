#include <stdio.h>

/* Jeffery Parent
 * Outputs the fibonaccii series up to a user specified number*/
int main(){

	/*initialize first and second term // and end value*/
	unsigned long int num1 = 0, num2 = 1;
	long int end = 0;
	
	/*Initialize the next term (Third)*/
	unsigned long int nextterm = num1 + num2;

	/*get end number from user*/
	printf("Enter a number: ");
	scanf("%ld",&end);

	/*Finds and prints the fibonacci sequence until the next term printed is above the specified value*/
	if(end > 0){
		printf("Fibonacci Series: %lu, %lu",num1,num2);
		while (nextterm < end){
			printf(", %lu", nextterm);
			num1 = num2;
			num2 = nextterm;
			nextterm = num1 + num2;
			
		}
		printf("\n");

	}
	else{
		printf("Invalid input - please try a positive integer\n");
	}

	return 0;
}
