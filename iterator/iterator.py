#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   mutse
#   E-mail  :   yyhoo2.young@gmail.com
#   Date    :   14/04/13 17:08:15
#   Desc    :   
#

# abstract Iterator
class Iterator(object):
    def first(self):
        pass

    def next(self):
        pass

    def is_done(self):
        pass

    def current_item(self):
        pass

class Aggregate(object):
    def create_iterator(self):
        pass

class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        Iterator.__init__(self)

        self.current = 0
        self.aggregate = aggregate

    def first(self):
        return self.aggregate[0];

    def next(self):
        ret = None
        self.current += 1
        if self.current < self.aggregate.count():
            ret = self.aggregate[self.current]

        return ret

    def is_done(self):
        flag = False
        if self.current >= self.aggregate.count():
            flag = True

        return flag

    def current_item(self):
        return self.aggregate[self.current]

class ConcreteAggregate(Aggregate):

    def __init__(self):
        Aggregate.__init__(self)

        self.items = []

    def create_iterator(self):
        return ConcreteIterator()

    def count(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items.insert(index, value)

if __name__ == "__main__":
    agg = ConcreteAggregate()

    agg[0] = "Genius" # 大鸟
    agg[1] = "Newbie" # 小菜
    agg[2] = "Baggage" # 行李
    agg[3] = "Foreigner" # 老外
    agg[4] = "Internal Employee" # 内部员工
    agg[5] = "Thief" # 小偷

    it = ConcreteIterator(agg)
    item = it.first()
    while not it.is_done():
        print "%s, please buy the ticket!" % it.current_item()
        it.next()


