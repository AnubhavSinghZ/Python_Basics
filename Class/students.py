class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    print("Adding Students and his marks")
s1= Student("Karan", 99)
s2= Student("Arjun", 100)
print(f"{s1.name} and his marks is {s1.marks}")
print(f"{s2.name} and his marks is {s2.marks}")
del s1.name  # this will delete the s1 name 
print(s1)  

#print(s1.name,s1.marks) Karan,99
#print(s2.name,s2.marks)  Arjun,100
# We can use this type to show the output directly