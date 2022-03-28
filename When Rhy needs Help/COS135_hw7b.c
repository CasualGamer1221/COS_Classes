#include <stdio.h>
/* Jeffery Parent
 * 5 functions that do various things(as labelled) with an inputted number*/

/* Prints all natural numbers for 1 to the inputted number*/
void nat(int number){
	for(int num1=1;num1<=number;num1++ ){
		printf(" %d,",num1);
	}
}

/* Prints all natural numbers from inputted number to 1(above function in reverse)*/
void nat_rev(int number){
	for(int num1=number;num1>0;num1-- ){
                printf(" %d,",num1);
        }
}

/*prints all even numbers from 1 to n*/
void even(int number){
	for(int num1=1;num1<=number;num1++){
		if(!(num1%2)){
			printf(" %d,",num1);
		}
        }
}

/*prints all odd numbers from 1 to n*/
void odd(int number){
        for(int num1=1;num1<=number;num1++){
                if(num1%2){
                        printf(" %d,",num1);
                }
        }
}

/*returns the sum of all natural numbers between 1 and n*/
int nat_sum(int number){
	int sum = 0;
        for(int num1=1;num1<=number;num1++ ){
               sum += num1;
        }
	return sum;
}

/*Calls all functions and recieves & checks user inputted number*/
int main(){
	int number = 0;
	printf("Enter an integer larger than 10: ");
	if(scanf("%d", &number) && number > 10){
		printf("\n\n");

		nat(number);
		printf("\n\n");

		nat_rev(number);
	        printf("\n\n");	
	
		even(number);
		printf("\n\n");
	
		odd(number);
		printf("\n\n");

		int sum = nat_sum(number);
		printf("%d\n\n", sum);

	}

	return 0;
}
