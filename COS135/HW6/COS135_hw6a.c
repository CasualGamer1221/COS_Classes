#include <stdio.h>
int main(){
	/*Jeffery Parent
	 * returns change to a customer using a prompted value*/
	
	/*Variable initialization*/
	int change_due = 0;
	int quarters = 0, dimes = 0, nickels = 0, pennies = 0;

	/*Prompts user for change due*/
	printf("Change due(only 0-99)");
	scanf("%d",&change_due);

	/*If change_due is >= 0 and <= 99, calculates change that is due
	 * else prints error statement*/
	if (0 <= change_due && change_due <= 99){
		if (change_due >= 25){
			quarters = change_due / 25;
			change_due = change_due % 25;
		}
		if (10 <= change_due < 25){
			dimes = change_due / 10;
			change_due = change_due % 10;
		}
		if (5 <= change_due < 10){
			nickels = change_due / 5;
			change_due = change_due % 5;
		}
		if (1 <= change_due < 5){
			pennies = change_due / 1;
			change_due = change_due % 1;
		}

		printf("Quarters: %d, Dimes: %d, Nickels: %d, Pennies: %d\n", quarters,dimes,nickels,pennies);
	}	
	
	else
		printf("Invalid Input!\n");

	return 0;
}
