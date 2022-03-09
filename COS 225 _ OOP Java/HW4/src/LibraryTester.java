
public class LibraryTester {

	public static void main(String[] args) {
		/*Instantiates a new BookShelf for letter 'O' and 'T'*/
		BookShelf bookshelf_O = new BookShelf();
		bookshelf_O.set_bookshelf_letter('O');
		
		BookShelf bookshelf_T = new BookShelf();
		bookshelf_T.set_bookshelf_letter('T');

		/*Prints the two BookShelf objects*/
		System.out.println(bookshelf_O);
		System.out.println(bookshelf_T);
		
		/*Instantiates four books w/ genres*/
		Book book1 = new Book("One of a Kind","Fantasy");
		Book book2 = new Book("The Heart of the Betrayed", "Romance");
		Book book3 = new Book("The Vision of Roses", "Crime");
		Book book4 = new Book("Our Hill of Stars", "Science Fiction");
		
		/*Prints each of the four books on a separate line*/
		System.out.println(book1);
		System.out.println(book2);
		System.out.println(book3);
		System.out.println(book4);
		
		/*Attempts to add each book to BOTH BookShelfs*/
		bookshelf_O.addbook(book1);
		bookshelf_T.addbook(book1);
		
		bookshelf_O.addbook(book2);
		bookshelf_T.addbook(book2);
		
		bookshelf_O.addbook(book3);
		bookshelf_T.addbook(book3);
		
		bookshelf_O.addbook(book4);
		bookshelf_T.addbook(book4);
		
		/*Prints both BookShelfs on separate lines*/
		System.out.println(bookshelf_O);
		System.out.println(bookshelf_T);
		
	}

}
