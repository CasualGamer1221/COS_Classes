

public class ParkingLot {
	ParkingSpot spot;
	ParkingSpot type;
	int handicapped;
	int normal;
	
	
	ParkingSpot[] spots = new ParkingSpot[20];
	
	public ParkingLot(){
		
		for(int j = 0; j < 20; j++){
			spots[j] = new ParkingSpot(j);
		
		}
	}

	
	public String toString() {
		handicapped = 0;
		normal = 0;
		for (int i = 0; i < 20; i++) {
			
			if (spots[i].car1 == null) {
				if (spots[i].handicap == true) {
					handicapped++;
				}
				else {
					normal++;
				}
			}
		}
		return handicapped + " " + normal + "\n";
	}
	
	public int park(Car car){
		for (int i = 0; i < 20; i++) {
			if (spots[i].car1 == null && spots[i].handicap == car.handicapAccessible) {
				spots[i].car1 = car;
				return i;
			}
			if (spots[i].car1 == null && spots[i].handicap == false && car.handicapAccessible == true) {
				spots[i].car1 = car;
				return i;
			}
		}
		return -1;
	}
	
	public Car leave(int index) {
		Car cartype = spots[index].car1;
		spots[index].car1 = null;
		return cartype;
	}
	
}
