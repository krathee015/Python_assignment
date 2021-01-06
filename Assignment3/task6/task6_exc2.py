# Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension

students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']

x = {stu:sub for(stu,sub) in zip(students,subjects)}
print(x)
