import java.util.ArrayList;

public class ParkingLot {
	ParkingSpot spot;
	ParkingSpot type;
	
	
	public ParkingLot(){
		ArrayList<ParkingSpot> spots = new ArrayList<ParkingSpot>();
		
		for(int i = 16; i > 0; i--){
			spots.add(new ParkingSpot(false));
		}
		for(int i = 4; i > 0; i--){
			spots.add(new ParkingSpot(true));
		}
	}
	
}
