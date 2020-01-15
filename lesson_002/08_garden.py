#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
all_flower = garden+meadow
flower_all_set = set(all_flower)
print('Все виды цветов',flower_all_set)

# выведите на консоль те, которые растут и там и там
all_flower_set = garden_set | meadow_set
print('Растут везде',all_flower_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
only_garden = garden_set - meadow_set
print('Растут только в саду',only_garden)

# выведите на консоль те, которые растут на лугу, но не растут в саду
only_meadow = meadow_set - garden_set
print('Растут только на лугу',only_meadow)


