  def __init__(self, n, a, w):
    self.name = n
    self.age = a
    self.weight = w
        
  def display(self):
    print(f"{self.name} is {self.age} years old and weighs {self.weight}kg.")
   #alexandra = Person("Alexandra", 23, 80)
   #alexandra.display()
   #print(alexandra.age)
class Doctor(Person): #child/subclass
  
  def hospital(self):
    print("The doctor goes to hospital 6 days of the week.")

d = Doctor("Dr Jones", 56, 65)
print(d.age)
d.display()
d.hospital()

class Lecturer(Person):
  speciality = "Computer Science"
  yearsOfExperience = 8
  university = "Solent"
  
  def lecture(self):
    print("The lecturer delivers lectures.")
  
l = Lecturer("James", 42, 70)
l.lecture()
l.display()
print(l.university)

class GP(Doctor):
  numberOfRegisteredPatients = 500

  def colleague(self):
    print("10 people work under GP.")

gp = GP("Ahmed", 50, 76)
print(gp.numberOfRegisteredPatients)
gp.colleague()
gp.hospital()
gp.display()
print(gp.name)