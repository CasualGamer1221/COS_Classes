
public class Car {
	String make;
	String model;
	String color;
	Boolean handicapAccessible;
	
	public Car(String make, String model, String color, boolean HandicapAccessible){
		this.make = make;
		this.model = model;
		this.color=color;
		this.handicapAccessible = HandicapAccessible;
	}
	
	
	///set and get
	public String setCarMake(String make) {
		this.make = make;
		return make;
	}
	
	public String getCarMake(){
		return make;
	}
	
	public String setCarModel(String model){
		this.model = model;
		return model;
	}
	  
	public String getCarModel(){
		return model;
	}
	
	public String setCarColor(String color){
		this.color = color;
		return color;
	}
	
	public String getCarColor(){
		return color;
	}
	
	public boolean setisHandicapAccessible(){
		this.handicapAccessible = true;
		return true;
	}
	
	public boolean getisHandicapAccessible(){
		return handicapAccessible;
	}
	
	public String toString() {
		return "Car: " + make + " " + model + " " + color + " " + handicapAccessible;
	}
	

	
}
