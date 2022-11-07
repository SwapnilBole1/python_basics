# Inheritance
class Parent:
    def bike(self):
        print('bike of parent')

    def car(self):
        print('car of parent')


class Child(Parent):
    def bike(self):
        print('bike of child')
        super().bike()

    def pocketmoney(self):
        print('Pocket money of child')
c = Child()
c.bike()

