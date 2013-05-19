#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Copyright(C) 2013 mutse<yyhoo2.young@gmail.com>
#
# This program is visitor demo of the Design Pattern Gossip Series.
#

class Action:
    def getManConclusion(self):
        return

    def getWomanConclusion(self):
        return

class Success(Action):
    def getManConclusion(self):
        print '男人成功时，背后多半有一个伟大的女人。'

    def getWomanConclusion(self):
        print '女人成功时，背后多半有一个不成功的男人。'

class Failing(Action):
    def getManConclusion(self):
        print '男人失败时，闷头喝酒，谁也不用劝。'

    def getWomanConclusion(self):
        print '女人失败时，眼泪汪汪，谁也劝不了。'

class Amativeness(Action):
    def getManConclusion(self):
        print '男人恋爱时，凡事不懂也要装懂。'

    def getWomanConclusion(self):
        print '女人恋爱时，遇事懂也装不懂。'

class Marriage(Action):
    def getManConclusion(self):
        print '男人结婚时，感慨道：恋爱游戏结束时，有妻徒刑遥无期。'

    def getWomanConclusion(self):
        print '女人结婚时，欣慰曰：爱情长跑路漫漫，婚姻保险保平安。'

class Person:
    def accept(self, visitor):
        return

class Man(Person):
    def accept(self, visitor):
        visitor.getManConclusion()

class Woman(Person):
    def accept(self, visitor):
        visitor.getWomanConclusion()

class Content:
    def __init__(self):
        self.perlist = []

    def attach(self, element):
        self.perlist.insert(0, element)

    def display(self, visitor):
        self.perlist[0].accept(visitor)
        self.perlist[-1].accept(visitor)

if __name__ == "__main__":
    content = Content()
    man = Man()
    woman = Woman()

    content.attach(man)
    content.attach(woman)

    v1 = Success()
    content.display(v1)

    v2 = Failing()
    content.display(v2)

    v3 = Amativeness()
    content.display(v3)

    v4 = Marriage()
    content.display(v4)

