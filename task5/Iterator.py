class NumberIterator:

    def __init__(self, number, type='int'):
        if type == 'int':
            if number < -2_147_483_648 or number > 2_147_483_647:
                raise ValueError("Number isn't integer")
            self.size = 32
        elif type == 'long':
            if number < -9_223_372_036_854_775_808 or number > 9_223_372_036_854_775_807:
                raise ValueError("Number isn't long")
            self.size = 64
        elif type == 'short':
            if number < -32_768 or number > 32_767:
                raise ValueError("Number isn't short")
            self.size = 16
        elif type == 'byte':
            if number < -128 or number > 127:
                raise ValueError("Number isn't byte")
            self.size = 8
        else:
            raise ValueError("Unknown type")
        self.number = number
        self.mask = 1
        self.count = 0

    def get_number(self):
        return self.number

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.size:
            raise StopIteration()
        byte = self.number & self.mask != 0
        self.mask <<= 1
        self.count += 1
        return byte


print('Starting')
iterator = iter(NumberIterator(32, 'byte'))
try:
    for b in iterator:
        print(b)
except StopIteration:
    print("Stop iteration")
