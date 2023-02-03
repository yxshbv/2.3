# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def table_name_fil(names):
    post = []
    for idx_new, spisok_new_new in enumerate(names, 1):
        post.append(
            '| {:>8} | {:<30} | {:<45} | {:<30} | '.format(
                idx_new,
                spisok_new_new.get('name_shop', ''),
                spisok_new_new.get('name_product', ''),
                spisok_new_new.get('prise', '')
            )
        )
    return post