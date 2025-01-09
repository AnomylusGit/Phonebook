import sys

def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts:")), 5
    

    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order(ONLY):"% (i+1))
        print("NOTE: * indicates mandatory fields")

        temp = []
        for j in range(cols):

            if j == 0:
                temp.append(str(input("Enter name*: ")))

                if temp[j] == '' or temp[j] == '':
                    sys.exit(
                        "Name is a mandatory field. Process exiting due to blank field..."
                    )
                if j == 1:
                        temp.append(int(input("Enter number*: ")))

                if j == 2:
                        temp.append(str(input("Enter e-mail adress: ")))

                        if temp[j] == '' or temp[j] == ' ':

                                temp[j] = None

                if j == 3:
                        temp.append(str(input("Enter date of birth(dd/mm/yy): ")))

                        if temp[j] == '' or temp[j] == ' ':

                            temp[j] = None
                phone_book.append(temp)
     print(phone_book)
     return phone_book

def menu():
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Delete all Contacts")
    print("4. Search Contact")
    print("5. Display all Contacts")
    print("6. Exit")
    choice = int(input("Enter your Choice"))
    return choice  

def  add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter Name")))
        if i == 1:
            dip.append(int(input("Enter Number")))
        if i == 2:
            dip.append(str(input("Enter E-mail")))
        if i == 3:
            dip.append(str(input("Enter DOB(Date of Birth)")))
        if i == 4:
            dip.append(str(input("Enter Category")))
    pb.append(dip)
    return (pb)

def delete_all(pb):
    return pb.clear()

ch=1
pb=initial_phonebook
while ch in (1, 2, 3, 4, 5):
    ch=menu
    if ch == 1:
        pb= add_contact(pb)
    elif ch == 2:
        pb= remove_existing(pb)
    elif ch == 3:
        pb= delete_all(pb)
    elif ch == 4:
        pb= search_existing(pb)
    elif ch == 5:
        pb= display_all(pb)
    else: 
		thanks()