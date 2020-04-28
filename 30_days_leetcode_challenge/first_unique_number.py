from collections import OrderedDict


class FirstUnique:

    def __init__(self, nums: list):
        self.nums = nums
        self.values = OrderedDict()
        self.freq = {}
        self.on_init(self.nums)

    def showFirstUnique(self) -> int:
        if not self.values:
            return -1
        return next(iter(self.values.items()))[0]

    def add(self, value: int) -> None:
        self.nums.append(value)
        if value in self.values:
            del self.values[value]
            self.freq[value] += 1

        elif value not in self.values and value not in self.freq:
            if self.values:
                self.values.update({value: self.values.get(next(reversed(self.values))) + 1})
            else:
                self.values.update({value: 0})
            self.freq[value] = 1

        else:
            self.freq[value] += 1

    def on_init(self, nums):
        for n in nums:
            if n not in self.values and n not in self.freq:
                if self.values:
                    self.values.update({n: self.values.get(next(reversed(self.values))) + 1})
                else:
                    self.values.update({n: 0})
                self.freq[n] = 1
            else:
                if n in self.values:
                    del self.values[n]
                self.freq[n] += 1



if __name__ == '__main__':
    s = FirstUnique([7, 7, 10,1, 3, 4, 1, 2, 2, 8, 8, 5, 6, 7,10])
    print(s.showFirstUnique()[0])
    print(s.freq)
