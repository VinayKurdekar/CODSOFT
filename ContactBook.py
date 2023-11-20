class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("===== Contact List =====")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"Contact {index}:")
                print(contact)
                print("------------------------------")
        else:
            print("Contact list is empty.")

    def search_contact(self, search_query):
        found = False
        for contact in self.contacts:
            if search_query in [contact.name.lower(), contact.phone_number]:
                print("Contact found:")
                print(contact)
                found = True
                break
        if not found:
            print("Contact not found.")

    def update_contact(self, search_query, updated_contact):
        for contact in self.contacts:
            if search_query in [contact.name.lower(), contact.phone_number]:
                contact.name = updated_contact.name
                contact.phone_number = updated_contact.phone_number
                contact.email = updated_contact.email
                contact.address = updated_contact.address
                print("Contact updated successfully.")
                break
        else:
            print("Contact not found.")

    def delete_contact(self, search_query):
        for contact in self.contacts:
            if search_query in [contact.name.lower(), contact.phone_number]:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                break
        else:
            print("Contact not found.")

def create_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone_number, email, address)

def main():
    contacts = ContactList()

    while True:
        print("\n====== Contact Management System ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            new_contact = create_contact()
            contacts.add_contact(new_contact)
        elif choice == '2':
            contacts.view_contacts()
        elif choice == '3':
            search_query = input("Enter name or phone number to search: ").lower()
            contacts.search_contact(search_query)
        elif choice == '4':
            search_query = input("Enter name or phone number to update: ").lower()
            updated_contact = create_contact()
            contacts.update_contact(search_query, updated_contact)
        elif choice == '5':
            search_query = input("Enter name or phone number to delete: ").lower()
            contacts.delete_contact(search_query)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
