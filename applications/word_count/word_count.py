def word_count(s):
#     # Your code here

   word_count = len(s.split()) 
   print("There are", word_count, "words in the input string : ",s)




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    