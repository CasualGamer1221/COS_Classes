#include <stdio.h>

/* JEFFERY PARENT
 * Asks for the amount of chcocolates and toffees purchased
 * more than 5 chocolates = 10% discount
 * more than 2 toffees = 5% discount
 * total more than $100 = additional 10% discount*/
int main(){
	/*Intitializes variables*/
	char storename[50]; 				//name of store
	int chocamt = 0, toffamt = 0; 			//amount of each candy purchased
	float total_choc = 0, total_toff = 0; 		//total price of each candy purchased
	float total_bd = 0, total_ad = 0; 		//totals before and after final discount
	float discount = 1.00;				//discount multiplier
	float choccost = 15.50, toffcost = 6.90;	//base cost of candies
	
	/*Asks for store name*/
	printf("Enter store name: ");
	fgets(storename,50,stdin);

	/*Gets number of chocolate bags purchased*/
	printf("Enter number of chocolate bags: ");
	scanf("%d", &chocamt);

	/*Gets number of toffee bags purchased*/
	printf("Enter number of toffee bags: ");
	scanf("%*c%d",&toffamt);

	/*calculates any discounts and prints everything in an itemized reciept */
	printf("\tWelcome to %s", storename);
	
	
	/************************* RECIEPT *********************************/
	/*Prints Chocolate amount and total price*/
	printf("Chocolates \tx%d      $ %0.2f\n",chocamt,chocamt*choccost);
	
	/*If qty is greater than 5 then applies a 10% discount to the chocolate price*/
	if(chocamt>5){
		discount -= .10;
		printf("\tafter discount   $ %0.2f\n",chocamt*discount*choccost);
		total_choc = chocamt*discount*choccost;
		discount = 1.00;
	}
	else{
		total_choc = chocamt*choccost; 
	}
	


	/*Prints toffee amount and total price*/
	printf("\nToffees \tx%d      $ %0.2f\n",toffamt,toffamt*toffcost);
	
	/*If qty is greater than 2 then applies a 5% discount to the toffee price*/
        if(toffamt>5){
                discount -= .05;
                printf("\tafter discount   $ %0.2f\n",toffamt*discount*toffcost);
                total_toff = toffamt*discount*toffcost;
		discount = 1.00;
        }
        else{
                total_toff = toffamt*toffcost; 
        }
	


	/*Prints the total price of everything before the bulk discount*/
	total_bd=total_choc+total_toff;
	printf("\nTotal after discount     $ %0.2f\n", total_bd);

	/*If price is greater than $100 applies a 10% bulk discount and prints result*/
	if (total_bd>100){
		discount -= .10;
		total_ad = total_bd*discount;
		printf(" after 10%% discount      $ %0.2f\n",total_ad );
		printf("\n\t    You owe      $ %0.2f\n\t   Thank you!\n\n", total_ad);

	}
	else{

		printf("\n\t    You owe      $ %0.2f\n\t   Thank you!\n\n", total_bd);
	}
		
	return 0;
}
