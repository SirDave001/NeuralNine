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
        
    def __del__(self):
        Person.amount -= 1
        
class Worker(Person):
    def __init__(self, name, age, salary):
        super(Worker, self).__init__(name, age)
        self.salary = salary
    def __str__(self):
        txt = super(Worker, self).__str__()
        txt += f', Salary: {self.salary}'
        return txt
    def calc_annual_salary(self):
        return self.salary * 12
        
worker1 = Worker('Cha', 39, 54000)
person = Person('Bad', 23)
print(person)
person.introduceSelf()
print(f'My name is {worker1.name}, I am {worker1.age} years and I earn {worker1.salary} monthly.')
print(worker1.calc_annual_salary())

# OPERATOR OVERLOADING
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'
    
v1 = Vector(2, 3)
v2 = Vector(3, 5)

print(v1)
print(v2)

v3 = v1 -v2
print(v3)