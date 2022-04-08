
public class OrderQueue {
	LinkedQueue<CustomerOrder> orders = new LinkedQueue<CustomerOrder>();
	
	/*Variables for queue size and stock amount*/
	int stock = 0;
	int queuesize = 0;
	
	/*sets up an empty queue with no stock*/
	public OrderQueue() {
		this.stock = 0;
		this.queuesize = 0;
	}
	
	/*Sets up an order queue with a stock passed as a parameter*/
	public OrderQueue(int stock) {
		this.stock = stock;
	}
	
	/*Implements a method to add a new order to the queue*/
	public void newOrder(CustomerOrder order) {
		orders.enqueue(order);
		queuesize += 1;
	}
	
	/*Implements a method to add additional stock*/
	public void addStock(int stockb) {
		this.stock += stockb;
	}
	
	/*Implements a method that will take the customer at the front of the queue, and fulfill one of their orders
	 * removes customer from queue if quantity == 0 */
	public void completeOrder() {
		orders.getFront().shipProduct();
		this.stock -= 1;
		
		if(orders.getFront().quantity == 0) {
			orders.dequeue();
			queuesize -= 1;
		}
	}
	
	/*Implements a method that will sell the remaining stock to each customer at the front of the queue until the stock is 0*/
	public void sellout() {
		while(stock > 0) {
			completeOrder();
		}
	}
	
	/*Returns a string with the quantity of the first order in the queue*/
	public String toString() {
		return orders.getFront().quantity + " ";
	}	
	
	
}
