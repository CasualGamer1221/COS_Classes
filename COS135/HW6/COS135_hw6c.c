#include <stdio.h>
#include <ctype.h>

/* Jeffery Parent
 * Finds the sum of all even numbers between 1 and a user inputted number */
int main(){
	/* Declares variables*/
	int num = 0, sum = 0;

	/* Asks user for number*/
	printf("Input a number larger than 1: ");

	/* Finds sum of all even numbers from 1 to num if input is a valid integer
	 * Else prints error statement*/	
	if (scanf("%d",&num) && num > 1){
		for(int i=1;i<=num;i++){
			if(i%2 == 0){
				sum += i;
			}
			else
				continue;
		}
		printf("Sum of even numbers between 1 and %d: %d\n",num,sum);
	}
	else{
		printf("Invalid Input!\n");
	}

	return 0;
}
