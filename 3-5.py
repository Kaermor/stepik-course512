# import csv
# import re
#
# lst = []
# with open("Crimes.csv") as f:
#     rr = csv.reader(f)
#     tmpl = r'\d\d/\d\d/2015 \d\d:\d\d:\d\d \w\w'
#     # lst1 = re.findall(tmpl, rr)
#     for row in rr:
#         print(row[2])
#         print(re.search(tmpl, row[2]))
#         if re.search(tmpl, row[2]) is not None:
#             lst.append(row[5])
#
# max = 0
# st = set(lst)
# print(st)
# for s in st:
#     print('s = ', s, ' = ', lst.count(s))
#     if lst.count(s) > max:
#         # print('s = ', s, ' = ', lst.count(s))
#         max = lst.count(s)
# print(max)

# -----------------------------------------------

import json


def glubina(ll):
    llc = 0
    dl[ll] += 1
    if ll in dictc.keys() and len(dictc[ll]) == 0 :
        if dl[ll] == 0:
            llc = llc + 1
        return llc
    elif ll in dictc.keys() and len(dictc[ll]) != 0:
        for i in dictc[ll]:
            if i not in dl.keys() or dl[i] == 0:
                dl[i] += 1
                llc = llc + 1 + glubina(i)
            # else:
            #     dl[i] = 1
            #     llc = llc + glubina(i)
        # print('dl=', dl)
        # print('llc1=', llc)
        return llc


# def sverhu(ll):
#     llc = 0
#     # for k in dictp.keys():
#         if ll in dictc.keys() and len(dictc[ll]) == 0:
#             llc = llc + 1
#             return llc
#         elif ll in dictc.keys() and len(dictc[ll]) != 0:
#             for i in dictc[ll]:
#                 if ll == i:
#                     llc = llc + 1



data = json.loads(input())
print(data)
# print(data[0]['name'])
dictc = {}
dictp = {}
dr = {}
lst = []


for d in data:
    lst.append(d['name'])
    dictp[d['name']] = d['parents']
lst.sort()
print('lst=', lst)
# print('dictp=', dictp)

for l in lst:
    dictc[l] = []
    for d in data:
        if l in d['parents']:
            dictc[l].append(d['name'])
print('dictc=', dictc)

for l in lst:
    dl = {i: 0 for i in lst}
    # print('dl0=', dl)
    print(l, ':', glubina(l)+1)


