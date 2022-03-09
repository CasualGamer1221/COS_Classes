
import java.util.ArrayList;

public class BookShelf {
	/*Declares variables and creates an ArrayList of books w/ size of 8*/
	char bookshelf_letter;
	ArrayList<Book> books = new ArrayList<>(8);

	
	/* Default constructor , setting each value in ArrayList to null */
	public BookShelf() {
		for (int i = 0; i < 8; i++) {
			books.add(i, null);
		}
	}

	
	/* getters and setters */
	public char get_bookshelfLetter() {
		return bookshelf_letter;
	}

	public void set_bookshelf_letter(char letter) {
		this.bookshelf_letter = letter;
	}

	public ArrayList<Book> getbookShelf() {
		return books;
	}

	
	/* Adds book to BookShelf if the 1st character of the book title matches the character for the bookshelf_letter
	 * and if there is room on the BookShelf*/
	public void addbook(Book book) {
		char title_firstletter = book.title.charAt(0);
		if (title_firstletter == bookshelf_letter) {
			for (int i = 0; i < 8; i++) {	
				if (books.get(i)==null) {
					books.set(i,book);
					return;
				}
			}
		}
			else {
				return;
			}
	}

	
	/* Removes book from BookShelf */
	public void removebook(Book book) {
		books.remove(book);
	}

	/*Overridden toString that outputs the books that are on the BookShelf
	 * if there are no books, outputs EMPTY*/
	@Override
	public String toString() {
		String output_string = "";
		int items = 8;
		for (int i = 0; i < 8; i++) {
			if (books.get(i) != null) {
				output_string += (books.get(i).title + "   ");
				items--;
			} 
			else if (items == 0) {
				return "Empty";
			}
		}
		return output_string;
	}

}
