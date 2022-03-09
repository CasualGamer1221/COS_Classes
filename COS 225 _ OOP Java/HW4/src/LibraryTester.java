
public class LibraryTester {

	public static void main(String[] args) {
		BookShelf bookshelf_O = new BookShelf();
		bookshelf_O.set_bookshelf_letter('O');

		BookShelf bookshelf_T = new BookShelf();
		bookshelf_T.set_bookshelf_letter('T');

		System.out.println(bookshelf_O);
		System.out.println(bookshelf_T);
		
		Book book1 = new Book("One of a Kind","Fantasy");
		Book book2 = new Book("The Heart of the Betrayed", "Romance");
		Book book3 = new Book("The Vision of Roses", "Crime");
		Book book4 = new Book("Our Hill of Stars", "Science Fiction");
		
		System.out.println(book1);
		System.out.println(book2);
		System.out.println(book3);
		System.out.println(book4);
		
		bookshelf_O.addbook(book1);
		bookshelf_T.addbook(book1);
		
		bookshelf_O.addbook(book2);
		bookshelf_T.addbook(book2);
		
		bookshelf_O.addbook(book3);
		bookshelf_T.addbook(book3);
		
		bookshelf_O.addbook(book4);
		bookshelf_T.addbook(book4);
		
		
		
		
		
		System.out.println(bookshelf_O);
		System.out.println(bookshelf_T);
		
		//System.out.println(bookshelf_O.getbookShelf());
		
	}

}
