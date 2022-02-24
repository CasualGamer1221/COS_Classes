
public class PatientManager {
	/*Creates empty array of Patient*/
	Patient[] patients = new Patient[6];
	
	
	/*DEFAULT
	 * Sets each value in array to be null*/
	public PatientManager() {
		for (int i = 0; i < 6; i++) {
			patients[i] = null;
		}
	}
	
	
	/*Adds patient to array given Patient object
	 * Returns -1 if error occurs*/
	public int addPatient(Patient patient) {
		for (int i = 0; i < 6; i++) {
			if (patients[i] == null) {
				patients[i] = patient;
				return i;
			}
		}
		return -1;
	}
	
	
	/*Removes patient from array if given patient id*/
	public Patient removePatient(int index) {
		Patient patient = patients[index];
		patients[index] = null;
		return patient;
	}
	
	
	/*When called will simulate absorption of caffeine and will remove 130 caffeine from each patient in the array
	 * if caffeine level of any patient is 0 or less after, they will be removed from the array */
	public void caffeineAbsorbtion() {
		for (int i = 0; i < 6; i++) {
			if (patients[i] != null && patients[i].caffeine_level > 130) {
				patients[i].caffeine_level -= 130;
			}
			else if (patients[i] != null && patients[i].caffeine_level < 130) {
				patients[i] = null;
			}
			else if (patients[i] == null) {
				continue;
			}
		}
	}
	
	
	/*Returns a string representation of the array
	 * returns EMPTY if there are no patients in the array*/
	public String toString() {
		String patientsReturn = "";
		int total = 6;
		for (int i = 0; i < 6; i++) {
			if (patients[i] != null) {
				patientsReturn += (patients[i].id+" "+patients[i].caffeine_level+"\n");
				total--;
			}
			else if(total == 0) {
				patientsReturn = "EMPTY\n";
			}
		}
		return patientsReturn;
	}
}
