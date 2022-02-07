
public class ParkingTester {

	public static void main(String[] args) {
		//creates a new parkingLot and prints empty lot
		ParkingLot lot1 = new ParkingLot();
		System.out.print(lot1.toString());
		
		//creates a new car and parks it
		Car car1 = new Car("Lexus","RX","Blue",true);
		int car1_index = lot1.park(car1);
		System.out.print(lot1.toString());
		
		//creates a second car and parks it
		Car car2 = new Car("Ford","Explorer","",false);
		lot1.park(car2);
		System.out.println(lot1.toString());
		
		//un-parks the first car
		lot1.leave(car1_index);
		System.out.println(lot1.toString()); 
		
	}

}
