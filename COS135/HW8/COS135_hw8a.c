#include<stdio.h>
#include<stdlib.h>
#include <time.h>

/*Jeffery Parent
 * outputs the max and min of a random array of 200 numbers*/


/*
return the index of the lowest number in the array
e.g., if the lowest number is in 3rd position, returns 2
if not return -1
*/
int find_lowest(int numbers[]) {
	// Initialize minimum element and index
	int min = numbers[0];
	int min_index = 0;
	int i;
	if (sizeof(numbers[0]) > 0){
		// Traverse array elements from second and
		// compare every element with current min 
		for (i = 1; i < 200; i++)
			if (numbers[i] < min){
				min = numbers[i];
				min_index = i;
			}
		return min_index;
	}
	else
		return -1;
}

/*
return the highest number in the array
e.g., if the highest number is in 1st position, returns 0
if not return -1
*/
int find_highest(int numbers[]) {
	
	// Initialize maximum element and index
	int max = numbers[0];
	int max_index = 0;
	int i;
 
	if (sizeof(numbers[0]) > 0){
		// Traverse array elements from second and
		// compare every element with current max 
		for (i = 1; i < 200; i++)
			if (numbers[i] > max){
				max = numbers[i];
				max_index = i;
			}
		return max_index;
	}
	else
		return -1;
}
int main() {
	// seed rng
	srand(time(NULL));
	
	//creates empty array
	int numbers [200];
	
	//sets 200 random numbers in array
	for (int i = 0; i < 200; i++) {
		numbers[i] = (rand() % (999));
	}	
	int highest_index = find_highest(numbers);
	int lowest_index = find_lowest(numbers);
	
	//prints largest and smallest values in array
	printf("\n\nLowest number %d is at index %d\n", numbers[highest_index], highest_index);
	printf("Highest number %d is at index %d\n", numbers[lowest_index], lowest_index);

}
