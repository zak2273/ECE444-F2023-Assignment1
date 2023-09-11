class utils:
    def __init__(self, num):
        self.num = num
        
    def reversed(self):
        number = int(self.num)
        reversed_num = 0
        while number != 0:
            digit = number % 10
            reversed_num = (reversed_num * 10) + digit
            number //= 10
        return reversed_num

    def formatter(self):
        number = int(self.num)
        return (bin(number), oct(number))