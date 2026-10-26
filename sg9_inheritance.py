class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    @property
    def get_title(self):
        return self.__title
    @property
    def get_author(self):
        return self.__author
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_of_pages)
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")
    @property
    def get_number_of_pages(self):
        return self.__number_of_pages

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)
    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")
    @property
    def get_issue_number(self):
        return self.__issue_number

# TEST RUN

#First set of Objects
pub1 = Publication("Harry Potter", "J.K. Rowling")
book1 = Book("The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", 400)
mag1 = Magazine("Vogue", "Various Authors", 140)

print(f"\nPublication Information:")
pub1.display_info()

print(f"\nBook Information:")
book1.set_number_of_pages(-400)
book1.display_info()
print(f"Number of Pages: {book1.get_number_of_pages}")

print(f"\nMagazine Information:")
mag1.set_issue_number(121)
mag1.display_info()
print(f"Issue Number: {mag1.get_issue_number}")

print(f"\n-------------------------")

#Second set of Objects
pub2 = Publication("The Diary of a Wimpy Kid", "Jeff Kinney")
book2 = Book("Percy Jackson and the Lightning Thief", "Rick Riordan", 416)
mag2 = Magazine("Harper's Bazaar", "Various Authors", 170)

print(f"\nPublication Information:")
pub2.display_info()

print(f"\nBook Information:")
book2.set_number_of_pages(-416)
book2.display_info()
print(f"Number of Pages: {book2.get_number_of_pages}")

print(f"\nMagazine Information:")
mag2.set_issue_number(167)
mag2.display_info()
print(f"Issue Number: {mag2.get_issue_number}")

