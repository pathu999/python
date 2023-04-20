#Encaptulation is also an essential accept of object oriented programming.it is used to restrict access method and variable
#in encaptulation code and data are wrapped in single unit from being modify by accident
class MyClass:
    def __init__(self):
        self._protected_attr = 20
        
    def _protected_method(self):
        print("This is a protected method.")
        
class MySubClass(MyClass):
    def __init__(self):
        super().__init__()
        self._protected_attr += 5
        
    def call_protected_method(self):
        self._protected_method()
        
my_obj = MySubClass()
print(my_obj._protected_attr)        # 25
my_obj.call_protected_method()       # "This is a protected method."

