# Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:

f = open("doc.txt","r")
for line in f:
    if len(line)%2 ==0:
        print(line)
f.close()

