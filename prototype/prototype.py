#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Copyright (C) 2013 mutse <yyhoo2.young@gmail.com>
#
#   Author  :   mutse
#   E-mail  :   yyhoo2.young@gmail.com
#   Date    :   13/06/07 22:17:25
#   Desc    :   This program is a prototype demo of the Design Pattern Gossip Series
#

import copy

class WorkExperience(object):

    workDate = ""   # work date
    company = ""    # company name

    def getWorkDate(self):
        return self.workDate

    def setWorkDate(self, value):
        self.workDate = value

    def getCompany(self):
        return self.company

    def setCompany(self, value):
        self.company = value

    def clone(self):
        return copy.deepcopy(self)

class Resume(object):
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
            self.work = WorkExperience()
        elif isinstance(name, WorkExperience):
            self.work = copy.deepcopy(name)

        self.sex = ""
        self.age = ""

    def setPersonalInfo(self, sex, age):
        self.sex = sex
        self.age = age

    def setWorkExperience(self, workDate, company):
        self.work.setWorkDate(workDate)
        self.work.setCompany(company)

    def display(self):
        print "%s %s %s" % (self.name, self.sex, self.age)
        print "Work Experience: %s %s" % (self.work.getWorkDate(), self.work.getCompany())

    def clone(self):
        resume = Resume(self.work)
        resume.name = self.name
        resume.sex = self.sex
        resume.age = self.age
        return resume

if __name__ == "__main__":
    man = Resume("VBird")
    man.setPersonalInfo("male", "29")
    man.setWorkExperience("1998-2000", "Company A")

    b = man.clone()
    b.setWorkExperience("2000-2003", "Company B")

    c = man.clone()
    c.setWorkExperience("2003-2012", "Company C")

    man.display()
    b.display()
    c.display()



