contacts = []

def add_contacts():
    name = input("Enter contact Name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = {
        "name" : name,
        "phone" : phone,
        "email" : email
    }
    contacts.append(contact)
    print("Contacts saved successfully")

def view_contacts():
    if not contacts:
        print("No saved contacts found\n")
    else:
        print(".....Contacts List....")
        for i, contact in enumerate(contacts, start = 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()

def search_name():
    search_name = input("Enter the name: ").lower()
    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name:
            print(f"Name: {contact['name']}, Contact: {contact['phone']}, Email: {contact['email']}")
            found = True
            break
        if not found:
            print("Contact not found")

while True:
    print("..........Add Contact.........")
    print("1. Add Contact")
    print("2. View ontacts")
    print("3. Search ontacts")
    print("4. Exit")
    choice = input(" Choose an option: ")

    if choice == "1":
        add_contacts()
    
    elif choice == "2":
        view_contacts()
    
    elif choice == "3":
        search_name()
    
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print(" Invalid Choice. Please input correct option")

    
