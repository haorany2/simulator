'''
Created on Feb 7, 2018

@author: Haoran
'''

class Simulton:

    def __init__(self,x,y,width,height):
        self.set_location(x,y)
        self.set_dimension(width,height)
        

    def get_location(self):
        return (self._x,self._y)
    

    def set_location(self,x,y):
        self._x = x
        self._y = y 
        

    def change_location(self,dx,dy):
        self._x += dx
        self._y -= dy 
        

    def get_dimension(self):
        return (self._width,self._height)
    

    def set_dimension(self,width,height):
        self._width  = width
        self._height = height
        

    def change_dimension(self,dw,dh):
        self._width  += dw
        self._height += dh
        

    # computes distance from center to center
    def distance(self,xy):
        return ((self._x -xy[0])**2  + (self._y -xy[1])**2)**.5

    
    # determines whether xy is in the bounding box of self
    def contains(self,xy):
        return self._x - self._width/2  <= xy[0] <= self._x + self._width/2 and\
               self._y - self._height/2 <= xy[1] <= self._y + self._height/2


        