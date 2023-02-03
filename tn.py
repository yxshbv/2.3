# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def table_name():
    post = '| {:^8} | {:^30} | {:^45} | {:^30} | '.format(
        "№",
        "Название магазина",
        "Название товара",
        "Стоимость"
    )
    return post