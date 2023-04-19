class person: #parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

class Employee(person):
    def __init__(self, name, age,salary,post):
        self.salary = salary
        self.post = post
        super().__init__(name,age)

        person.__init__(self,name,age)


    def display(self):
        super().display()
        print(self.salary)
        print(self.post)
 

#creare object        
e = Employee("ram",22,42000,"manager")
p = Employee("sham",26,45000,"ceo")

e.display()
p.display()