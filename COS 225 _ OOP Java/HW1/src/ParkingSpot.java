
public class ParkingSpot {
	Car type;
	boolean Handicap = false;
	
	public ParkingSpot(boolean Handicap) {
		this.Handicap = Handicap;
		
		//????????????????
		this.type = new Car(null, null, null, Handicap);
	}
	
}
