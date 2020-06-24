def generator(number):
    result = 1
    while True:
        yield result
        result *= number


print('Start')
gen = generator(2)
for i in range(5):
    print(next(gen))
