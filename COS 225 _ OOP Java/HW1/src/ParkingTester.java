
public class ParkingTester {

	public static void main(String[] args) {
		ParkingLot lot1 = new ParkingLot();
		
		System.out.print(lot1.toString());
		
		Car car1 = new Car("Lexus","RX","Blue",true);
		lot1.park(car1.handicapAccessible);
		
		System.out.print(lot1.toString());
		
		Car car2 = new Car("Ford","Explorer","",false);
		lot1.park(car2.handicapAccessible);
		
		System.out.println(lot1.toString());
		
		lot1.leave(car1.handicapAccessible);
		
		System.out.println(lot1.toString()); 
	}

}
