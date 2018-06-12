'''
Created on Feb 8, 2018

@author: Haoran
'''
import math,random
from simulton import Simulton
import model


class Mobile_simulton(Simulton):
    radius=5
    
    
    def __init__(self,x,y,angle,speed):
        Simulton.__init__(self,x,y,Mobile_simulton.radius,Mobile_simulton.radius)  #####how large are these robots, need to dis
        self._angle = angle
        self._speed = speed
        self._back_counter_left=0
        self._back_counter_right=0
        self._back_counter_top=0
        self._back_counter_bottom=0
        
    def get_angle(self):
        return self._angle
    
    
    def set_angle(self,angle):
        self._angle = angle
    
    
    def get_speed(self):
        return self._speed
    
    
    def set_speed(self,speed):
        self._speed = speed
        
        
    # velocity includes speed and angle        
    def set_velocity(self,speed,angle):
        self.set_speed(speed)
        self.set_angle(angle)

        
    def randomize_angle(self):
        self._angle = 2*math.pi*random.random()

    
#     def move(self):
#         self.change_location(self._speed*math.cos(self._angle),
#                              self._speed*math.sin(self._angle))
#         self.wall_bounce()

        
    def bounce(self,barrier_angle):
        self._angle = 2*barrier_angle - self._angle

    
    def display(self,canvas):
        
        canvas.create_oval(self._x-Mobile_simulton.radius      , self._y-Mobile_simulton.radius,
        self._x+Mobile_simulton.radius, self._y+Mobile_simulton.radius,
        fill='blue')
        
        
            
    def update(self): # the way that robots move
        
        
        
        ###########boundary situation########################
        x,y      = self.get_location()
        w,h      = self.get_dimension()
        mw,mh    = model.world()
        #current_cycle=model.get_cycle()
        
        left_x   = x - w/2
        right_x  = x + w/2
        top_y    = y - h/2
        bottom_y = y + h/2
        if self._back_counter_left>0:
            print("back_counter_left start:" ,self._back_counter_left)
            self._back_counter_left-=1
        if self._back_counter_right>0:
            print("back_counter_right start:", self._back_counter_right)
            self._back_counter_right-=1
        if self._back_counter_top>0:
            print("back_counter_top start")
            self._back_counter_top-=1
        if self._back_counter_bottom>0:
            print("back_counter_bottom start")
            self._back_counter_bottom-=1
            
            
#         if Mobile_simulton.back_counter==0:
#             back_run_mode=''

#         if left_x < 0 or right_x > mw or top_y < 0 or bottom_y > mh :
#             #Mobile_simulton.back_run=True
#             Mobile_simulton.back_counter=5
#             
        if left_x < 10:
            print("back_counter_left motivate")
            self._back_counter_left=5
            self.change_location(5,0)
             #back_run_mode='left_x_edge'
        if  right_x > mw-10:
            print("back_counter_right motivate")
            self._back_counter_right=5
            self.change_location(-5,0)
            print(self._back_counter_right)
            #back_run_mode='right_x_edge'
        if top_y < 10:
            print("back_counter_top motivate")
            self._back_counter_top=5
            self.change_location(0,-5)
            #back_run_mode='top_y_edge'
        if bottom_y > mh-10: 
            print("back_counter_bottom motivate")
            self._back_counter_bottom=5
            self.change_location(0,5)
            #back_run_mode='bottom_y_edge'   
            
        
            
        if  self._back_counter_right>0:
            print("****************step1******************")
            if (self._back_counter_right>1):
                self.change_location(2*self._speed*math.cos(self._angle+math.pi),
                              2*self._speed*math.sin(self._angle+math.pi))
                if left_x < 10 or  top_y < 10 or bottom_y > mh-10:
                    self._back_counter_right=1
            else:
                self._angle+=1/18*math.pi
                self._angle%= (2*math.pi)
#                 if self._angle%(2* math.pi)<0.5*math.pi:
#                     self._angle+=1/9*math.pi
#                     self._angle%= (2*math.pi)
#                 else:
#                     self._angle+=17/9*math.pi
#                     self._angle%=(2*math.pi)

        
        
        
        if    self._back_counter_left>0:
            if self._back_counter_left>1:
                self.change_location(2*self._speed*math.cos(self._angle+math.pi),
                              2*self._speed*math.sin(self._angle+math.pi))
                if  right_x > mw-10 or top_y < 10 or bottom_y > mh-10:
                    self._back_counter_left=1
            else:
                self._angle+=1/18*math.pi
                self._angle%= (2*math.pi)   
#                 if self._angle%(2* math.pi)<math.pi:
#                     self._angle+=17/9*math.pi
#                     self._angle%= (2*math.pi)
#                     
#                 else:   
#                     self._angle+=1/9*math.pi
#                     self._angle%= (2*math.pi)
           
        
        
        
        
        
            
        if    self._back_counter_top>0:
            if self._back_counter_top>1:
                self.change_location(2*self._speed*math.cos(self._angle+math.pi),
                            2*self._speed*math.sin(self._angle+math.pi))
                if left_x < 10 or right_x > mw-10 or bottom_y > mh-10:
                    self._back_counter_top=1
            else: 
                self._angle+=1/18*math.pi
                self._angle%= (2*math.pi)  
                
                
                
#                 if self._angle%(2* math.pi)<0.5*math.pi:
#                     self._angle+=17/9*math.pi
#                     self._angle%= (2*math.pi)
#                     
#                 else:   
#                     self._angle+=1/9*math.pi
#                     self._angle%= (2*math.pi)
            
            
            
            
        if    self._back_counter_bottom>0:
            if self._back_counter_bottom>1:
                self.change_location(2*self._speed*math.cos(self._angle+math.pi),
                            2*self._speed*math.sin(self._angle+math.pi))
                if left_x < 10 or right_x > mw-10 or top_y < 10 :
                    self._back_counter_bottom=1
            else:  
                self._angle+=1/18*math.pi
                self._angle%= (2*math.pi) 
                
                
#                 if self._angle%(2* math.pi)<1.5*math.pi:
#                     self._angle=17/9*math.pi
#                     self._angle%= (2*math.pi)
#                     
#                 else:   
#                     self._angle+=1/9*math.pi
#                     self._angle%= (2*math.pi)
            
                 
        self.change_location(self._speed*math.cos(self._angle),
                             self._speed*math.sin(self._angle))
        
        
        ##############################################################
        for i in list(model.get_static_simultons()):
            if (i.get_location()[0]-x)**2+(i.get_location()[1]-y)**2<=400:
                i.set_find(True)