class Animal:
    name=""
    sound=""
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(self.name, "says", self.sound)


dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")
dog.speak()
cat.speak()
