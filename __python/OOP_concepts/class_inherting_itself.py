class whatever(object):

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def muliplyadd(self):
        return whatever.add(self)*self.a

print(whatever(5,5).muliplyadd())
