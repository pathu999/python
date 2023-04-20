# polymorphism contains two words "poly"and "morph" poly means meany and morph means shape(forms)
# by understand that one task can perform in different ways we have a class animal and all animal speak
#abiliy to take various forms
class Tommato:
    def type(self):
        print("vagitable")

    def color(self):
        print("red")

    def func(self,obj):
        obj.type()
        obj.color()


class Apple:
    def type(self):
        print("fruit")

    def color(self):
        print("red")

    def func(obj):
        obj.type()
        obj.color()

    obj_tommato = Tommato()
    
    obj_apple = Apple()


    obj_tommato.type()
    obj_tommato.color()

    # obj_apple.type()
    # obj_apple.color()

    obj_tommato.func()
    


"""obj_tommato.type() 
obj_tommato.color()

obj_apple.type() 
obj_apple.color()

obj_apple.func(obj_tommato)
obj_apple.func(obj_apple)"""
