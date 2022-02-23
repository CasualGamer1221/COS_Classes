#include <stdio.h> 

int main(){
	
	// Initializes variables w/ name being a max of 50 characters long
	char name[50];
	char sc1=0,  sc2=0,  sc3=0, sc4=0;
	float g1 = 0, g2 = 0, g3 = 0, g4 = 0;
	float total = 0, average = 0;
	
	//asks for the student's name
	printf("Enter the student's name (MAX 50 CHARACTERS): ");
	fgets(name,50,stdin);

	//asks for subject and grade 1
	printf("Enter subject code 1 and grade (e.g. m 98): ");
	scanf("%c%f",&sc1,&g1);

	//asks for subject and grade 2, while removing newline character that was left in stream
	printf("Enter subject code 2 and grade (e.g. m 98): ");
	scanf("%*c%c%f",&sc2,&g2);

	//asks for subject and grade 3, while removing newline character that was left in stream
	printf("Enter subject code 3 and grade (e.g. m 98): ");
	scanf("%*c%c%f",&sc3,&g3);

	//asks for subject and grade 4, while removing newline character that was left in stream
	printf("Enter subject code 4 and grade (e.g. m 98): ");
	scanf("%*c%c%f",&sc4,&g4);
	
 
	//finds the total and average of the inputted grades
	total = g1+g2+g3+g4;
	average = total/4;

	//prints the student's name, total grades, and average grades
	printf("Final grades for %s: ", name);
	printf("Total for %c%c%c%c: %0.2f\n",sc1,sc2,sc3,sc4 , total );
	printf("Average grades: %0.2f\n\n", average);
	
	return 0;


}
