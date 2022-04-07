
public class CustomerOrder {
	/*Declares variables*/
	String name, date;
	int quantity;
	
	/*Default constructor to make a null customer*/
	public CustomerOrder() {
		this.name =null;
		this.date = null;
		this.quantity = 0;
	}
	
	/*sets up a customer order*/
	public CustomerOrder(String name, String date, int quantity) {
		this.name = name;
		this.date = date;
		this.quantity = quantity;
	}
	
	/*ships this customer a product unless quantity would become negative*/
	public void shipProduct() {
		if(this.quantity >= 1) {
			this.quantity -= 1;
		}
		else {
			return;
		}
	}
	
}
