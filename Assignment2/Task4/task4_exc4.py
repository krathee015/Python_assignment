print("Exercise 4")
print("hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically")

def sorted_seq (seq1):

    x = seq1.split('-')
    x.sort()
    print("After sorting: ",'-'.join(x))

str = input("Enter a hyphen-seperated sequence: ")
sorted_seq(str)
        
