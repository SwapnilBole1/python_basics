# Simple Inheritance
"""
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


# Multilevel Inheritance
# more than two classes are used in implementation of inheritance

class Central:
    def funds(self):
        print('fund of central')
class State(Central):
    def funds(self):
        print('fund of state')
        super().funds()
class Local(State):
    def funds(self):
        print('fund of local')
        super().funds()
l = Local()
l.funds()


# Multiple Inheritance
# when we have more than one parent and one child class
class Father:
    def money(self):
        print('money of father')
class Mother:
    def money(self):
        print('money of mother')
class Child(Mother, Father):
    def money(self):
        print('money of child')
        super().money()

c = Child()
c.money()


# Hierarchical Inheritance
# it contains more than one derived class from single base class

class Parent:
    def car(self):
        print('car of parent')
class Child1:
    def bike1(self):
        print('bike of child 1')
class Child2:
    def bike2(self):
        print('bike of child 2')

c1 = Child1()
c2 = Child2()
c1.bike1()
c2.bike2()

"""