'''
Created on Mar 14, 2018

@author: Haoran
'''
import math,random
from simulton import Simulton
import model


class Super_simulton4(Simulton):
    radius=5
    check1=False
    check2=False
    check3=False
    check4=False
    robot_busy=False
    finish_mission=False
    current_victum_mission=()
    
    #blind_search=True
    
    def __init__(self,x,y,angle,speed):
        Simulton.__init__(self,x,y,Super_simulton4.radius,Super_simulton4.radius)  #####how large are these robots, need to dis
        self._angle = angle
        self._speed = speed
        self._back_counter_left=0
        self._back_counter_right=0
        self._back_counter_top=0
        self._back_counter_bottom=0
        self.scan_flag=False
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

    
    def move_to_destiniation(self,x,y):  #python  x,y asix
        x_current,y_current=self.get_location()
        
        self.set_angle(math.atan2(y_current-y,x-x_current)+2*math.pi)
        self.change_location(self._speed*math.cos(self._angle),
                              self._speed*math.sin(self._angle))
        
        if math.fabs(x_current-x)<= math.fabs(5*math.cos(self._angle)) and math.fabs(y_current-y)<=math.fabs(5*math.sin(self._angle)):
        #if x_current==x and y_current==y  :
            return True
        else:
            return False
#     def move(self):
#         self.change_location(self._speed*math.cos(self._angle),
#                              self._speed*math.sin(self._angle))
#         self.wall_bounce()

    def move_close_to_destiniation(self,x,y):
        x_current,y_current=self.get_location()
        self.set_angle(math.atan2(y_current-y,x-x_current)+2*math.pi)
        self.change_location(self._speed*math.cos(self._angle),
                              self._speed*math.sin(self._angle))
        if math.fabs(x_current-x)<= math.fabs(15*math.cos(self._angle)) and math.fabs(y_current-y)<=math.fabs(15*math.sin(self._angle)):
        #if x_current==x and y_current==y  :
            return True
        else:
            return False
        
        
    def bounce(self,barrier_angle):
        self._angle = 2*barrier_angle - self._angle

    
    def display(self,canvas):
        
        canvas.create_oval(self._x-Super_simulton4.radius      , self._y-Super_simulton4.radius,
        self._x+Super_simulton4.radius, self._y+Super_simulton4.radius,
        fill='green')
        
        
            
    def update(self): # the way that robots move
        
        
       
        ###########boundary situation########################
        x,y      = self.get_location()    
        w,h      = self.get_dimension()
        mw,mh    = model.world()
        if model.scan_time4!=0:
            self.change_location(0,0)
        if  model.avoid_victum_counter4!=0 and model.scan_time4==0:
            print("yes22::::",model.avoid_victum_counter4)
            self._angle+=0.3*math.pi
            self.change_location(-self._speed*math.cos(self._angle),
                              -self._speed*math.sin(self._angle))
        if Super_simulton4.check1==False and model.avoid_victum_counter4==0: 
            Super_simulton4.check1=self.move_to_destiniation(390,390)
        #if Super_simulton3.check1==True and Super_simulton3.check2==False and model.avoid_victum_counter3==0:
        #        Super_simulton3.check2=self.move_to_destiniation(390,10)
        if Super_simulton4.check1==True and Super_simulton4.check3==False and model.avoid_victum_counter4==0:
            Super_simulton4.check3=True
        #current_cycle=model.get_cycle()
