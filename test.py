from MultiInstanceModules import MultiInstance

class A:
    def __init__(self):
        self.f = 1
        self.s = 2

    def first(self):
        print("I'm A")

class B:
    def __init__(self):
        self.t = 3
        self.f = 4
        self.fif = 5
    
    def second(self):
        print("i'm B")

a=A()
b=B()

c=MultiInstance.SetMultiInstanceByTwoObject(a, b)

print(c.fif)
c.first()
c.second()