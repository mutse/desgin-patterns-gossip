#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2013 mutse <yyhoo2.young@gmail.com>
# This program is a observer demo of the Design Pattern Gossip Series.
#

class Subject(object):
    observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for o in self.observers:
            o.update()

class Observer(object):
    def update(self):
        return

class ConcreteSubject(Subject):
    state = ''
    def getState(self):
        return self.state

    def setState(self, value):
        self.state = value

class ConcreteObserver(Observer):
    def __init__(self, subject, name):
        self.subject = subject
        self.name = name
        self.observerState = ''

    def update(self):
        self.observerState = self.subject.getState()
        print 'Observer %s new state is %s' % (self.name, self.observerState)

    def getSubject(self):
        return self.subject

    def setSubject(self, value):
        self.subject = value

if __name__ == "__main__":
    s = ConcreteSubject()

    c1 = ConcreteObserver(s, "X")
    c2 = ConcreteObserver(s, "Y")
    c3 = ConcreteObserver(s, "Z")

    s.attach(c1)
    s.attach(c2)
    s.attach(c3)
    s.detach(c2)

    s.setState("ABC")
    s.notify()

