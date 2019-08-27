# import requests
# import re
#
# A = input()
# B = input()
# k = 0
# resa = requests.get(A)
# # print(resa.status_code)
# # print(resa.headers['Content-Type'])
# # resb = requests.get(B)
# # print(resb.status_code)
# # print(resb.headers['Content-Type'])
# # print(resa.text)
# tmpl = r"<a href=.+\">"
# lstssa = re.findall(tmpl, resa.text)
# # print(lstssa)
# for i in lstssa:
#     # print(i)
#     # print(i.lstrip("<a href=").lstrip('\"').rstrip('>\"'))
#     resc = requests.get(i.lstrip("<a href=").lstrip('\"').rstrip('>\"'))
#     # print(resc.text.lstrip("<a href=").lstrip('\"').rstrip('>\"'))
#     lstssc = re.findall(tmpl, resc.text)
#     for j in lstssc:
#         # print(j)
#         if j.lstrip("<a href=").lstrip('\"').rstrip('>\"') == B:
#             k = 1
#             break
# if k == 1:
#     print('Yes')
# else:
#     print('No')
# -----------
# link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

import requests
import re

a = input().strip()
resa = requests.get(a)
# print(resa.text)
tmpl = r'<a[^>]*?href=[\"\'](?:[^>]*?://){0,1}(?:\.\.){0,1}([^:/]*?)(?:[:/][^>]*?){0,1}[\"\'][^>]*?>'    # r'<a[^>]*?href="(.*?)"[^>]*?>'
lst = re.findall(tmpl, resa.text)
st = set(lst)
lst1 = list(st)
lst1.sort()
for i in lst1:
    print(i)