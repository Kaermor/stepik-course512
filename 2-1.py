# Задача на проверку исключений об ошибках
def Prov(err, dl):
    if dl > 0:
        for i in range(dl-1, -1, -1):
            if err in d.keys() and len(d[err]) != 0:
                if lster[i] in d[err]:
                    return err
                # if d[err][0] == lster[i]:
                #     return err
                elif lster[i] not in d[err]:
                    for j in d[err]:
                        if Prov(j, dl) is not None:
                            return err


d = {}
lst = []
lster = []
n = int(input())
for i in range(n):
    lst = input().split(sep = ' : ')
    if len(lst) == 1:
        d[lst[0]] = []
        # print(d)
    else:
        d[lst[0]] = lst[1].split()
        # print(d)
m = int(input())
for i in range(m):
    err = input()
    dl = len(lster)
    if Prov(err, dl) is not None:
        print(Prov(err, dl))
    lster.append(err)


# Задача на написание класса и функции. Лист положительных чисел. Исключение об ошибке неположительного числа.
# class NonPositiveError(Exception):
#     pass
#
#
# class PositiveList(list):
#     def append(self, x):
#         if x > 0:
#             return super(PositiveList, self).append(x)
#         else:
#             raise NonPositiveError