from os import system
from time import sleep
myLibrary_name = input("Enter a Name for Your Library ")
system('cls')

# the program will start from here
print("Before Starting The Library Let's add Some Books, Enter the Book Nmae to add: \ntype 'Done' when you're Done: ")
list_books = [] #this is the main list of books
while True: # this block is for adding books into the library while starting first time
    books = input()
    cap = books.capitalize()
    list_books.append(cap)
    if cap == "" or cap == " ":
        print(f"book name can not be Empty {cap}")
        list_books.pop()
    elif cap == "Done":
        list_books.pop()
        print("Starting.....")
        sleep(1)
        system('cls')
        print("You added these Books")
        a = 0
        for items in list_books:
            a = a + 1
            print(a, " ", items)
        continuee = input("press enter to continue")
        break
list_of_books = list_books.copy()

def set_verification(): # while running first time this function will create two files for username and password
       try:
           open("username.txt", "x")
           with open("username.txt", "r") as u:
               if u.read() == "":
                   with open("username.txt", "w") as u:
                       system('cls')
                       print("It seems you are running the Software for the first time. Let's create your username and password")
                       usrnm = input("Set Your Username: ")
                       usrnm = usrnm.capitalize()
                       u.write(usrnm)
                       u.close()
           open("pass.txt", "x")
           with open("pass.txt", "r") as p:
               if p.read() == "":
                   with open("pass.txt", "w") as p:
                       pswd = input("Set Your Password: ")
                       pswd = pswd.capitalize()
                       p.write(pswd)
                       p.close()
                       print("username and password have been set successfully !")
                       sleep(1.5)
                       system('cls')
       except Exception:
           pass

# main class for library
class Library:
    def __init__(self, list_of_books, library_name):
        set_verification()
        self.list_of_books = list(list_of_books)
        self.list_of_books.sort()
        self.ref_copy = self.list_of_books.copy()
        self.library_name = library_name


    def display_books(self):
        print(self.list_of_books)

    lended_books = {} #this dictionary will hold all the records of lended books
    def lend_books(self):
        try:

            self.lend_book_name = input(" enter book name to lend ")
            self.lend_book_name = self.lend_book_name.capitalize()
            username = input("Enter Your Name: ")
            username = username.capitalize()
            self.list_of_books.remove(self.lend_book_name)
            Library.lended_books[self.lend_book_name] = username
            print("book Lended Successfully")
            sleep(1.5)
            system('cls')
        except ValueError:
            print("Book Not Found!")
            sleep(1.5)
            system('cls')

    def return_book(self):

        self.return_book_name = input("Enter book name to Return: ")
        a = self.return_book_name.capitalize()
        belong = a in self.ref_copy
        already = a in self.list_of_books
        if belong == False:
            print("Sorry, this book dosen't belog to us! "
                  "If You want add books then select 'Add a Book'")
            sleep(3)
            system('cls')
        elif already == True:
            print("This Book Present Already! ")
            sleep(1.5)
            system('cls')
        else:
            self.list_of_books.append(a)
            self.list_of_books.sort()
            del Library.lended_books[a]
            print("Book Returned Successfully!")
            sleep(1.5)
            system('cls')

    def lend_list(self):
        try:
            if len(self.lended_books) == 0:
                print("No Records Found!")
            else:
                print(f"current lend list is as [book name : person name]: {self.lended_books} ")

        except AttributeError:
            print("No Records Found!")
    def add_book(self):
        self.add_book_name = input("Enter book name to add into the Library: ")
        a = self.add_book_name.capitalize()
        add_belong = a in self.ref_copy
        already = a in self.list_of_books
        if already == True:
            print("This Book is Already presennt in the Library")
        elif add_belong == True:
            print("This Book Already Exists! but Lended!. Get Lend Book List for more info.")
            sleep(2.7)
            system('cls')
        else:
            self.list_of_books.append(a)
            self.list_of_books.sort()
            print("Book Added Successfully! ")
            sleep(1.5)
            system('cls')

yogesh = Library(list_of_books, myLibrary_name) #creating instance for library with two arguments which are user defined


# here is the main infinite loop to run the library code continuously
try:
    system('cls')
    while True:

        print(f"\n\nWelcome to {myLibrary_name}")

        def operation():
            #system('cls')

            operation = int(input("\nwhat do you want to do: \n1.Display Books \n2.Lend Books"
                                  " \n3.Return Book \n4.Get Lend book List \n5.Add a Book\n............:"))
            if operation == 1:
                system('cls')
                yogesh.display_books()
            elif operation == 2:
                # system('cls')
                yogesh.lend_books()
            elif operation == 3:
                #system('cls')
                yogesh.return_book()
            elif operation == 4:
                system('cls')
                yogesh.lend_list()
            elif operation == 5:
                system('cls')
                print("You Need to Verify Your Identity For This Operation. ")
                while True:
                    while True:
                        with open("username.txt", "r") as u:
                            u_rd = u.read()
                            usr = input("\nEnter Your Username: ")
                            usr_cap = usr.capitalize()
                            if usr_cap == "Exit":
                                break
                            elif u_rd == usr_cap:
                                print("Username Verified!")
                                u.close()
                                while True:
                                    with open("pass.txt", "r") as p:
                                        p_rd = p.read()
                                        pas = input("Enter Your Password: ")
                                        pas_cap = pas.capitalize()
                                        if pas_cap == "Exit":
                                            break
                                        elif p_rd == pas_cap:
                                            print("Verification Completed!")
                                            p.close()
                                            yogesh.add_book()
                                            break
                                        else:
                                            print("Incorrect Password! Please Try Again")
                            else:
                                print("Username can't be found")

                            if usr_cap == "Exit":
                                break
                            elif u_rd == usr_cap and p_rd == pas:
                                break
                    if u_rd == usr_cap and p_rd == pas:
                        break
                    elif usr_cap == "Exit" or pas_cap == "Exit":
                        break
            else:
                print("Invalid Input! Please Try Again")
        operation()
except ValueError:
    print("Invalid Input...")
    sleep(1)
    print("Exiting...")
    sleep(1.5)
    exit()
