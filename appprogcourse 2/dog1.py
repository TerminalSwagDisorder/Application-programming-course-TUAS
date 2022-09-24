class Dog:
    """A simple attempt to model a dog."""  
  
    def __init__(self, name, age, race):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.race = race
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
    
    def bark(self):
        print(self.name, "barked")

my_dog = Dog('Willie', 6, "doberman")
your_dog = Dog('Lucy', 3, "labrador")

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print("My dog is a", my_dog.race)
my_dog.sit()
my_dog.bark()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
print("Your dog is a", your_dog.race)
your_dog.sit()
your_dog.bark()
