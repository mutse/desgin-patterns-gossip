#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2013 mutse<yyhoo2.young@gmail.com>
#
# This is a demo of composite pattern of the Design Pattern Gossip Series. 
#

class Company(object):
    def __init__(self, name):
        self.name = name

    def add(self, company):
        return

    def remove(self, company):
        return

    def display(self, depth):
        return

    def duty(self):
        return

class HRDepartment(Company):
    '''
    Human Resource Department
    '''
    def __init__(self, name):
        super(HRDepartment, self).__init__(name)

    def add(self, company):
        print

    def remove(self, company):
        print

    def display(self, depth):
        print "-" * depth + self.name

    def duty(self):
        print '%s 员工招聘培训管理' % (self.name)

class FinanceDepartment(Company):
    '''
    Finance Department
    '''
    def __init__(self, name):
        super(FinanceDepartment, self).__init__(name)

    def add(self, company):
        print

    def remove(self, company):
        print

    def display(self, depth):
        print "-" * depth + self.name

    def duty(self):
        print '%s 公司财务收支管理' % (self.name)

class ConcreteCompany(Company):
    def __init__(self, name):
        super(ConcreteCompany, self).__init__(name)
        self.children = []

    def add(self, company):
        self.children.append(company)

    def remove(self, company):
        self.children.remove(company)

    def display(self, depth):
        print "-" * depth + self.name

        for component in self.children:
            component.display(depth + 2)

    def duty(self):
        for component in self.children:
            component.duty()

if __name__ == "__main__":
    root = ConcreteCompany("北京总公司")
    root.add(HRDepartment("总公司人力资源部"))
    root.add(FinanceDepartment("总公司财务部"))

    comp = ConcreteCompany("上海华东分公司")
    comp.add(HRDepartment("华东分公司人力资源部"))
    comp.add(FinanceDepartment("华东分公司财务部"))
    root.add(comp)

    comp1 = ConcreteCompany("南京办事处")
    comp1.add(HRDepartment("南京办事处人力资源部"))
    comp1.add(FinanceDepartment("南京办事处财务部"))
    comp.add(comp1)

    comp2 = ConcreteCompany("杭州办事处")
    comp2.add(HRDepartment("杭州办事处人力资源部"))
    comp2.add(FinanceDepartment("杭州办事处财务部"))
    comp.add(comp2)

    print '结构图： '
    root.display(1)

    print '职责：'
    root.duty()

