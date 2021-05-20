class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


d = dog("Ellie", 7)
d2 = dog("Max", 5)

print(d2.get_name())
print(d.get_age())
d.set_age(20)
d2.set_name("Albert")
print(d.get_age())
print(d2.get_name())