
public class ParkingTester {

	public static void main(String[] args) {
		ParkingLot lot1 = new ParkingLot();
		
		System.out.print(lot1.toString());
		
		Car car1 = new Car("Lexus","RX","Blue",true);
		int car1_index = lot1.park(car1);
		
		System.out.print(lot1.toString());
		
		Car car2 = new Car("Ford","Explorer","",false);
		lot1.park(car2);
		
		System.out.println(lot1.toString());
		
		lot1.leave(car1_index);
		
		System.out.println(lot1.toString()); 
	}

}
