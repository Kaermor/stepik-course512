# class A:
#     def __init__(self, val=0):
#         self.val = val
#
#     def add(self, x):
#         self.val += x
#
#     def print_val(self):
#         print(self.val)
#
#
# a = A()
# b = A(2)
# c = A(4)
# a.add(2)
# b.add(2)
#
# a.print_val()
# b.print_val()
# c.print_val()


# class MoneyBox:
#     def __init__(self, capacity):
#         # конструктор с аргументом – вместимость копилки
#         self.capacity = capacity
#         self.val = 0
#
#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#         if (self.val + v) <= self.capacity:
#             return True
#         else:
#             return False
#
#     def add(self, v):
#         # положить v монет в копилку
#         if self.can_add() is True:
#             self.val += v
#         else:
#             False


# class Buffer:
#     def __init__(self):
#         # конструктор без аргументов
#         self.lst = []
#         self.sum = 0
#
#     def add(self, *a):
#         # добавить следующую часть последовательности
#         for i in range(len(a)):
#             self.lst.append(a[i])
#         i = 1
#         llst = ((len(self.lst) // 5) * 5)
#         while i <= llst:
#             self.sum += self.lst.pop(0)
#             if i % 5 == 0:
#                 print(self.sum)
#                 self.sum = 0
#             i += 1
#     def get_current_part(self):
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
#         # добавлены
#         print(self.lst)
#         return self.lst
#
#
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]

# lst = []
# lst = input().split()
# print(lst)

# Попытка на работе
# def proverka(parent, child):
#     if child in d.keys():
#         if parent in d[child]:
#             return 'Yes'
#         else:
#             for i in range(len(d[child])):
#
#
# lst = []
# # lstr = []
# d = {}
# n = int(input())
# for i in range(n):
#     lstr = input().split(sep=" : ")
#     if len(lstr) == 1:
#         d[lstr[0]] = 'Object'
#     else:
#         d[lstr[0]] = lstr[1].split()
#     # print(lstr)
#     # print(len(lstr))
# print(d)
# q = int(input())
# for i in range(q):
#     parent, child = input().split()
#     if child in d.keys():
#         if


# Попытка из дома
def proverka(parent, child):
    if child not in d.keys():
        return 'No'
    elif child == parent:
        return 'Yes'
    elif child in d.keys() and len(d[child]) == 0:
        return 'No'
    elif child in d.keys() and parent in d[child]:
        return 'Yes'
    elif child in d.keys() and parent not in d[child]:
        r = len(d[child])
        lansw = []
        for i in range(r):
            #parent = child
            childN = d[child][i]
            lansw.append(proverka(parent, childN))
            # print(lansw)
        if 'Yes' in lansw:
            return 'Yes'
        else:
            return 'No'


d = {}
lst = []
lstr = []
n = int(input())
for i in range(n):
    lst = input().split(sep = ' : ')
    if len(lst) == 1:
        d[lst[0]] = []
        #print(d)
    else:
        #lstr = []
        #lstr = lst[1].split()
        d[lst[0]] = lst[1].split()
        #print(d)
q = int(input())
for i in range(q):
    parent, child = input().split()
    print(proverka(parent, child))


# Создание классов для проверки классов :)


# def clascreate(a, b):
#     class a(b):
#         pass
#
#
# d = {}
# lst = []
# lstr = []
# n = int(input())
# for i in range(n):
#     lst = input().split(sep = ' : ')
#     if len(lst) == 1:
#         class lst[0]:
#             pass
#         #print(d)
#     else:
#         #lstr = []
#         #lstr = lst[1].split()
#         clascreate(lst[0], lst[1])
#         #print(d)


# Расширенный стек
# class ExtendedStack(list):
#
#     def sum(self):
#         top1 = self.pop()
#         top2 = self.pop()
#         return self.append(top1 + top2)
#
#     def sub(self):
#         # операция вычитания
#         top1 = self.pop()
#         top2 = self.pop()
#         return self.append(top1 - top2)
#     def mul(self):
#         # операция умножения
#         top1 = self.pop()
#         top2 = self.pop()
#         return self.append(top1 * top2)
#     def div(self):
#         # операция целочисленного деления
#         top1 = self.pop()
#         top2 = self.pop()
#         return self.append(top1 // top2)


