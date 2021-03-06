import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return self.x, self.y
    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    
    def dist(self):
        return math.sqrt()
    
    