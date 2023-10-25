class Person:
    amount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.amount += 1
        # self.weight = weight
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'
    def introduceSelf(self):
        print(f'My name is {self.name} and I am {self.age} years old.')
    #THIS OBJECT DELETES AN AMOUNT OF INSTANCES YOU WANT TO DELETE AND RETURN THE REMAINDER
    def __del__(self):
        Person.amount -= 1
        
person1 = Person('Dave', 30)
person2 = Person('Dive', 34)
person3 = Person('ive', 14)
print(person1)
person1.introduceSelf()
#PRINTS THE OUTPUT OF __del__(self)
del person3, person1
print(Person.amount)
