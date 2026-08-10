#Create an address book that can get various inputs, store them, and retrieve them whenever needed.
import sys
def inital_phonebook():
    rows, cols = int(input("Please enter inital number of contacts: ")), 5
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in following oder (ONLY):"% (i+1))
        print("NOTE: * indicates mandatory feilds")
        print("............................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandtory field. Process exiting due to blank field...")
            if j == 1:
                temp.append(int(input("Enter phone number*:")))
            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter date of birth:" )))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Enter Category:" )))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
        phone_book.append(temp)
    print(phone_book)
    return phone_book
def menu():
    print("**********************************************************************************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY")
    print("**********************************************************************************************************************************")
    print("\tYou can now perform the following operations on this phinebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. display all contacts")
    print("6. Exit phonebook")
    choice = int(input("please anter your choice: "))
    return choice
def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter phone number: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail adress: ")))
        if i == 3:
            dip.append(str(input("Enter date of birth: ")))
        if i == 0:
            dip.append(str(input("Enter category: ")))
    pb.append(dip)
    return pb