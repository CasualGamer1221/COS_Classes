#include <stdio.h>

/* JEFFERY PARENT
 * Collects three values from the user and if at least two values match, outputs that value, else outputs ERROR*/

int main(){
	/*initializes variables and collects three numbers from the user*/
	int num1=0,num2=0,num3=0;

	printf("Enter first number: ");
	scanf("%*c%d",&num1);

	printf("Enter second number: ");
	scanf("%*c%d",&num2);

	printf("Enter third number: ");
        scanf("%*c%d",&num3);

	/*compares the three numbers to see if any values are the same
	 * IF at least two values are the same: outputs that value.
	 * ELSE outputs an ERROR message*/
	if (num1==num2 || num1==num3){
		printf("Value: %d\n",num1);
	}
	else if(num2==num3){
		printf("Value: %d\n", num2);
	}
	else{
		printf("ERROR\n");
	
	}
	return 0;
}
