
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
	
	public CustomerOrder(String name, String date, int quantity) {
		this.name = name;
		this.date = date;
		this.quantity = quantity;
	}
	
	public void shipProduct(String name, String date, int quantity) {
		if(quantity >= 1) {
			this.quantity = quantity - 1;
		}
		else {
			return;
		}
	}
	
}
