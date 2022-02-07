
public class ParkingSpot {
	
	Car car1;
	boolean handicap;
	int index;
	
	
	public ParkingSpot(int index) {
		if (index < 4) {
			handicap = true;
		}
		else {
			handicap = false;
		}
		this.index = index;
	}
	
	public ParkingSpot(Car car1, int index) {
		if (index < 4) {
			handicap = true;
		}
		else {
			handicap = false;
		}
		
		this.index = index;
		this.car1 = car1;
	}
}
