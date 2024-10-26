class Dog:

    def __init__(self):
        pass
    
    def bark(self):
        print("I generally bark because I am a general dog.")

    def eat(self):
        print("I generrally eat because I am a general dog.")

    def run(self):
        print("I generally run because I am a general dog.")


class Bulldog(Dog):

    def bark(self):
        super().bark()
        print("Woof woof, You are dead hooman. Woof!!!")

    def eat(self):
        super().eat()
        print("I also eat as a bulldog because I actually am a bulldog")

    def run(self):
        super().run()
        print("I also run as a bulldog because I actually am a bulldog")
        
d = Dog()
d.bark()
d.eat()
print("_"*50)
b = Bulldog()
b.bark()
b.eat()
b.run()