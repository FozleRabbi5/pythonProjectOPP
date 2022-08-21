class Library:
    def __init__(self, list, name):
        self.book_list = list
        self.name = name
        self.lend_dict = {}

    def display_books(self):
        print(f"we have following books in our library {self.name}")
        for book in self.book_list:
            print(book)

    def lend_books(self, user, book):
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book: user})
            print("Lender- book database has been updated")
        else:
            print(f"Book is already being used by {self.lend_dict[book]}")

    def add_books(self, book):
        self.book_list.append(book)
        print(f"{book} has been added to the book list")

    def return_book(self, book):
        self.book_list.remove(book)


if __name__ == "__main__":
    harry = Library(["python", "harry porter", "Rich Daddy Poor Daddy"], "codewithharry")

    while(True):
        print(f"welcome to the {harry.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Books")
        print("3. add Books")
        print("4. return Books")

        user_choice = int(input())

        if user_choice == 1:
            harry.display_books()
        elif user_choice == 2:
            user = input("Enter your name")
            book = input("enter a book name")
            harry.lend_books(user, book)

        elif user_choice == 3:
            book = input("enter a book to add")
            harry.add_books(book)
        elif user_choice == 4:
            book = input("enter book name")
            harry.return_book(book)
        else:
            print("Not a valid option")

        print("press q to quit and c to continue")
        user_choice2 = input()
        while user_choice2 == "q" and user_choice2 == "c":

            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue

            else:
                print("invalid keyword")



