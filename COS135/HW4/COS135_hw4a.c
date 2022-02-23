#include <stdio.h>

int main(){
	//Initializes variables to 0
	float width = 0;
	float height = 0;
	float area = 0;
	
	//Prompts the user to input a width and height as either a float or integer
	printf("Enter width:"); 
	scanf("%f" , &width);

	printf("Enter height");
	scanf("%f" , &height);
	
	//prints the area of a rectangle by multiplying the width and height
	printf("Area of the rectangle = %.3f\n", width*height);



}
