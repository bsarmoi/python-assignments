class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    print(f"Hello! My name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person("Bethuel Sarmoi", 30, "Male")

# Call the introduce method on the instance
person1.introduce()
