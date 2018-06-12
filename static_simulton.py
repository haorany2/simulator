'''
Created on Feb 7, 2018

@author: Haoran
'''
from simulton import Simulton
class Static_simulton(Simulton):
    '''
    classdocs
    '''
    radius=10
   

    def __init__(self, x,y):
        Simulton.__init__(self, x, y, Static_simulton.radius*2, Static_simulton.radius*2)
        self.find=False
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill='black')
        
    def set_find(self, x):
        self.find=x
        
    def get_find(self):
        return self.find
    def update(self):
        return self.find; 
    
    