


public class LibraryTester {

	public static void main(String[] args) {
		BookShelf bookshelf_O = new BookShelf();
		bookshelf_O.set_bookshelf_letter('O');

		BookShelf bookshelf_T = new BookShelf();
		bookshelf_T.set_bookshelf_letter('T');

		System.out.println(bookshelf_O);
		System.out.println(bookshelf_T);
	}

}
