contacts=[]
def add_contact():# Function to add a new contact
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact added successfully!")
def view_contacts():# Function to view all contacts
    if len(contacts) == 0:
        print("\nNo contacts found.")
    else:
        print("\nContact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
def search_contact():# Function to search for a contact
    search= input("\nEnter the name or phone number to search: ")
    found = []
    count=0
    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            found.append(contact)
            count=1
    if (count==0):
        print("\nNo matching contacts found.")
    else:
        print("\nMatching Contacts:")
        for contact in found:
             print(f"Name: {contact['name']}, Phone: {contact['phone']}")
def update_contact():# Function to update a contact
    search = input("\nEnter the name or phone number of the contact to update: ")
    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            print("\nContact found.")
            contact['name'] = input("\nEnter the new name: ")
            contact['phone'] = input("Enter the new phone number: ")
            contact['email'] = input("Enter the new email address: ")
            contact['address'] = input("Enter the new address: ")
            print("Contact updated successfully!")
            return
    print("\nNo matching contact found.")
def delete_contact():
    count=0
    name=input("Enter the name of the contact to delete:")
    for contact in contacts:
        if name.lower() in contact['name'].lower()or name.lower()in contact['phone']:
          contact=contacts.clear()
          print("deleted successfully")
          count=1
    if(count==0):
        print("not found")   
def run():
    n=int(input("\nenter your choice:(1/2/3/4/5)"))
    if(n==1):
       add_contact()
    elif(n==2):
       view_contacts()
    elif(n==3):
       search_contact()
    elif(n==4):
       update_contact()
    elif(n==5):
        delete_contact()
    m=input("you want to continue(yes/no)").lower()
    if(m=="yes"):
       run()
    elif(m=="no"):
       while False:
           break
print("\n1.Add contact.\n2.view contacts.\n3.search contact.\n4.update contact.\n5.delete contact.")
run()       
