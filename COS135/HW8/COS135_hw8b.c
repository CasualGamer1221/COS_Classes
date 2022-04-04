#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* Jeffery Parent
 * Checks if a password is:
 * 1. at least 8 characters long
 * 2. at least 1 upper and 1 lower case letter
 * 3. at least 1 digit/number
 * 4. at least 1 of: !,@,#,$*/

/* Checks if password is at least 8 characters long*/
int pass_length(char pass[]){
	if (strlen(pass)>7){
		return 1;
	}
	else{
		return 0;
	}
}

/* Check if password has at least 1 upper and 1 lowercase character */
int low_up(char pass[]){
	/*Variables to keep track of upper & lowercase letters*/
        int lower_case_count = 0;
        int upper_case_count = 0;
	int p = strlen(pass);

	/* Counts number of upper & lowercase values in password
	 * returns 1 if at least 1 of each
	 * else returns 0*/
     	for (int i = 0; i < p; i++) {
        	if (pass[i] >= 'a' && pass[i] <= 'z') ++lower_case_count;
        	if (pass[i] >= 'A' && pass[i] <= 'Z') ++upper_case_count;
	}
	
	if(lower_case_count > 0 && upper_case_count > 0){
		return 1;
	}
	else{
		return 0;
	}
}


/* Checks if password has at least 1 number*/
int num(char pass[]){
	/* Variables to keep track of numbers in password & password length*/
	int number_count = 0;
	int p = strlen(pass);

	/* Returns 1 if password has at least 1 digit*/
	for (int i = 0; i < p; i++) {
                if (isdigit(pass[i])){
			++number_count;
        	}
	}
	if(number_count > 0){
		return 1;
	}
	else{
		return 0;
	}
}

/* Checks if password has at least 1 from the following: !,@,#,$*/
int special(char pass[]){
	/* Variables to keep track of specials in password and password length*/
	int special_count = 0;
	int p = strlen(pass);
	
	for (int i = 0; i < p; i++) {
		if(pass[i] == 33 || pass[i] == 64 || pass[i] == 35 || pass[i] == 36){
			++special_count;
		}
        }
	if(special_count > 0){
		return 1;
	}
	else{
		return 0;
	}
}

/* ENCRYPTION FOR VALID PASSWORD*/
void encrypt(char pass[]){
	int p = strlen(pass); //password length
	
	/* Checks each character of password bases on ASCII; 
	 * adds 1 if alphanumeric & subtracts 1 if one of the 4 special characters*/
	for (int i = 0; i < p; i++){
		if(isalnum(pass[i])){
			pass[i] = pass[i] + 1;
		}
		if(pass[i] == 33 || pass[i] == 64 || pass[i] == 35 || pass[i] == 36){
			pass[i] = pass[i] - 1;
		}	
	}
}

int main(){
	/* Variable initialization for inputted password*/
	char pass[100];
	printf("Please enter your preffered password: ");
	scanf("%s",pass);
	
	/* Initialize variables to keep track of password validity by using function outputs*/
	int length_out = pass_length(pass);
	int low_up_out = low_up(pass);
	int num_out = num(pass);
	int special_out = special(pass);

	/* If any part of the password is invalid, print that its invalid and states all the reasons why
	 * else says password is valid*/
	if(length_out == 0 || low_up_out == 0 || num_out == 0 || special_out == 0){
		printf("Invalid password\n");
		if(length_out == 0){
			printf("Reason #1: your password should contain at least 8 characters\n");
		}
		if(low_up_out == 0){
			printf("Reason #2: your password should contain at least one uppercase and one lowercase character\n");
		}
		if(num_out == 0){
			printf("Reason #3: your password should contain at least one digit/number\n");
		}
		if(special_out == 0){
			printf("Reason #4: your password should contain at least one of the four special characters: \"! @ # $\"\n");
		}
	}
	else{
		printf("Valid Password\n");
		
		encrypt(pass); //Calls Encryption function
		printf("\n\n If password is encrypted: %s\n", pass);
	}
}
