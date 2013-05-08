#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2013 mutse <yyhoo2.young@gmail.com>
#
# This program is a strategy demo of the Design Pattern Gossip Series.
#

"""
definition of CashSuper
"""
class CashSuper:
    def acceptCash(self, money):
        return

class CashNormal(CashSuper):
    def acceptCash(self, money):
        return money

class CashRebate(CashSuper):
    def __init__(self, rebate):
        self.rebate = rebate

    def acceptCash(self, money):
        return self.rebate * money

class CashReturn(CashSuper):
    def __init__(self, condition, moneyReturn):
        self.condition = condition
        self.moneyReturn = moneyReturn

    def acceptCash(self, money):
        result = money
        if money >= self.condition:
            result = money - (money /self.condition) * self.moneyReturn

        return result

class CashContext:
    def __init__(self, type):
        if type == "Normal":
            cs0 = CashNormal()
            self.cs = cs0
        elif type == "Return":
            cr1 = CashReturn(300, 100)
            self.cs = cr1
        elif type == "Rebate":
            cr2 = CashRebate(0.8)
            self.cs = cr2
        else:
            print "error type"

    def GetResult(self, money):
        return self.cs.acceptCash(money)

if __name__ == "__main__":
    cash = CashContext("Return")
    print '[Return Strategy] The result cash is %s' % (cash.GetResult(400))

    cash = CashContext("Normal")
    print '[Normal Strategy] The result cash is %s' % (cash.GetResult(400))

    cash = CashContext("Rebate")
    print '[Rebate Strategy] The result cash is %s' % (cash.GetResult(400))

