class Dog:

    #class attribute
    species = "mammal"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} year(s) old"
    
    def speak(self, sound):
        return f'{self.name} says {sound}'


class RusselTerrier(Dog):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.breed = 'Russel Terrier'
    
    def run(self,speed):
        return f'{self.name} runs {speed}'


class BullDog(Dog):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.breed = 'BullDog'
    
    def run(self,speed):
        return f'{self.name} runs {speed}'




# philo = Dog('Philo',5)
# mikey = Dog('mikey',6)
# joey = Dog('Joey',10)

# print(f'{philo.name} is {philo.age} year(s) old')
# print(f'{mikey.name} is {mikey.age} year(s) old')

# print(mikey.description())
# print(mikey.speak('Woof Woof!'))

jim = BullDog('Jim',12)
print(jim.description())

print(jim.run('slowly'))