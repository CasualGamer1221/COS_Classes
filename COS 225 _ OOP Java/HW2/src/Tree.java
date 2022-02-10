
public class Tree {
	int idNumber;
	int age;
	String speciesName;
	
	//default tree
	public Tree(int idNumber) {
		this.idNumber = idNumber;
	}
		
	public Tree(int id, int age, String speciesName) {
		this.idNumber = id;
		this.age = age;
		this.speciesName = speciesName;
	}
	
}
