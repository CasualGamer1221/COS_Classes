
public class GroveTester {

	public static void main(String[] args) {
		//Instantiates a grove object named Grove One
		Grove grove1 = new Grove("Grove One");
		System.out.println(grove1);
		
		//Adds trees of species:Fir , and age: 20, to the grove
		for (int i=0; i<7; i++) {
			Tree tree1 = new Tree(i,20,"Fir");
			grove1.plantTree(tree1);
		}
		System.out.println(grove1);
		
		//Removes trees at indexes 3 and 5 from Grove One
		grove1.removeTree(3);
		grove1.removeTree(5);
		
		System.out.println(grove1);
		
		Tree tree1 = new Tree(0,10, "Pine");
		grove1.plantTree(tree1);
		
		System.out.println(grove1);
		
	}

}
