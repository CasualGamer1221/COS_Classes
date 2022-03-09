import java.util.ArrayList;

public class BookShelf {
	char bookshelf_letter;
	ArrayList <Book> books = new ArrayList <> (8);
	
	
	/*Default constructor , setting each value in ArrayList to null*/
	private BookShelf() {
		for (int i=0;i<6;i++) {
			books.set(i, null);
		}
	}
	
	
	/*getters and setters*/
	public char get_bookshelfLetter() {
		return bookshelf_letter;
	}
	public void set_bookshelf_letter(char letter) {
		this.bookshelf_letter = letter;
	}
	
	public ArrayList<Book> getbookShelf() {
		return books;
	}
	
	
	/*Add book to BookShelf*/
	public void addbook(Book book) {
		char title_firstletter = book.title.charAt(0);
		if (title_firstletter == bookshelf_letter) {
			books.add(book);
		}
		else {
			return;
		}
	}
	
	/*Removes book from BookShelf*/
	public void removebook(Book book) {
		books.remove(book);
	}
}
