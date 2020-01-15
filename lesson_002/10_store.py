#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
################# ЛАМПЫ ##################################
lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
print('Лампа -',store[goods['Лампа']][0]['quantity'],'шт, общей стоимостью',lamps_cost , 'руб')
################# СТОЛЫ ##################################
tables_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
print('Столы -',store[goods['Стол']][0]['quantity'],'шт, общей стоимостью',tables_cost , 'руб')
################# ДИВАНЫ ##################################
sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
print('Диваны -',store[goods['Диван']][0]['quantity'],'шт, общей стоимостью',sofa_cost , 'руб')
################# СТУЛЬЯ ##################################
chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
print('Стулья -',store[goods['Стул']][0]['quantity'],'шт, общей стоимостью',chair_cost , 'руб')







