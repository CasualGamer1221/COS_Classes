
public class PatientTester {

	public static void main(String[] args) {
		/*Instantiates a new PatientsManager & calls its toString method*/
		PatientManager patientManager = new PatientManager();
		System.out.println(patientManager);
		
		/*Adds 4 patients to the array with pre-specified values & prints the result*/
		for (int i=1; i<5; i++) {
			Patient patient = new Patient(i,i*100);
			patientManager.addPatient(patient);
		}
		System.out.println(patientManager);
		
		/*Calls the caffeineAbsorbtion method of this instance of patientManager & prints the result*/
		patientManager.caffeineAbsorbtion();
		System.out.println(patientManager);
		
		/*Finds the patient in the array with the maximum value of caffeine & removes them from the array
		 * result is then printed*/
		int maxcaffid = 0;
		for (int i=0;i<6;i++) {
			if (patientManager.patients[i] != null && patientManager.patients[i].caffeine_level > maxcaffid) {
				maxcaffid = i;
			}
			else {continue; 
			}
		}
		patientManager.removePatient(maxcaffid);
		System.out.println(patientManager);
	}
}
