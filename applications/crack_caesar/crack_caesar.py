# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

""" The Plan:
    1.  Get ciphertext.txt
    2.  Make sure text letters uppercase.
    2.  Create a dictionary to store the frequency of letters in the text.
    
    """
f = open("ciphertext.txt", "r")
 
if f.mode == "r":
    contents = f.read()

def count_letters(contents):
        contents = contents.upper()
        letter_freq = {}

        for letter in contents:
            if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if letter not in letter_freq:
                    letter_freq[letter] = 1
                else:
                    letter_freq[letter] += 1
        print(letter_freq)

if __name__ == "__main__":

      print(count_letters(contents))
