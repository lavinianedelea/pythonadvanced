class Ball(object):

    def __init__(self, color, size):
        self.color = color
        self.size = size

    def _eq_(self,other):
        """overwrite default equal operator"""
        if isinstance(other, self.__class__):
            return self.color == other.color and self.size == other.size

    def __ne__(self, other):
        return self.color != other.color or self.size != other.size


class Box(object):

    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.color == other.color and self.size == other.size

    def __ne__(self, other):
        return self.color != other.color or self.size != other.size

ball1 = Ball ('blue' , 'small')
ball2 = Ball('blue', 'small')
box1 = Box('blue', 'small')
ball3 = Ball('green' , 'small')

print ( ball1 == ball2)
print(ball1 == ball3)
print(ball1 == box1)