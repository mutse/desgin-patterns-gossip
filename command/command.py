#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2013 mutse <yyhoo2.young@gmail.com>
#
# This program is a command demo of the Design Pattern Gossip Series.
#

import time

class Command:
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        return

class BakeMuttonCommand(Command):
    def __init__(self, receiver):
        Command.__init__(self, receiver)

    def execute(self):
        self.receiver.bakeMutton()

class BakeChickenWingCommand(Command):
    def __init__(self, receiver):
        Command.__init__(self, receiver)

    def execute(self):
        self.receiver.bakeChickenWing()


class Waiter:
    def __init__(self):
        self.orders = []

    def setOrder(self, command):
        if command.__class__.__name__ == 'BakeChickenWingCommand':
            print '服务员：鸡翅没有了，请点别的烧烤。'
        else:
            self.orders.append(command)
            print '增加订单：%s 时间：%s' % (command.__class__.__name__, time.strftime("%Y-%m-%d %A %X", time.localtime()))

    def cancelOrder(self, command):
        self.orders.remove(command)
        print '取消订单： %s 时间: %s' % (commandcommand.__class__.__name__, time.strftime("%Y-%m-%d %A %X", time.localtime()))

    def notify(self):
        for cmd in self.orders:
            cmd.execute()

class Barbecuer:
    def bakeMutton(self):
        print '烤羊肉串！'

    def bakeChickenWing(self):
        print '烤鸡翅！'

if __name__ == "__main__":
    b = Barbecuer()
    c1 = BakeMuttonCommand(b)
    c2 = BakeMuttonCommand(b)
    c3 = BakeChickenWingCommand(b)
    w = Waiter()

    w.setOrder(c1)
    w.setOrder(c2)
    w.setOrder(c3)

    w.notify()

