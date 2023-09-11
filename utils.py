class utils:
    def __init__(self, num):
        self.num = num
    def reversed(self):
        while self.num != 0:
            digit = self.num % 10
            reversed_num = reversed_num * 10 + digit
            self.num //= 10

    def formatter(self):
        return (bin(self.num), oct(self.num))