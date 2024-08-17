class library:
    def __init__(self,list, name):
        self.name=name
        self.booklist=list
        self.lendDict={}

    def displayBook(self):
        print("Available Books")
        for book in self.booklist:
            print(book)

    def lendBook(self, book,name):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:name})
            print("Updated Successfully")
        else:
            print(f"book is already own by{self.lendDict[book]}")

    def addBook(self,book):
        self.booklist.append(book)
        print("book has been added")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__=='__main__':
    jv = library(['python','c++','c#','dsa','dbms','java'],"jvlibrary")

    while(True):
        print(f"welcome to the {jv.name}. Enter the choice to continue")
        print("1.Display Books")
        print("2.Land a Book")
        print("3.Add a Book")
        print("4.Return a Book")
        user_choice = input()
       
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice==1:
            jv.displayBook()

        elif user_choice==2:
            book = input("Enter the name of the book for land")
            name = input("enter name")
            jv.lendBook(book,name)

        elif user_choice==3:
            book = input("Enter the name of the book for add")
            jv.addBook(book)

        elif user_choice==4:
            book = input("Enter the name of the book for return book")
            jv.returnBook(book)

        else:
            print("Not valid option")

        
        print("Press q to quit and c to continue")
        user_choice2=""
        
        while (user_choice2 !="q" and user_choice2 !="c"):
            user_choice2 = input()
           
            if user_choice2 =="q":
                exit()

            elif user_choice2 =="c":
                continue
