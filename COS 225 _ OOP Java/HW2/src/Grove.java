
public class Grove {
	String groveName = "";
	Tree tree;
	int index;
	int treeAmount;
	Tree[] groveArray = new Tree[12];
	
	//sets the Grove name
	public Grove(String groveName) {
		this.groveName = groveName;
	}
	
	//"Plants" trees in the array at the spots closest to the beginning
	public int plantTree(Tree tree) {
		for (int i = 0; i < 12; i++) {
			if (groveArray[i] == null) {
				groveArray[i] = tree;
				return i;
			}
		}
		return -1;
	}
	
	//removes trees from the array given an index
	public Tree removeTree(int index) {
		Tree tree = groveArray[index];
		groveArray[index] = null;
		return tree;
	}
	
	//returns a string with the number of trees in the array
	public String toString() {
		treeAmount = 12;
		for (int j = 0; j < 12; j++) {
			if (groveArray[j]== null) {
				treeAmount--;
			}
		}
		return treeAmount+"";		
	}
}
