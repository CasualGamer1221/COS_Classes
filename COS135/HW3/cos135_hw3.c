#include <stdio.h>
int main(){
	char storename[12] = "The Z Store";
	float item1_price = 21.45;
	float item2_price = 10.00;
	float item3_price = 14.90;
	float item4_price = 33.50;
	
	int quantity = 2;
	float item_total = quantity*(item1_price+item2_price+item3_price+item4_price);
	float gst = item_total*0.1;
	float total = gst + item_total;

	
	printf("\n\nWelcome to %s\n\n", storename);
	printf("Item 1\t $%0.2f\t  x2\t $%0.2f\n", item1_price,item1_price*2);
	printf("Item 2\t $%0.2f\t  x2\t $%0.2f\n", item2_price,item2_price*2);
	printf("Item 3\t $%0.2f\t  x2\t $%0.2f\n", item3_price,item3_price*2);
	printf("Item 4\t $%0.2f\t  x2\t $%0.2f\n\n", item4_price,item4_price*2);
	printf("Item Total:   $%0.2f\n\n",item_total);
	printf("GST:     $%0.2f\n",gst);
	printf("Total:   $%0.2f\n", total);
	
	return 0;


}
