'''
Geometry.py
Created on Feb 5, 2013
@author: Aria Bennett

This module deals with creating rectangles 
(Which are sometimes also squares!) and doing
questionable things to them.
'''

#===============================================================================
# Class Point
#
# Defines the Point class which consists of two values
# representing an x and y coordinate.
#===============================================================================
class Point():
    def __init__(self, point_x, point_y):
        self.x = point_x
        self.y = point_y
    def __str__(self):
        return str((self.x, self.y))

#===============================================================================
# Class Box
# 
#   tl == top-left | tr == top-right
# bl == bottom left | br == bottom-right
#===============================================================================
class Box():
    #===========================================================================
    # Function __init__
    # 
    # Initializes four point objects for each corner of
    # the box plus a width and height.
    #===========================================================================
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.tl = Point(x, y)
        self.tr = Point(self.calc_tr()[0], self.calc_tr()[1])
        self.bl = Point(self.calc_bl()[0], self.calc_bl()[1])
        self.br = Point(self.calc_br()[0], self.calc_br()[1])
    #===========================================================================
    # Function __str__
    # 
    # Alters the return value when the class is called
    # by a print function. Instead prints values
    # of top left point and bottom left point
    #===========================================================================
    def __str__(self):        
        return str((self.tl.x, self.tl.y)) + " => " + str((self.br.x, self.br.y))
    
    #===========================================================================
    # The following three functions return their
    # respective corners
    #===========================================================================
    def calc_tr(self):
        return ((self.tl.x + self.width), (self.height))
    def calc_bl(self):
        return ((self.tl.x), (self.tl.y + self.height))
    def calc_br(self):
        return ((self.tl.x + self.width), (self.tl.y + self.height))
    
    #===========================================================================
    # The following functions return left, right, top, and bottom point locations
    #===========================================================================
    def left(self):
        return self.tl.x
    def right(self):
        return self.br.x
    def top(self):
        return self.tl.y
    def bottom(self):
        return self.br.y
    #===========================================================================
    # Function area
    # 
    # Returns the area of the rectangle
    #===========================================================================
    def area(self):
        return self.find_difference(self.tl.x, self.tr.x)*self.find_difference(self.tl.y, self.br.y)
    
    #===========================================================================
    # Function find_difference
    # 
    # returns the absolute_value distance
    # between two points
    #===========================================================================
    def find_difference(self, a, b):
        #===========================================================================
        # Imports
        #===========================================================================
        import math
        
        a = math.fabs(a)
        b = math.fabs(b)
        
        if a > b:
            return a - b
        elif b > a:
            return b - a
        else:
            return 0;
        
    def is_intersecting(self, other):
        if self.tr.x < other.tl.x:
            return False
        if self.tl.x > other.tr.x:
            return False
        if self.br.y < other.tr.y:
            return False
        if self.tr.y > other.br.y:
            return False
        return True
        

if __name__ == '__main__':
    box1 = Box(2,3,8,4)
    print box1
    print box1.left()
    print box1.right()
    print box1.top()
    print box1.bottom()
    print box1.area()
    print ""
    b1 = Box(0, 0, 10, 10)
    b2 = Box(0, 0, 5, 5)
    b3 = Box(9, 9, 15, 15)
    empty = Box(5, 5, 0, 0)
    print b1
    print box1.is_intersecting(b3)