
public class Book {
	/*Declares variables*/
	String title, genre;

	/*Parameterized constructor that sets title & genre*/
	public Book(String title, String genre) {
		this.title = title;
		this.genre = genre;
	}
	
	/*toString method that returns the books title*/
	public String toString() {
		return title;
	}
}
