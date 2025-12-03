#Contact book application using python
contacts = []




def create_contact():                
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts to show.")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact['name']} - {contact['phone']} - {contact['email']}")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

#Iteration Process

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        create_contact()
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
