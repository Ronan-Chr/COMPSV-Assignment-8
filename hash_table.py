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
    ''' This method initializes a Node object with a key, value, and a pointer to the next node. '''
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

    ''' Insitializes the tbale with a size and an empty space'''
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size

    
    def hash_function(self, key: str) -> int:
        ''' This method takes a string key and returns an index in the array. '''
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    ''' This method inserts a new contact into the hash table. It handles collisions using linked lists. '''
    def insert(self, key: str, value: str) -> None:
        index = self.hash_function(key)
        current = self.data[index]

        '''Empty slot check and if empty create a new node with the key and value at thhe empty space.'''
        if current is None:
            self.data[index] = Node(key, Contact(key, value))
            return

        '''Follows the chain/map and updates names that exists'''
        while True:
            if current.key == key:
                current.value.number = value
                return
            if current.next is None:
                break 
            current = current.next

        current.next = Node(key, Contact(key, value))

    ''''''
    def search(self, key: str):
        index = self.hash_function(key)
        current = self.data[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next 
        return None

    def print_table(self) -> None:
        '''Prints the indexs of the has tables with the contacts and names attatched'''
        for i in range(self.size):
            current = self.data[i]
            if current is None:
                print(f"Index {i}: Empty")
            else:
                line = f"Index {i}: "
                while current is not None:
                    line += f"- {current.value} "
                    current = current.next
                print(line)
                

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
print(node1.next)  # Output: None

'''Tests the Hashtable Methods'''
'''Initializing the size of the hastable'''
table = HashTable(10)
table.print_table()

'''Inserts rebecca and john into hashmap'''
table.insert("John", "908-876-1234")
table.insert("Rebecca", "111-555-0002")
table.print_table()

'''Search for John and his number'''
contact = table.search("John")
print("\n Search result:", contact)

'''Edge case of duplicate name different number dupe keys'''
table.insert("Rebecca", "098-765-4321")
table.print_table()

'''Edge case of searching for a nobody (Not in the table)'''
print(table.search("Nobody")) #Should be None

'''Edge case for Amy / May'''
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-4444")
table.print_table()