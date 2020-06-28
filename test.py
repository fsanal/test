class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def find(self, item):
        return [self.x + item]

x = Test(5, 3)
print(x.find(5))