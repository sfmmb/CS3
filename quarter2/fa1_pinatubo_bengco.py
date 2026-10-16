class Publication:
    _title:str
    _author:str
    def __init__(self, title, author):
        self._title = title
        self._author = author
    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def set_title(self, title):
        self._title = title
    def set_author(self, author):
        self._author = author
    def display_info(self):
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")

class Book(Publication):
    _number_of_pages = 1 #default value of 1, because a book cannot have 0 pages
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self._number_of_pages = number_of_pages
    def get_number_of_pages(self):
        return self._number_of_pages
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages < 0:
            print("Number of pages must be positive.")
        else:
            self._number_of_pages = number_of_pages
    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.get_number_of_pages()}")

class Magazine(Publication):
    _issue_number:int
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self._issue_number = issue_number
    def get_issue_number(self):
        return self._issue_number
    def set_issue_number(self, issue_number):
        self._issue_number = issue_number
    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.get_issue_number()}")

#Sample Code Workflow:
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dogen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information")
pub1.display_info()

print("\nBook Information")
book1.set_number_of_pages(-310)
book1.display_info()

print("\nMagazine Information")
mag1.display_info()
