#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define display_width 2 // fieldwidth - set the distance between numbers

/**
 * Jeffery Parent
 * using part of the given example program, prints 2 matrices of a user inputted size and multiplies them if the sizes are valid */

/**
 * @brief  clear all the memory allocated dynamically
 * @note
 * @param  xr: The number of matrix x rows (xr > 0)
 * @param  ***x: Reference of the Matrix to be freed
 * @param  yr: The number of matrix y rows (yr > 0)
 * @param  ***y: Reference of the Matrix to be freed
 * @param  ***z: Reference of the Matrix to be freed
 * @retval None
 */
void freememory(int xr, int ***x, int yr, int ***y, int ***z)
{
    // free the dynamically allocated memory
    // you need to clear all the dimentions
    for (int i = 0; i < xr; i++) {
        free((*x)[i]);
        (*x)[i] = NULL;
    }
    for (int i = 0; i < yr; i++) {
        free((*y)[i]);
        (*y)[i] = NULL;
    }
    for (int i = 0; i < xr; i++) {
        free((*z)[i]);
        (*z)[i] = NULL;
    }
    
    free(*x);
    free(*y);
    free(*z);
    
    *x = *y = *z = NULL;
}

/**
 * @brief  Print row r of the matrix m with data column width w.
 * @note   
 * @param  mr: The number of rows in the matrix (mr > 0)
 * @param  mc: The number of columns in the matrix  (mc > 0)
 * @param  **m: Matrix with dimensions mr by mc
 * @param  r: The row to display (r >= 0)
 * @param  w: Data display width / fieldwidth (w > 0)
 * @retval None
 */
void printrow(int mr, int mc, int **m, int r, int w)
{

    if (r < mr) // We have data for this row
    {

        for (int c = 0; c < mc; c++)
        {
            printf("%-*d ", w, m[r][c]);
        }
    }
    else // Array doesn't have enough rows, just pad with white space
    {
        for (int c = 0; c < mc; c++)
        {
            printf("%*c ", w, ' ');
        }
    }
}

/**
 * @brief  Display matrix x multiplied by matrix y and the resulting matrix z.
 * @note   This function displays the matrices in the format specified in assignment 9.
 * @param  xr: The number of matrix x rows (xr > 0)
 * @param  xc: The number of matrix x columns (xc > 0)
 * @param  **x: Matrix with dimensions xr by xc
 * @param  yr: The number of matrix y rows (yr > 0)
 * @param  yc: The number of matrix y columns (yc > 0)
 * @param  **y: Matrix with dimensions yr by yc
 * @param  zr: The number of matrix z rows (zr > 0)
 * @param  zc: The number of matrix z columns (zc > 0)
 * @param  **z: Matrix with dimensions zr by zc
 * @retval None
 */
void matrixprint(int xr, int xc, int **x, int yr, int yc, int **y, int zr, int zc, int **z)
{

    // Print all three matrices at the same time line by line.
    // White space padding for smaller matrices.
    for (int r = 0; r < xr || r < yr; r++)
    {

        printrow(xr, xc, x, r, display_width);

        if (r == 0) // Print dot on first row of first matrix
        {
            printf(".%*c", display_width, ' ');
        }
        else
        {
            printf(" %*c", display_width, ' ');
        }

        printrow(yr, yc, y, r, display_width);

        if (r == 0)
        {
            printf("=%*c", display_width, ' ');
        }
        else
        {
            printf(" %*c", display_width, ' ');
        }

        printrow(zr, zc, z, r, display_width);

        printf("\n");
    }
}

/**
 * @brief  Fill matrix x with random numbers between 1 and 9.
 * @note   
 * @param  xr: The number of matrix rows (xr > 0)
 * @param  xc: The number of matrix columns (xc > 0)
 * @param  **x: Matrix
 * @retval None
 */
void fillmatrix(int xr, int xc, int **x)
{
    for (int i = 0; i < xr; i++)
    {
        for (int j = 0; j < xc; j++)
        {
            x[i][j] = 1 + rand() % 9; // I'll let you guys figure this out
        }
    }
}

/**
 * @brief  gets matrix dimensions from user and validates them
 * @retval None
 */
void matrixdim(int *xr, int *xc, int *yr, int *yc){
	//Temp variables for dimensions
	int txr = 0, txc = 0, tyr = 1, tyc = 0;

	//loop will continue until matrix 1 columns match matrix 2 rows
	//eg. matrices can be "legally" multiplied
	
	while(txc != tyr){
		printf("Enter matrix 1 rows: ");
		scanf("%d",&txr);
		*xr = txr;

		printf("Enter matrix 1 columns: ");
		scanf("%d",&txc);
		*xc = txc;

		printf("Enter matrix 2 rows: ");
		scanf("%d",&tyr);
		*yr = tyr;

		printf("Enter matrix 2 columns: ");
		scanf("%d", &tyc);
		*yc = tyc;

		if(txc != tyr || txc == 0 || tyr == 0){
			printf("Matrix 1 columns and Matrix 2 Rows Don't match\tor are 0\nplease re-enter dimensions: \n");
		}
	}
	
	
}

/**
 *  @brief multiplies matrix x and y to form matrix z
 */
void multiplymatrix(int xr, int xc, int **x, int yr, int yc, int **y, int zr, int zc, int **z){
	for (int i = 0; i < xr; ++i){
		for (int j = 0; j < yc; ++j){
			z[i][j] = 0;
			for (int k = 0; k < xc; ++k){
				z[i][j] += x[i][k] * y[k][j];
				
			}
		}
	}
}

/**
 * @brief  COS135 assignment 9 matrix print example //edited by Jeffery Parent
 * @note   This example uses dynamic 2D arrays
 * @retval 0 if the program terminates without errors
 */
int main()
{

    // initialize dimension variables
    int xr = 0, xc = 0, yr = 0, yc = 0;
    
    //seeds rand
    srand ( time(NULL) );
	
    // Calls funtion to get matrix dimensions
    matrixdim(&xr, &xc, &yr, &yc);

    // pointer to a pointer - 2D array
    // dynamically allocate rows
    int** x = (int**)malloc(xr * sizeof(int*));
    int** y = (int**)malloc(yr * sizeof(int*));
    int** z = (int**)malloc(xr * sizeof(int*));

    // dynamically allocate columns for each matrix
    for (int i = 0; i < xr; i++)
        x[i] = (int*)malloc(xc * sizeof(int));
    for (int i = 0; i < yr; i++)
        y[i] = (int*)malloc(yc * sizeof(int));
    for (int i = 0; i < xr; i++)
        z[i] = (int*)malloc(yc * sizeof(int));
    
    fillmatrix(xr, xc, x); // Will be random numbers
    fillmatrix(yr, yc, y); // Will be random numbers
    fillmatrix(xr, yc, z); // Just to initialize - will be replaced
	
    multiplymatrix(xr, xc, x, yr, yc, y, xr, yc, z); // will multiply the 2 matrices together

    matrixprint(xr, xc, x, yr, yc, y, xr, yc, z); // will print 2 beginning matrices and matrix product of the two
    
    //deallocate memory from all the matrices
    freememory(xr, &x, yr, &y, &z);
    
    return 0;

}
