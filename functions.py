# Built-in functions/standard -library function

y = max(45,89.75,56,78,89,14,1000)
print("The maximum value is",y)

x = min(12,34,566,1,0,67)
print("The minimum value is",x)

# User-defined Functions
def school():
    print("eMobilis")

school()


def add():
    num1 = 5
    num2 = 3
    print(num1+num2)
add()

# Parameter/variable and Argument/value
def multiply(a, b):
    print(a*b)
multiply(6,5)
multiply(10,56)
multiply(5,20)


def employee(name, age, gender, salary,position):
    print(name,age,gender,salary,position)
employee("Aby", 25, "female",55000,"ceo")
employee("setsuna", 25, "male",5000,"managing director")
employee("lahito", 25, "male",95000,"director")
employee("tanjiro", 25, "male",100000,"deplomat")
employee("nazuko", 25, "female",90000,"deputy director")


# A program to display details of 5 patients
# fullname, gender, age,disease

def patient (fullname, gender, age, disease):
    print(fullname, gender, age, disease)

patient("Ichiro Nakata", "male", 27, "Broken ribs")
patient("Oma Tokita", "male", 28, "Broken leg")
patient("Setsuna Kiriu", "male", 27, "Broken ribs")
patient("Ray Knight", "female", 24, "Broken rist")
patient("Jun Sekibayashi", "male", 27, "Broken ribs")