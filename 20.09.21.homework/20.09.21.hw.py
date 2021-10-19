class Summator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def return_sum(self):
        return self.a + self.b
s = Summator(1,3)
print(s.return_sum())

#2
class Car():
    def __init__(self):
        pass
    def what_is_this(self):
        print('I am a car')
class Pink_car(Car):
    def what_color(self):
        print('Pink')

pink_car = Pink_car()
pink_car.what_is_this()
pink_car.what_color()

#3
class Person():
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print('Удалили объект', self)
    def exclaim(self):
        print('я человек с именем', self.name)
class Student(Person):
    def exclaim(self):
        print('я челвоек с именем ', self.name,'но я хочу спать больше')

p = Person('Vanya')
s = Student('Vanya')
p.exclaim()
s.exclaim()
p.__del__()
s.__del__()
a = '4'
print(isinstance(p, Person))
print(issubclass(Student,Person))
print(isinstance(a, str))
