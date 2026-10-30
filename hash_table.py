class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    ''' initializes what Contact class will have being the name and number of the contact. '''
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    ''' This method returns a string representation of the contact in the format "name: number". '''
    def __str__(self) -> str:
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    pass # Delete this line when implementing the class

# Test your hash table implementation here.  
''' Make sure to test the Contact class as well. I dont know what happened but the bottom view terminal in VS wasnt displaying the output of the print statements. I ended up restarting VS and without changing anything it started working and displaying the output of the print statements. I am not sure what happened but it is working now. '''
contact1 = Contact("Riley", "123-456-7890")
print(contact1)  # Output: Riley: 123-456-7890
print(contact1.name)  # Output: Riley
print(contact1.number)  # Output: 123-456-7890

''' Test the Node class prints'''
node1 = Node("Riley", contact1)
print(node1.key)  # Output: Riley
print(node1.value)  # Output: Riley: 123-456-7890