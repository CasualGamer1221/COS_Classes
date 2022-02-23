#include <stdio.h>

int main(){

	//Initialization of Fahrenheit and Celsius variables
	float F = 0;
	float C = 0;
	
	//Asks the user for a temperature in Fahrenheit
	printf("Enter a temperature in Fahrenheit: ");
	scanf("%f",&F);

	//Prints the given temperature in Celsius
	printf("Temperature in celsius = %0.3f\n", (F-32)/1.8);

	return 0;
}