#         if Super_simulton.check1==False and model.avoid_victum_counter==0:
#             #print("check1 is False")
#             Super_simulton.check1=self.move_to_destiniation(0.25*mw,0.25*mh)
#             
#         if Super_simulton.check1==True and Super_simulton.check2==False and model.avoid_victum_counter==0:
#             #print("check2 is False")
#             #Super_simulton.check1=False
#             Super_simulton.check2=self.move_to_destiniation(0.25*mw,0.75*mh)
#             #print("should go into check2")
#         if Super_simulton.check2==True and Super_simulton.check3==False and model.avoid_victum_counter==0:
#             #Super_simulton.check1=False
#             Super_simulton.check3=self.move_to_destiniation(0.75*mw,0.75*mh)
#         if Super_simulton.check3==True and Super_simulton.check4==False and model.avoid_victum_counter==0:
#             #Super_simulton.check1=False
#             Super_simulton.check4=self.move_to_destiniation(0.75*mw,0.25*mh)
#         if Super_simulton.check4==True:
#             model.set_blind_search(False)
            
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
        if left_x < 4:
            print("back_counter_left motivate")
            self._back_counter_left=5
            self.change_location(5,0)
             #back_run_mode='left_x_edge'
        if  right_x > mw-4:
            print("back_counter_right motivate")
            self._back_counter_right=5
            self.change_location(-5,0)
            print(self._back_counter_right)
            #back_run_mode='right_x_edge'
        if top_y < 4:
            print("back_counter_top motivate")
            self._back_counter_top=5
            self.change_location(0,-5)
            #back_run_mode='top_y_edge'
        if bottom_y > mh-4: 
            print("back_counter_bottom motivate")
            self._back_counter_bottom=5
            self.change_location(0,5)
            #back_run_mode='bottom_y_edge'   
            
        
            
        if  self._back_counter_right>0:
            print("****************step1******************")
            if (self._back_counter_right>1):
                self.change_location(2*self._speed*math.cos(self._angle+math.pi),
                              2*self._speed*math.sin(self._angle+math.pi))
                if left_x < 4 or  top_y < 4 or bottom_y > mh-4:
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
                if  right_x > mw-4 or top_y < 4 or bottom_y > mh-4:
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
                if left_x < 4 or right_x > mw-4 or bottom_y > mh-4:
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
                if left_x < 4 or right_x > mw-4 or top_y < 4:
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
            
                 
#         self.change_location(self._speed*math.cos(self._angle),
#                              self._speed*math.sin(self._angle))
#         
        
        ##############################################################
        for i in list(model.get_static_simultons()):
            #low_range= self._angle-math.pi*(1/12) if self._angle-math.pi*(1/12)>=0 else math.pi*2+self._angle-math.pi*(1/12)
            if (i.get_location()[0]-x)**2+(i.get_location()[1]-y)**2<=900 and\
                self._angle-math.pi*(1/4)<=math.atan2(y-i.get_location()[1],i.get_location()[0]-x)+2*math.pi and\
                math.atan2(y-i.get_location()[1],i.get_location()[0]-x)+2*math.pi<=self._angle+math.pi*(1/4):
                #self._angle+=1/4*math.pi
                model.avoid_victum4=True
                
                print("come inside2")
        
        if model.avoid_victum4==True:
            model.avoid_victum_counter4=4
            model.avoid_victum4=False
            
        ######################build suspect list in lidar raneg#################
        if Super_simulton4.check3==True and Super_simulton4.check4==False:
            for i in list(model.get_static_simultons()):
                if (i.get_location()[0]-x)**2+(i.get_location()[1]-y)**2<=70756 and [i.get_location()[0]-10,i.get_location()[0]+10,i.get_location()[1]-10,i.get_location()[1]+10] not in [[k[0],k[1],k[2],k[3]]for k in model.suspect_victums]:#2/3 is detected with lidar
                    model.add_suspect_victums([i.get_location()[0]-10,i.get_location()[0]+10,i.get_location()[1]-10,i.get_location()[1]+10,False])
                    Super_simulton4.check4=True# when check4 is true, scan finished  .need to add a counter for scan time   
                    
                    
        if  Super_simulton4.check4==True and self.scan_flag==False:
            model.scan_time4=50########this number need to be test out
            self.scan_flag=True                
                    
        if Super_simulton4.robot_busy==False and Super_simulton4.check4==True and model.scan_time4==0:#need to go confirm session
            lst= list(model.suspect_victums)
            print(lst)
            lst.sort(key=lambda k:((x-k[0])**2+ (y-k[2])**2))
            if lst!=None:
                for i in lst:
                    if i[4]==False:
                        i[4]=True
                        Super_simulton4.current_victum_mission=(i[0],i[1],i[2],i[3])
                        Super_simulton4.robot_busy=True
                        break
            else:#shouldnt come to this
                print(lst)
            print("current_victum_mission2:::",Super_simulton4.current_victum_mission)
        if   Super_simulton4.robot_busy==True:  
                Super_simulton4.finish_mission=(self.move_close_to_destiniation(Super_simulton4.current_victum_mission[0],Super_simulton4.current_victum_mission[2]))
            
        if   Super_simulton4.finish_mission:
            Super_simulton4.robot_busy=False
            Super_simulton4.finish_mission=False
            for i in list(model.static_simultons):
                #if (i.get_location()[0]-x)**2+(i.get_location()[1]-y)**2<=225:##need to change the num
                if (Super_simulton4.current_victum_mission[1]-Super_simulton4.current_victum_mission[0])/2+Super_simulton4.current_victum_mission[0]==i.get_location()[0] and (Super_simulton4.current_victum_mission[3]-Super_simulton4.current_victum_mission[2])/2+Super_simulton4.current_victum_mission[2]==i.get_location()[1]:
                    print("the find one:", i.get_location()[0],i.get_location()[1])
                    i.set_find(True)
             
            
            
            
            
        
        #print(model.suspect_victums  ) 
        
        
