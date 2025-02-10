#Parent class/super/bass
class animal :
    def speak(self):
        print("animal is speak")

#child class/sub class/derived class
class dog(animal) :
    def bark(self):
        print("dog is barking")


class cat(dog) :
    def meow(self):
        print("cat is meowing")


a = animal()

d = dog()

c = cat()

