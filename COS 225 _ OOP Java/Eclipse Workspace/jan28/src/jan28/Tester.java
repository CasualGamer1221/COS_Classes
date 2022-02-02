package jan28;

import java.util.ArrayList;

public class Tester {

	public static void main(String[] args) {
		
		PersonalComputer computerOne = new PersonalComputer();
		
		System.out.println(computerOne.processor.clockRate);
		System.out.println(computerOne.RAMPerCore());
		//System.out.println(computerOne.devices[0]);
		
		for (int i = 0; i < 10; i++) {
			System.out.println(computerOne.devices[i].name);
		}
		
		ArrayList<PersonalComputer> computers = new ArrayList<PersonalComputer>();
		
		for (int i = 0; i < 10; i++) {
			computers.add(new PersonalComputer());
		}
		
		for (int i = 0; i < 10; i++) {
			System.out.println(computers.get(i).devices[0].name);
	}

}
}
