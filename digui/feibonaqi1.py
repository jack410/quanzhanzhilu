def Counter(Index, Start, End):
    print("第%d次计算,第一个数字是%d,第二个数字是%d" % (Index, Start, End))
    if Index == 10:
        return Start
    N = Start + End
    Number = Counter(Index + 1, End, N)
    return Number

result = Counter(1, 3 ,1)
print("得出的数字是:", result)