#1
class Girls:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is:",self.name)
        print("age is:",self.age)
p1=Girls("Pooja",20)
p2=Girls("Mathumitha",22)
p1.display()
p2.display()

#2
class Players:
    def __init__(self,name,score,games):
        self.name=name
        self.score=score
        self.games=games
    def display(self):
        print("NAME:",self.name)
        print("SCORE:",self.score)
        print("GAMES:",self.games)
a1=Players("pooja",100,5)
a2=Players("priya",99,5)
a3=Players("nila",95,5)
a4=Players("sowmiya",91,5)
a5=Players("sona",90,5)
a1.display()
a2.display()
a3.display()
a4.display()
a5.display()

#3
class Person:
    def __init__(self,name):
        self.name = name
    def sayhello(self):
        print("hello,my name is:",self.name)
    def __del__(self):
        print("how r u",self.name)
A=Person('yang li')
A.sayhello()

#4
class Girls:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is:",self.name)
        print("age is:",self.age)
    def __del__(self):
        print("hey girls",self.name,self.age)
p1=Girls("Pooja",20)
p2=Girls("Mathumitha",22)
p1.display()
p2.display()






