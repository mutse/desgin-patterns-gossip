#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   mutse
#   E-mail  :   yyhoo2.young@gmail.com
#   Date    :   14/02/27 11:13:34
#   Desc    :   Bridge Pattern
#

class Implementor(object):
    """
    operation
    """
    def operation(self):
        pass

class ConcreteImplementorA(Implementor):
    """
    override function
    """
    def operation(self):
        print "The method of ImplementorA is running"

class ConcreteImplementorB(Implementor):
    """
    override function
    """
    def operation(self):
        print "The method of ImplementorB is running"

class Abstraction(object):

    def __init__(self):
        self.implementor = None

    def setImplementor(self, implementor):
        self.implementor = implementor

    def operation(self):
        self.implementor.operation()

class RefinedAbstraction(Abstraction):

    def __init__(self):
        Abstraction.__init__(self)

    def operation(self):
        self.implementor.operation()

if __name__ == "__main__":
    ab = RefinedAbstraction()

    ab.setImplementor(ConcreteImplementorA())
    ab.operation()

    ab.setImplementor(ConcreteImplementorB())
    ab.operation()
