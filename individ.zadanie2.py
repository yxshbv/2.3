# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
# import inf
from inf import table, table_name, table_name_fil

list_shop = []
spisok_new = []

while True:
    command = input('>>> ').lower()

    if command == 'exit':
        break

    elif command == 'add':
        name_shop = input('Название магазина: ')
        name_product = input('Название товара: ')
        prise = input('Стоимость товара: ')

        list_shop_new = {
            'name_shop': name_shop,
            'name_product': name_product,
            'prise': prise
        }

        list_shop.append(list_shop_new)

        if len(list_shop) > 1:
            list_shop.sort(key=lambda item: item.get('name_shop', ''))

    elif command == 'list':
        print(table())
        print(table_name())
        print(table())
        for item_n in table_name_fil(list_shop):
            print(item_n)
        print(table())

    elif command == 'product':
        shop_sear = input('Введите название товара: ')
        search_shop = []
        for shop_sear_itme in list_shop:
            if shop_sear == shop_sear_itme['name_product']:
                search_shop.append(shop_sear_itme)

        if len(search_shop) > 0:
            print(table())
            print(table_name())
            print(table())
            for item_f in table_name_fil(search_shop):
                print(item_f)
            print(table())
        else:
            print('Такого товара не найдено', file=sys.stderr)

    elif command == 'help':
        print('Список команд:\n')
        print('add - добавить магазин.')
        print('list - вывести список магазинов.')
        print('product <Название> - запросить информацию о товаре.')
        print('help - Справочник.')
        print('exit - Завершить пработу программы.')
    else:
        print(f'Команда <{command}> не существует.', file=sys.stderr)
        print('Введите <help> для просмотра доступных команд')