def concat(cortege):
    curs = list(range(len(cortege)))
    li = list(cortege)
    result = []
    while 1:
        for i in range(len(li)):
            while curs[i] < len(li[i]):
                a = li[i][curs[i]]
                curs[i] += 1
                if a % 2 == i:
                    result.append(a)
                    break
            else:
                i = (i+1) % 2
                return result + li[i][curs[i]:]


arg = ([1, 2, 3, 4, 5, 6], [100, 101, 102, 103, 104, 105, 100, 107, 109])
print(concat(arg))
