package jan28;

public class PersonalComputer {
	CPU processor;
	boolean powered = false;
	int RAM;
	Peripheral devices[];
	
	public PersonalComputer() {
		RAM = 16000;
		powered = false;
		processor = new CPU();
		devices = new Peripheral[100];
		devices[0] = new Peripheral();
		devices[0].name = "Mouse";
	}
	
	public PersonalComputer(int RAM) {
		powered = false;
		processor = new CPU();
		this.RAM = RAM;
		devices = new Peripheral[100];
	}
	
	public int RAMPerCore(){
		return RAM/processor.cores;
	}
}
