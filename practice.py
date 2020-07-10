#  Notes from lecture w/Beej

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f'HashTableEntry({repr(self.key)},{repr(self.value)})'

data = [None] * 8

def my_hashing_function(s):   # Returns a number that is the um of the bytes that made up the string
    string_bytes = s.encode()

    total = 0

    for b in string_bytes:
        total += b

    return total  

def get_slot(s):      # Makes sure that the number fits into the array; becomes the index to store data
    hash_val = my_hashing_function(s)
    return hash_val % len(data) 
    

def get(key):               # O(1) operation
    slot = get_slot(key)
    hash_entry = data[slot] 

    if hash_entry is not None:
        return hash_entry.value

    return None

def put(key, value):        # O(1) operation
    slot = get_slot(key)
    data[slot] = HashTableEntry(key, value)
    
def delete(key):
    put(key, None)


put("Karen", 497)
put("cat", 514)

#print(data)

print(get("Karen"))

# print(my_hashing_function("dog"))  #314
# print(my_hashing_function("cat"))  #312
# print(my_hashing_function("elephant"))#849
# print(my_hashing_function("foo"))#324
# print(my_hashing_function("bar"))#309

# print(get_slot("dog"))  # 2
# print(get_slot("cat"))  # 0
# print(get_slot("elephant"))# 1
# print(get_slot("foo"))# 4
# print(get_slot("bar"))# 5

print (get("bar"))