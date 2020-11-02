# Collections required for sorting dictonary.
import collections

def findwords():
    # Open File to read
    f = open("HIT137cdu.txt","r")
    wordlist = {}
    # For each line in file
    for line in f:
        # For each word in file
        for word in line.split():
            word = word.lower()
            # For each letter in word
            for letter in word:
                # If letter is not alphabet letter, remove it. For example '!' and '.'.
                if ord(letter) < 97 or ord(letter) > 122:
                    word = word.replace(letter,'')
            # If letter not in dictionary, add it, else increase it's count
            if word not in wordlist:
                wordlist[word]=1
            else:
                wordlist[word]+=1
    # Sort the dict by alphabet
    sortedlist = collections.OrderedDict(sorted(wordlist.items()))
    # Print sorted list
    for k, v in sortedlist.items(): print(k, v)
    f.close()

# Call function
findwords()

# Prevent app from closing.
print("")
exit = input("Press enter to close ")