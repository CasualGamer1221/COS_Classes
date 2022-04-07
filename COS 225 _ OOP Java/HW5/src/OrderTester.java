
public class OrderTester {

	public static void main(String[] args) {
		/*Instantiates an OrderQueue with a stock of 12*/
		OrderQueue orders = new OrderQueue(12);
		
		/*adds three customers to the queue with order quantities of 3, 5, and 8*/
		orders.newOrder(new CustomerOrder(null, null,3));
		orders.newOrder(new CustomerOrder(null, null,5));
		orders.newOrder(new CustomerOrder(null, null,8));
		
		/*Prints the order Queue*/
		System.out.println(orders);
		
		/*clears the stock by fulfilling as many orders as possible*/
		orders.sellout();
		
		/*Prints the order queue*/
		System.out.println(orders);
		
		/*adds 8 units to the stock*/
		orders.addStock(8);
		
		/*adds 3 new customer orders w/ quantities of 2, 2, and 5*/
		orders.newOrder(new CustomerOrder(null, null,2));
		orders.newOrder(new CustomerOrder(null, null,2));
		orders.newOrder(new CustomerOrder(null, null,5));
		
		/*clears the stock by fulfilling as many orders as possible*/
		orders.sellout();
		
		/*Prints the order queue*/
		System.out.println(orders);
		
		
		
	}

}
