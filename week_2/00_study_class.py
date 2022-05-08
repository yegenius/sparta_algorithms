class Person:
    def __init__(self, param_name):
        self.name=param_name
        print("hihihi")
    def talk(self):
        print("hi my name is", self.name)

person_1= Person("Yoo J.S")
print(person_1.name)
person_1.talk()
person_2=Person("Park M.S")
print(person_2.name)
person_2.talk()
