#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2013 mutse <yyhoo2.young@gmail.com>
#
# This program is a proxy demo of the Design Pattern Gossip Series.
#

class SchoolGirl:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class AbstractProxy:
    def giveDolls(self):
        return

    def giveFlowers(self):
        return

    def giveChocolate(self):
        return

class Pursuit(AbstractProxy):
    def __init__(self, mm):
        super(Pursuit).__init__(self)
        self.mm = mm

    def giveDolls(self):
        print 'Give the dolls to %s' % (self.mm.getName())

    def giveFlowers(self):
        print 'Give some flowers to %s' % (self.mm.getName())

    def giveChocolate(self):
        print 'Give some chocolate to %s' % (self.mm.getName())

class Proxy(AbstractProxy):
    def __init__(self, mm):
        super(Proxy).__init__(self)
        self.gg = Pursuit(mm)

    def giveDolls(self):
        self.gg.giveDolls()

    def giveFlowers(self):
        self.gg.giveFlowers()

    def giveChocolate(self):
        self.gg.giveChocolate()

if __name__ == "__main__":
    mm = SchoolGirl("Mary")
    proxy = Proxy(mm)
    proxy.giveDolls()
    proxy.giveFlowers()
    proxy.giveChocolate()

