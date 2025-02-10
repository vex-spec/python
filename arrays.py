courses =["MIT","cybersecurity","Datascience"]
print(courses)

# Accessing an element
print(courses[2])

# Looping through an array
for x in courses :
    print("Course is",x)

# Adding a new element in to an array
courses.append(" Laravel")
print(courses)

# Removing an element from an array
courses.remove("cybersecurity")
print(courses)