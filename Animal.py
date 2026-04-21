class Animal:
    def __init__(self, n, s):
        self.name = n
        self.sound = s

    def speak(self):
        print(self.name, "says", self.sound)


dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

dog.speak()
cat.speak()