directory = "1 - Yeni Kisi Ekleme\n2 - Kisi Duzenleme\n3 - Kisi silme\n4 - Kisi arama"

def add_person():
    name = input("Name:").capitalize()
    number = input("Number:")
    telephone_directory[name] = number

def edit_person():
    person = input("Name:").capitalize()
    if person in telephone_directory:
        # print(rehber.items(kisi))
        edit = input("For name -> 'N'\nFor number -> 'C'\nFor delete -> 'D' ").upper()
        if edit == "N":
            new_name = input("YENI ISIM:").capitalize()
            telephone_directory[new_name] = telephone_directory.pop(person)
        elif edit == "C":
            new_number = input("New number:")
            telephone_directory[person] = new_number
        elif edit == "D":
            delete_person()
    else:
        print("No Match!")


def delete_person():
    delete = input("Name:").capitalize()
    ask = input("Are you sure?: Y / N").upper()
    if ask == "Y":
        telephone_directory.pop(delete)
    elif ask == "N":
        print("Cancelled!")

def search_person():
    search = input("Name:").capitalize()
    if search in telephone_directory:
        print("Number:",telephone_directory.get(search))
    else:
        print("No Match!")

telephone_directory = {}
while True:
    print("Welcome")
    print("For Quit -> 'q'")
    print(directory)
    Choose = input("Bir islem seciniz:")

    if Choose == "q":
        break
    elif Choose == "1":
        add_person()
    elif Choose == "2":
        edit_person()
    elif Choose == "3":
        delete_person()
    elif Choose == "4":
        search_person()
    else:
        print("Error! Try Again.")

    print(20*"-")
    print("Your Directory:")
    print(telephone_directory)
    print(20*"-")