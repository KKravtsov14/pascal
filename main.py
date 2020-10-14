class Pascal:
    def __init__(self, list):
        self.list = list

    def __setitem__(self, key, value):
        if key > 0 and key < len(self.list) + 1:
            self.list[key] = value

    def __getitem__(self, item):
        if item > 0:
            return self.list[item - 1]
        elif item < 1:
            return KeyError
        elif item > len(self.list):
            return KeyError

    def __str__(self):
        return str(self.list)

    def index(self, value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                return i + 1
                break

a = Pascal([1, 2, 3, 4, 5])
print(a)
print(a[2])
print(a.index(2))