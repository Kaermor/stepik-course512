d = {'global': ['ab', 'ac', 'ad'], 'local': ['la', 'lb', 'lc']}
# if 'acs' in d['global']:
#     print('Yes')
d['global'].insert(1, 'ab2')
print(d)
# print(d.values())
# print(d['global'])
# print(d['local'])



# Вариант 1 Словари только
# vvod = []
# d = {}
# n = int(input())
# for i in range(n):
#     vvod = input().split()
#     if vvod[0] == 'add':
#         if vvod[1] in d.keys():
#             d[vvod[1]].append(vvod[2])
#         else:
#             d[vvod[1]] = [vvod[2]]
#     if vvod[0] == 'create':
#         if vvod[2] in d.keys():
#             d[vvod[2]].append(vvod[1])
#             # d[vvod[1]]=['']
#         else:
#             d[vvod[2]] = [vvod[1]]
#     if vvod[0] == 'get':
#         if vvod[2] in d[vvod[1]]:
#             print(vvod[1])
#         else:
#             nsp1 = vvod[1]
#             # k1 = k
#             # while k != 'global':
#             for k in d.keys():
#                 if nsp1 in d[k]:
#                     if vvod[2] in d[k]:
#                         print(k)
#                     else:
#                         nsp1 = k
#                 # k = k1
#                 # if vvod[2] in d['global']:
#                 #     print('global')
#                 # else:
#                 #     print('None')
#
#
# print(d)

# Вариант 2 - Два списка: всё и пространства
# vvod = []
# listt = []
# lst_nmsp = []
# n = int(input())
# for i in range(n):
#     vvod = input().split()
#     if vvod[0] == 'add':
#         if vvod[1] in listt:
#             listt.append(vvod[2])
#         else:
#             listt.append(vvod[1])
#             listt.append(vvod[2])
#             lst_nmsp.append(vvod[1])
#     if vvod[0] == 'create':
#             listt.append(vvod[1])
#             lst_nmsp.append(vvod[1])
#     # print(len(listt))
#     if vvod[0] == 'get':
#         if vvod[2] not in listt:
#             print('None')
#         for j in range(len(listt)-1, -1, -1):
#             if vvod[2] == listt[j]:
#                 for j1 in range(j-1, -1, -1):
#                     if listt[j1] in lst_nmsp:
#                         print(listt[j1])
#                         break
#                 break
# print(listt)

# Вариант 3: Словарь переменная-списки пространств
# vvod = []
# d = {}
# n = int(input())
# for i in range(n):
#     vvod = input().split()
#     if vvod[0] == 'add':
#         if vvod[2] in d:
#             d[vvod[2]].append(vvod[1])
#         else:
#             d[vvod[2]] = [vvod[1]]
#     # if vvod[0] == 'create':
#     #     if vvod[2] in d:
#     #         d[vvod[2]].append(vvod[1])
#     #         d[vvod[1]] = ['']
#     #     else:
#     #         d[vvod[2]] = [vvod[1]]
#     if vvod[0] == 'get':
#         if vvod[2] in d:
#             x = len(d[vvod[2]])
#             # print(x)
#             print(d[vvod[2]][x-1])
#         else:
#             print('None')
#
# print(d)

# Вариант 4 - Список из словарей пар
#
# vvod = []
# nmsp_lst = []
# n = int(input())
# perem = {}
#
# for i in range(n):
#     d = {}
#     l = []
#     vvod = input().split()
#
#     if vvod[0] == 'add':
#         if vvod[1] in perem.keys():
#             perem[vvod[1]].append(vvod[2])
#         else:
#             perem[vvod[1]] = [vvod[2]]
#
#     if vvod[0] == 'create':
#         # d[vvod[1]] = vvod[2]
#         l.append(vvod[1])
#         l.append(vvod[2])
#         nmsp_lst.append(l)
#
#     if vvod[0] == 'get':
#         if vvod[2] in perem[vvod[1]]:
#             print(vvod[1])
        # else:
        #     nmsp = vvod[1]
        #     ok = False
        #     while nmsp != 'global' or ok != True:
        #         for i in range(len(nmsp_lst)):
        #             if nmsp in nmsp_lst[i].keys():
        #                 if vvod[2] in perem[nmsp]:
        #                     print(nmsp)
        #                     ok = True
        #                 else:
        #                     nmsp_tmp = nmsp_lst[i].values()
        #         nmsp = nmsp_tmp
        #     if vvod[2] in perem['global']:
        #         print('global')
        #     else:
        #         print(None)
        #
        # if vvod[2] in d[vvod[1]]:
        #     print(vvod[1])
        # elif vvod[1] in d and
# print()
# print(nmsp_lst)
# print(perem)
# print(nmsp_lst[1].keys())

# Вариант 5 - рекурсия


def _addf(nmsp, perem):

    if nmsp in d.keys():
            d[nmsp].append(perem)
    else:
            d[nmsp] = [perem]


def _createf(nmsp1, nmsp2):

    if nmsp1 in d.keys():
        d[nmsp1].append(nmsp2)
    else:
        d[nmsp1] = [nmsp2]


def _getf(nmsp, perem):


    if nmsp == 'global' and perem in d['global']:
        return nmsp
    elif nmsp == 'global' and perem not in d['global']:
        return 'None'
    elif perem in d[nmsp]:
        return nmsp
    elif nmsp != 'global':
        for k in d.keys():
            if nmsp in d[k]:
                # _getf(k, perem)
                nmsp = k
                break
        return _getf(nmsp, perem)


vvod = []
d = {}
n = int(input())
for i in range(n):
    vvod = input().split()
    if vvod[0] == 'add':
        _addf(vvod[1], vvod[2])
    if vvod[0] == 'create':
        _createf(vvod[2], vvod[1])
    if vvod[0] == 'get':
        print(_getf(vvod[1], vvod[2]))

print(d)