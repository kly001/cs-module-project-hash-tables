class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

# class ListNode:
#         def __init__(self, value):
#             self.value = value
#             self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    # def find(self, value):
    #     current = self.head

    #     while current is not None:
    #         if current.value == value:
    #             return current

    #         current = current.next
        
    #     return None
    
    # def insert_at_tail(self, value):
    #     node = ListNode(value)

    #     # if there is no head
    #     if self.head is None:
    #         self.head = node
    #     else:
    #         current = self.head

    #         while current.next is not None:
    #             current = current.next
    #         current.next = node

    # def delete(self, value):
    #     current = self.head

    #     # if there is nothing to delete
    #     if current is None:
    #         return None

    #     # when deleting head
    #     if current.value == value:
    #         self.head = current.next
    #         return current

    #     # when deleting something else
    #     else:
    #         previous = current
    #         current = current.next

    #         while current is not None:
    #             if current.value == value: # found it!
    #                 previous.next = current.next  # cut current out!
    #                 return current # return our deleted node

    #             else:
    #                 previous = current
    #                 current = current.next

    #         return None # if we got here, nothing was found!

    # def insert_at_head(self, node):
        # node.next = self.head
        # self.head = node



class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
       self.capacity = capacity
       self.storage = [None] * capacity
       self.item_total = None


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # number of things stored in the hash table / number of slots 
        load = self.item_total/self.capacity
        return load


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_prime = 1099511628211 
        FNV_offset_basis = 14695981039346656037
        # Your code here
        hash =  FNV_offset_basis
        for x in key:
            hash = hash * FNV_prime
            hash = hash ** ord(x)
        return hash
    

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here                                                                                                                               
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash 
        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        location = self.hash_index(key)
        self.storage[location] = HashTableEntry(key, value)
       

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        location = self.hash_index(key)
        self.storage[location] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #  # Old Code
        # location = self.hash_index(key)
        # hash_entry = self.storage[location]

        # if hash_entry is not None:
        #     return hash_entry.value

        # return None
        #------------------------------------------
        # Updated Code
        location = self.hash_index(key)
        current = self.storage[location]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None


        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
