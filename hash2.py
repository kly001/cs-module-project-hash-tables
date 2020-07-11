# big ideas: use all the info you can to scramble stuff, even the bits
## use bit shifting to get a new weird sort-of-random number

def djb2(key):
    hash 5381

    for char in key:
        hash = ((hash<<5) + hash) + ord(char)
        # hash = (( hash * 33) + hash) + ord(char)
    return hash


hash_table = [None] * 8

class HashTableItem:
    def __init__(self. key, value):
        self.key = key 
        self.value = value 
        self.next = next 



def my_hash(str):
    s_utf8 = str.encode()

    total = 0
    for c in s_utf8:
        total += c

    return total

def put(key, value):
    hashed_key = my_hash(key)

    index= hashed_key % len(hash_table)

    # print a warning if we are going to overwrite
    if hash_table[index] is not None:
        print("What is happening?")

    hash_table[index] = HashTableItem(key, value)

def get(key):
     hashed_key = my_hash(key)
     index= hashed_key % len(hash_table)

     table_item = hash_table[index]

     return table_item.value

def delete(key):
    hashed_key = my_hash(key)
    index= hashed_key % len(hash_table)
    hash_table[index] = None

put("hello", "hello world")
put("olleh", "overriding original")

print(hash_table)
print(get("hello"))
delete("hello")
print(hash_table)

#------------------------------------------------------
​
'''
Index  Chain (linked list)
----   ---------------
0      ("qux", 54)  -> None
1      ("foo", 29)  -> None
2      ("bar", 99)  -> None
3      LL[self.head = Node(self.key = "fox", self.value = 101) -> Node("tree", 209) -> None]
4      -> None
​
put("foo", 42)   # hashed to index 1
put("foo", 29)   
put("bar", 99)   # hashes to index 2
put("baz", 38)   # hashes to index 1! collision!
put("qux", 54)   # hashes to 0
put("fox", 101)  # hashes 3
put("tree", 209) # hashes 3
​
get("qux")
get("foo")
get("fred")  # hashes to 0 --> return None
​
​
delete("baz")
​
'''
​
# Insert a LL into the hash table, when you put something in
# hash table main data structure: [LL, LL, LL, None, LL, None, None]
​
# how to make the LL work with our hash table?
## ensure each node has a key as well as a value
## change methods to use keys, not just values, where necessary
## write a new method, maybe insert_or_overwrite
### search for the key, if found, overwrite
### otherwise, add a new node

#--------------------------------------------------------------------

