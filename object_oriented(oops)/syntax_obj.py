class Employee :  #create class employee
    def __init__(self,name,salary):
        self . name = name
        self . salary  = salary

    def getsalary(self):
        print(self.salary)

rohan=Employee("Rohan",89000)

print(rohan.salary)
print(rohan.name)
        