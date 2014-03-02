#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   mutse
#   E-mail  :   yyhoo2.young@gmail.com
#   Date    :   13/12/26 14:18:03
#   Desc    :   Singleton Pattern
#

class Singleton(object):
    instance = None
    def __init__(self):
        pass

    def getInstance(self):
        if Singleton.instance is None:
            Singleton.instance = Singleton()

        return Singleton.instance

if __name__ == "__main__":
    s1 = Singleton().getInstance()
    s2 = Singleton().getInstance()

    if s1 is s2:
        print "the two objects are the same instance"

    print "Done"
