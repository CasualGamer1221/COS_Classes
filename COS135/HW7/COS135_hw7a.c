#include <stdio.h>
/* Jeffery Parent
 * Prints ASCII characters with their values from 33->127*/
int main(){
	/* Initializes variables*/
	int i = 33;
	
	for (;i<=127;i++){
		printf("%c = %d\n",i,i);
	}
	return 0;
}
