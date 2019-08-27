# Задача на количество замен подстроки на подстроку не более 1000
# def skolko(s1, a1, b1):
#     i = 0
#     while s1.count(a1) > 0: # and i <= 1000:
#         s1 = s1.replace(a1, b1)
#         i += 1
#         if i > 1000:
#             return 'Impossible'
#     return i
#
#
# # print(str.replace.__doc__)
# s = input()
# a = input()
# b = input()
# print(skolko(s, a, b))
# # print(i)


# Задача на количество вхождений подстроки в строку, в том числе перекрывающиеся
s = input()
t = input()
# print(str.count.__doc__)
sk = 0
for i in range(len(s)-len(t)+1):
    s1 = s[i:i+len(t)]
    if t in s1:
        sk += 1

print(sk)