# Simple Contact Management System

contacts = {}  # Dictionary to store contacts: {name: {"phone": ..., "email": ...}}

def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name} | Phone: {info['phone']} | Email: {info['email']}")
    print("--------------------")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    phone = input(f"Enter new phone number ({contacts[name]['phone']}): ").strip()
    email = input(f"Enter new email ({contacts[name]['email']}): ").strip()
    contacts[name]["phone"] = phone if phone else contacts[name]["phone"]
    contacts[name]["email"] = email if email else contacts[name]["email"]
    print(f"Contact '{name}' updated successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    del contacts[name]
    print(f"Contact '{name}' deleted successfully!")

def menu():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


menu()
