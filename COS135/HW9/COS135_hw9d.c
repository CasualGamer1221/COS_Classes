#include<stdio.h>
#include<stdlib.h>
#include <string.h>

/* JEFFERY PARENT
 * 
 * @brief  print all the elements in the stack
 * @note   passing the pointer to stack as a read-only by using const char *stack (same for size)
 * @param  *stack: Reference to the stack
 * @param  size: current length of the stack (size > 0)
 * @retval None
 */
void printstack(const char *stack, const int size) {
    
    if (size == 0) return; //nothing to print

    printf("current stack elements: ");
    for (int i = 0; i < size; i++) {
        printf("%c ", *(stack+i));
    }
    
    printf("\n");
    
}

/**
 * @brief  shift all the stack elements to right before push a new element
 * @note
 * @param  *stack: Reference to the stack
 * @param  size: current length of the stack (size > 0)
 * @retval None
 */
void shiftright(char *stack, int size) {
    
    for (int i = (size-1); i > 0; i--) {
        *(stack + i) = *(stack + i - 1);
    }
    
}

/**
 * @brief  shift all the stack elements to left after pop
 * @note
 * @param  *stack: Reference to the stack
 * @param  size: current length of the stack (size > 0)
 * @retval None
 */
void shiftleft(char *stack, int size) {
    
    for (int i = 0; i < size; i++) {
        *(stack + i) = *(stack + i + 1);
    }
    
}

/**
 * @brief  pop the top element from the stack (from beginning)
 * @note   if the stack is empty, returns a '_'
 * @param  **stack: Reference to the stack (double pointer)
 * @param  *size: pointer to the size variable defined in main() function
 * @retval character popped from the stack (first element)
 */
char pop(char **stack, int *size) {
    
    if (*size == 0) {
        printf("Error: The stack is empty.\n");
        return '_';
    }
    //if it is the last element, pop it and free the memory
    else if (*size == 1) {
        char ch = **stack;
        free(*stack);
        *stack = NULL;
        --*size; // reduce size by 1
        return ch;
        
    }
    //pop the first element, shift all to the left, remove one element
    else if (*size > 1) {
        char ch = **stack;
        shiftleft(*stack, *size);
        --*size; // reduce size by 1
        *stack = realloc(*stack, *size);
        return ch;
    }
    
    // this return will reach if only there is an unexpected error
    // you may handle this in the main function
    return 0; // return NULL
    
}

/**
 * @brief  insert/push a new element to the top of the stack (from beginning)
 * @note   if the stack is empty, create a new memory; else add more memory
 * @param  **stack: Reference to the stack (double pointer)
 * @param  *size: pointer to the size variable defined in main() function
 * @retval None
 */
void push(char new_value, char **stack, int *size) {
    
    if (*size == 0) {
        ++*size; // increment size by 1
        *stack = (char *) malloc(*size); // allocate new memory
        **stack = new_value;
    }
    // increase the size of memory, shift everything to the right,
    // assign the new value to the first element
    else if (*size >= 1) {
        ++*size; // increment size by 1
        *stack = realloc(*stack, *size);
        shiftright(*stack, *size);
        
        **stack = new_value;
    }
    
    //printf("pushed: %c\n", new_value);
    
    return;
}

/**
 * Main function that takes user inputted string and prints it in reverse
 * MAX stack size is 10
 */

int main() {
    
    int size = 0; // maintain the size of the stack
    
    // create a reference to the char stack (no memory is allocated yet)
    // dynamic memory will be allocated in the push() function when required
    char* stack;
    
    char phrase[200]; // user inputted phrase 
    printf("Enter a phrase [200 char max]: ");
    scanf("%s",phrase);
    
    for (int i = 0; i < strlen(phrase); i++){
	push(phrase[i],&stack,&size);
    }

    while (size > 0){
	printf("%c",pop(&stack,&size));
    }
    printf("\n");


    

    return 0;
}

