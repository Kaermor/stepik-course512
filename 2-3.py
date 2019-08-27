class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg == 0:
            return True
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.judge = judge
        self.pos = 0
        self.neg = 0
        self.iterable = iterable
        self.funcs = funcs
        self.ii = -1
        self.ii1 = -1
        self.iterable1 = []
        # print(self.iterable)
        # print(self.funcs)
        for i in self.iterable:
            self.pos = 0
            self.neg = 0
            # print(i)
            for j in self.funcs:
                # print(j(i))
                if j(i) is True:
                    self.pos += 1
                else:
                    self.neg += 1
            # print(self.pos, self.neg)
            if self.judge(self.pos, self.neg) is True:
                self.iterable1.append(i)
            else:
                pass


        # [self.pos +=1 for i in self.iterable if ]
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        # if self.__next__() is True:
            return self
        # else:
        #     raise StopIteration
        # return self
        # возвращает итератор по результирующей последовательности

    def __next__(self):
        if self.ii < (len(self.iterable1)-1):
            self.ii += 1
            return self.iterable1[self.ii]
        #     self.pos = 0
        #     self.neg = 0
        # # for i in self.iterable:
        #     for j in self.funcs:
        #         # print(j(self.iterable[self.ii]))
        #         if j(self.iterable[self.ii]) is True:
        #             self.pos += 1
        #         else:
        #             self.neg += 1
        #     if self.judge(self.pos, self.neg) is True:
        #         # self.ii1 += 1
        #         # self.iterable1.append(self.iterable[self.ii])
        #         return self.iterable[self.ii]
        #     else:
        #         # del(self.iterable[self.ii])
        #         # self.ii +=1
        #         return False
            # self.ii += 1 после ретёрна не работает
        else:
            raise StopIteration


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]