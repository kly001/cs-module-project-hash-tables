#  Practice from Lecture w/Tim Roy

#  my_array = ["hello","world","how",'are',"you","Karen"]  # O(n) time complexity

# Operations with O(1) using arrays:
    # append, pop
    # lookup
#### print("The word at index 5 in my_array is:", my_array[5])

# We need a hashing function that will give us the index of the word we are looking for.
## It must be deterministic
## It must be unique
#---------------------------------------------------------------

# take a string
# give us a number
# not unique

# def my_hash(str):
#     return len(str) 

# print("The length of the string 'Karen' is: ",my_hash("Karen")) # returns 3, the length of the string

#----------------------------------------------------------------
# ASCII assigns numbers to characters ==>  ord()
# UTF-8 (Uniform Transforamtion Format) ASCII plus additional letters/symbols 
#       from other languages; global applicable

# print("The ASCII value for uppercase letter 'K' is:" ,ord("K"))
# print("The ASCII value for lowercase letter 'a' is:" ,ord("a"))
# print("The ASCII value for lowercase letter 'r' is:" ,ord("r"))
# print("The ASCII value for lowercase letter 'e' is:" ,ord("e"))
# print("The ASCII value for lowercase letter 'n' is:" ,ord("n"))

# def my_hash2(str):
#     s_utf8 = str.encode()

#     for c in s_utf8:
#         print(c)
# print("The UTF-8 values for the letters in 'Karen':")
# my_hash2("Karen")

#----------------------------------------------------------------

def my_hash3(str):
    s_utf8 = str.encode()

    total = 0
    for c in s_utf8:
        total += c

    return total

karen_index = my_hash3("Karen") # 497; modulo = 2

my_arr = [None] * 5

karen_index = karen_index % len(my_arr)

my_arr[karen_index] = "Karen"

print(my_arr)

#------------------------------------------
world_index = my_hash3("world!") # 585; modulo = 0
print(" Initial world_index value:",world_index)  #585

world_index = world_index % len(my_arr)
print("world_index modulo my_arr length:",world_index)
my_arr[world_index] = "world value"

print(my_arr)

#----------------------------------------------
#  Insert into our hash map (PUT)
key = "key"
print("Initial key_index value:",my_hash3(key)) #329

key_index = my_hash3(key) % len(my_arr)
print("key_index modulo my_arr length: ",key_index)

my_arr[key_index] = "value"

print(my_arr)

#-------------------------------------------------

#access the value (GET)
key_index = my_hash3(key) % len(my_arr)
print(my_arr[key_index])

#----------------------------------------------------
# Steps to PUT (NOTE => Assumes you have an array and a hash function):
    # 1. Hash the word, get some number back from the hash function
    # 2. Modulo the number with array length to get the index
    # 3. Use index to insert the word

# Steps to GET (NOTE => Assumes you have an array and a hash function):
    # 1. Hash the key/word, get some number back from the hash function
    # 2. Modulo the number with array length to find the index
    # 3. Look up value at that index, return it

