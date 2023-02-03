# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def delchis(list1):
    def delchetnechet():
        type = input('Введите even или noteven:\n')
        if type == 'even':
            for x in range(len(list1)):
                if x % 2 == 0:
                    list1.pop(list1.index(x))
                    print(list1)
        elif type == 'noteven':
            for x in range(len(list1)):
                if x % 2 != 0:
                    list1.pop(list1.index(x))
                    print(list1)
        else:
            print('Введена не правильная команда')

    return delchetnechet