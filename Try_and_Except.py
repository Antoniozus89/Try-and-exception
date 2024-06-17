try:
        def add_everithing_up(a, b):
                c = a + b
                print(c)
        add_everithing_up(3.14, "P")
except TypeError as exc:
        print(f'нельзя складывать пременные разных типов  ', exc)

try:
        def  add_everithing_up(a, b):
                c = a + b
                print(c)
        add_everithing_up(123, 'строка')
except TypeError as exc:
        print(f'нельзя складывать пременные разных типов  ', exc)
else:
        print('А вот теперь все получилось')
try:
        def  add_everithing_up(a, b):
                c = a + b
                print(c)
        add_everithing_up(123.4, 7)
except TypeError as exc:
        print(f'нельзя складывать пременные разных типов  ', exc)
else:
        print('А вот теперь все получилось')
finally:
        print('заканчиваю домашнее задание')