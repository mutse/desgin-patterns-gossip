#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   mutse
#   E-mail  :   yyhoo2.young@gmail.com
#   Date    :   14/04/19 19:53:10
#   Desc    :   
#

class Mediator(object):
    def send(self, msg, colleague):
        pass

class Colleague(object):
    def __init__(self, mediator):
        self.mediator = mediator

class ConcreteMediator(Mediator):
    def __init__(self):
        Mediator.__init__(self)

        self.colleague1 = None
        self.colleague2 = None

    def set_colleague1(self, value):
        self.colleague1 = value

    def set_colleague2(self, value):
        self.colleague2 = value

    def send(self, msg, colleague):
        if colleague is self.colleague1:
            self.colleague2.notify(msg)
        else:
            self.colleague1.notify(msg)

class ConcreteColleague1(Colleague):
    def __init__(self, mediator):
        Colleague.__init__(self, mediator)

    def send(self, msg):
        self.mediator.send(msg, self)

    def notify(self, msg):
        print 'Colleague1 receives the message: %s' % msg

class ConcreteColleague2(Colleague):
    def __init__(self, mediator):
        Colleague.__init__(self, mediator)

    def send(self, msg):
        self.mediator.send(msg, self)

    def notify(self, msg):
        print 'Colleague2 receives the message: %s' % msg

if __name__ == "__main__":
    mediator = ConcreteMediator()

    c1 = ConcreteColleague1(mediator)
    c2 = ConcreteColleague2(mediator)

    mediator.set_colleague1(c1)
    mediator.set_colleague2(c2)

    c1.send('Hello, I am Colleague1.')
    c2.send('Hello, I am Colleague2.')

