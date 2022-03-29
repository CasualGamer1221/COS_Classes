#include <stdio.h>
#include <string.h>

/* Jeffery Parent
 * Ranks a student's grades and calculates their average*/

/*Changes what address each pointer goes to*/
void swap(int *x, int *y){
        int temp;
        temp = *x;
        *x = *y;
        *y = temp;
        return;
}

/*Ranks student's grades by changing the variable's pointers*/
void rankStudentGrades(int *grade1, int *grade2, int *grade3){
	if(*grade1 > *grade2){
		swap(&*grade1,&*grade2);
	}
	if(*grade2 > *grade3){
		swap(&*grade2,&*grade3);
	}
}

/*Calculates and returns average of grades*/
double average(int grade1, int grade2, int grade3){
	double average = (grade1 + grade2 + grade3) / 3;
	return average;
}

int main(){
	/*Initializes variables*/
	char name[40];
	int g1=0,g2=0,g3=0;
	double avg=0;
	
	/*Gets student's name*/
	printf("Enter student's name: ");
	fgets(name, 40, stdin);
	name[strcspn(name, "\n")] = 0;

	/*Gets student's 3 grades*/
	printf("Enter student's first grade: ");
	scanf("%d",&g1);

	printf("Enter student's second grade: ");
	scanf("%*c%d",&g2);
	
	printf("Enter student's third grade: ");
	scanf("%*c%d",&g3);
	

	/*Calls average and ranking functions*/
	
	rankStudentGrades(&g1,&g2,&g3);
	avg = average(g1,g2,g3);


	printf("%s\t%d\t%d\t%d\t%.2f\n",name,g1,g2,g3,avg);

	return 0;
}
