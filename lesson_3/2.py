class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " села.")

my_dog = Dog("willy", 6)
print(my_dog.name)
my_dog.sit()

my_dog1 = Dog("Lucy", 3)