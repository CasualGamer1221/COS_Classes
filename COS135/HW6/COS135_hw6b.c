#include <stdio.h>
#include <ctype.h>

/* Jeffery Parent
 * Prompts user for a character and checks whether it's part of the alphabet
 * program exits when '#' is entered*/
int main(){
	/*Declares variable for inputted character*/
	char c;
	
	printf("Enter a letter: ");
	scanf("%c", &c);

	while (isalpha(c)){
		// evaluates to 1 and runs if variable c is a vowel
    		if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'){
			printf("%c is a vowel\n",c);
		}

		else{
			printf("%c is a consonant\n",c);
		}
		
		/*Repeatedly asks user for a letter*/
		printf("Enter a letter: ");
		scanf("%*c%c", &c);
	}

	/*Exit program character*/
	if (c == '#'){
		printf("BYE!\n");
	}

	/*If character not in English alphabet*/
	else{
	       printf("%c is not a letter in the English alphabet\n",c);	
	}

	return 0;
}

