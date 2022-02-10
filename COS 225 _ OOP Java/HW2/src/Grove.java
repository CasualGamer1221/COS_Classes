
public class Grove {
	String groveName = "";
	Tree tree;
	int index;
	int treeAmount;
	Tree[] groveArray = new Tree[12];
	
	public Grove(String groveName) {
		this.groveName = groveName;
	}
	
	public int plantTree(Tree tree) {
		for (int i = 0; i < 12; i++) {
			if (groveArray[i] == null) {
				groveArray[i] = tree;
				return i;
			}
		}
		return -1;
	}
	
	public Tree removeTree(int index) {
		Tree tree = groveArray[index];
		groveArray[index] = null;
		return tree;
	}
	
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
