class Rectangle:
    def __init__(self,left,top,width,height):
        self._left = left
        self._top = top
        self._width=width
        self._height=height
        self._set_right()
        self._set_bottom()

    def get_left(self):
        return self._left

    def get_bottome(self):
        return self._bottom

    def get_top(self):
        return self._top

    def get_right(self):
        return self._right

    def _set_right(self):
        self._right=self._left+self._width

    def _set_bottom(self):
        self._bottom=self._top+self._height

    def is_inside(self, other_rect):
        isInLeft = self.get_left()>= other_rect.get_left()
        isInRight = self.get_right()<=other_rect.get_right()
        isInBottom = self.get_bottome()<=other_rect.get_bottome()
        isInTop = self.get_top()>=other_rect.get_top()
        isInside=isInLeft and isInBottom and isInRight and isInTop
        return isInside

def read_rect():
    inputDate = input().split(' ')
    left = int(inputDate[0])
    top = int(inputDate[1])
    widht = int(inputDate[2])
    height = int(inputDate[3])
    rectangle = Rectangle(left,top,widht,height)
    return rectangle

rect = read_rect()
another_rect = read_rect()
isInside = rect.is_inside(another_rect)

if isInside:
    print('Inside')
else:
    print('Not inside')