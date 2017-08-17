def Counter(n1, n2):
    if n1 > 100000:
        return
    print("Counter:", n1)
    n3 = n1 + n2
    Counter(n2, n3)

Counter(2,1)