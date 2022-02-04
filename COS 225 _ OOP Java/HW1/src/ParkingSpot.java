
public class ParkingSpot {
	
	Car car1;
	Car car2;
	
	public ParkingSpot(boolean Handicap) {
		 	Car car1 = new Car("Lexus","RX","Blue",Handicap);
		 	Car car2 = new Car("Ford","Explorer",null,Handicap);
		 	
		 	this.car1 = car1;
		 	this.car2 = car2;
	}
	
}
