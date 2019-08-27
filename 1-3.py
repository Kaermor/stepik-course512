# a = []
#
# def foo(arg1, arg2):
#   a.append("foo")
#
# foo(a.append("arg1"), a.append("arg2"))
#
# print(a)


# def closest_mod_5(x):
#   if x % 5 == 0:
#     y = x
#   else:
#     y = (x//5+1)*5
#   return y
#
# x = int(input())
# print((x+4)//5*5)

# def s(a, *vs, b=10):
#     res = a + b
#     for v in vs:
#         res += v
#     return res
#
#
# print(s(21))
# def c(n, k):
#     if k == 0:
#         return 1
#     elif k > n:
#         return 0
#     else:
#       return c(n-1, k) + c(n-1, k-1)
#
#
# n, k = map(int, input().split())
# print(c(n, k))