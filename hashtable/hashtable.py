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

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
       self.capacity = capacity
       self.storage = [None] * capacity
       self.item_total = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # number of things stored in the hash table / number of slots 
        return self.item_total/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_prime = 1099511628211 
        FNV_offset_basis = 14695981039346656037
        # Your code here
        hashed_key =  FNV_offset_basis

        byte_keys = key.encode()

        for byte in byte_keys:
            hashed_key = hashed_key * FNV_prime
            hashed_key = hashed_key ^ byte
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
        #  Old Code:
        
        # location = self.hash_index(key)
        # self.storage[location] = HashTableEntry(key, value)

        #--------------------------------------------------
        # Update Code:

        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)

        # hash the key, to get the index
        location = self.hash_index(key)

        # check the index, if it's empty put a node there
        if self.storage[location] is None:
            self.storage[location] = HashTableEntry(key, value)
            self.item_total += 1
      
        # otherwise, iterate through the linked list
        else:
            current_node = self.storage[location]
            while current_node is not None:
        ## Check for the key, update value if it's there
                if current_node.key == key:
                    current_node.value = value
                    break
        ## if we reach the end, add a new node
                elif current_node.next == None:
                    current_node.next = HashTableEntry(key, value)
                    self.item_total += 1
                    break
                else:
                    current_node = current_node.next
       

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        # # Old Code:
        # location = self.hash_index(key)
        # self.storage[location] = None

        #----------------------------------------------------
        # Updated Code:

        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        location= self.hash_index(key)
        # if there's a None at the index
        if self.storage[location] is None:
            print("WARNING: sound the alarm, key not found")
            return

        else:
            current_node = self.storage[location]
        # If the target node is the head
            if current_node.key == key:
                self.storage[location] = current_node.next
                self.item_total -= 1
                
            else:
        # And any other node
                previous_node = current_node
                current_node = current_node.next

                # now we iterate!
                while current_node is not None:
                    if current_node.key == key:
                        previous_node.next = current_node.next
                        self.item_total -= 1
                        return

                    previous_node = current_node
                    current_node = current_node.next

        # And if it's not found in the linked list
                print("WARNING got all the way through and did not find it")
          


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

        # if there's nothing at the index
        if self.storage[location] is None:
            return None

        # otherwise, go to the index, iterate through the linked list, and look for the key
        else:
            current_node = self.storage[location]

            while current_node is not None:

                if current_node.key == key:
                    return current_node.value

                current_node = current_node.next

            return None





    def resize(self, new_capacity):
    #     """
    #     Changes the capacity of the hash table and
    #     rehashes all key/value pairs.

    #     Implement this.
    #     """
    #     # Your code here
     
                # save our old storage
        old_storage = self.storage
        # make a new, bigger storage!
        self.storage = [None] * new_capacity
        self.capacity = new_capacity

        # iterate through our hashlist
        for bucket in old_storage:
        ## Iterate through every linked list
            while bucket is not None:
                ## re-insert key, value
                key = bucket.key
                value = bucket.value
                self.put(key, value)
                # go on to the next node
                bucket = bucket.next




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
