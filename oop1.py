class student :
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def study(self):
        print(self.name,"is studying")

student1 = student("oma","male",20)
print(student1.name,"gender","age")
student1.study()


student2 = student("Abigael","female", 17)
print(student2.name,"gender","age")
student2.study()


