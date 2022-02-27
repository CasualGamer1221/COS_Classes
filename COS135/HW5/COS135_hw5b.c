#include <stdio.h>
#include <string.h>

/* JEFFERY PARENT
 * Collects and applicant's information, then outputs a summary*/
int main(){
	/*Initializes variables*/
	char name[50];
	int birthyear = 0, currentyear=2022;
	float salary = 0.0;
	
	/*Asks for applicants name and removes trailing \n character*/
	printf("Enter applicant's name(MAX 50 Characters): ");
	fgets(name,50,stdin);
	name[strcspn(name, "\n")] = 0;
	
	/*Asks for applicants birthyear*/
	printf("Enter applicant's birth year: ");
	scanf("%d",&birthyear);
	
	/*Asks for applicants preffered monthly salary*/
	printf("Enter preferred monthly salary(USD): ");
	scanf("%*c%f", &salary);
	
	/*Prints the aformentioned data in a summary statement*/
	printf("\n%s is a %d years old applicant and requests a monthly salary of $%.2f\n",name, currentyear-birthyear, salary);

	return 0;
}
