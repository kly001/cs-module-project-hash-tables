def word_count(s):
#     # Your code here
# def Count_words(s):
   word_count = 1
   for i in range(len(s)):
      if(s[i] == ' ' or s == '\n' or s == '\t'):
         word_count += 1
   return word_count
# s = input("String to search is :")
# total = word_count(s)
# print("Total Number of Words in our input string is: ", total)


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))