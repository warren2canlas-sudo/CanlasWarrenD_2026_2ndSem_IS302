class Book:
    def __init__(self, book_title, book_author, book_year):
        self.book_title = book_title
        self.book_author = book_author
        self.book_year = book_year

    def display_book(self):
        print("Title:", self.book_title)
        print("Author:", self.book_author)
        print("Year:", self.book_year)
        print("----------------------")


# Create 3 book objects
book1 = Book("Tarzan", "Edgar Rice Burroughs", 1912)
book2 = Book("Jack and the Beanstalk", "Joseph Jacobs", 1807)
book3 = Book("Peter Pan", "J.M. Barrie", 1991)

# Display book information
book1.display_book()
book2.display_book()
book3.display_book()