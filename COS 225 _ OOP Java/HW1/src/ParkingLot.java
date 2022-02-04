import java.util.ArrayList;

public class ParkingLot {
	ParkingSpot spot;
	ParkingSpot type;
	int handicapped;
	int normal;
	
	public ParkingLot(){
		ArrayList<ParkingSpot> spots = new ArrayList<ParkingSpot>();
		
		for(int j = 0; j < 17; j++){
			spots.add(new ParkingSpot(false));
			this.normal = j;
			
		}
		for(int i = 0; i < 5; i++){
			spots.add(new ParkingSpot(true));
			this.handicapped = i;
		}
	}
	
}
