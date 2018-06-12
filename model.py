'''
Created on Feb 7, 2018

@author: Haoran
'''
import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from static_simulton import Static_simulton
from mobilesimulton import  Mobile_simulton
from supersimulton  import Super_simulton1
from supersimulton2  import Super_simulton2
from supersimulton3  import Super_simulton3
from supersimulton4  import Super_simulton4
import math
import random


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
avoid_victum1=False
avoid_victum2=False
avoid_victum3=False
avoid_victum4=False
running     = False
blind_search=True###########will use in the future
cycle_count = 0# general time counting
avoid_victum_counter1=0
avoid_victum_counter2=0
avoid_victum_counter3=0
avoid_victum_counter4=0
static_simultons       = set()
mobile_simultons       = set()
super_simultons1        =set()
super_simultons2        =set()
super_simultons3        =set()
super_simultons4        =set()
suspect_victums        =[]
click=''
back_counter_left=0
back_counter_right=0
back_counter_top=0
back_counter_bottom=0

scan_time1=0
scan_time2=0
scan_time3=0
scan_time4=0
#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())




    
    
    
    
#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,static_simultons,mobile_simultons,super_simultons1,super_simultons2,super_simultons3,super_simultons4,count_found
    running     = False
    cycle_count = 0
    count_found=0#how many victums has been found
    static_simultons = set()
    mobile_simultons = set()
    super_simultons1  =set()
    super_simultons2  =set()
    super_simultons3  =set()
    super_simultons4  =set()
  #  display_all()
    #print(floaters)
    #print(balls)
#start running the simulation
def start ():
    global running
    running = True
   # print(floaters)
    
   # print(balls)
#stop running the simulation (freezing it)
def stop ():
    global running
    
    running= False
    

#step just one update in the simulation
def step ():
    global running
    if running ==True:
        update_all()
        stop()
    elif running ==False:
        start()
        update_all()
        stop()
        
##################get global variables to use in other files
def get_static_simultons():
    global static_simultons
    return static_simultons

def add_suspect_victums(x):#x is tuple with position range. GPS error is included
    global suspect_victums
    return suspect_victums.append(x)
def set_blind_search(x):# should set blind_search to be True or false
    global blind_search
    blind_search=x
# def get_back_counter_left():
#     global back_counter_left
#     return back_counter_left
#     
# 
# def set_back_counter_left(x):
#     global back_counter_left
#     back_counter_left=x
#     
#     
# def get_back_counter_right():
#     global back_counter_right
#     return back_counter_right
#     
# 
# def set_back_counter_right(x):
#     global back_counter_right
#     back_counter_right=x
#     
#     
#     
# def get_back_counter_top():
#     global back_counter_top
#     return back_counter_top
#     
# 
# def set_back_counter_top(x):
#     global back_counter_top
#     back_counter_top=x
#  
#  
#  
#  
# def get_back_counter_bottom():
#     global back_counter_bottom
#     return back_counter_bottom
#     
# 
# def set_back_counter_bottom(x):
#     global back_counter_bottom
#     back_counter_bottom=x
#     
#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global click
    click=kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if click =='Static_simulton':
        t = eval(click)
        static_simultons.add(t(x,y))
  
    if click =='Mobile_simulton':
        t = eval(click)
        mobile_simultons.add(t(x,y,0.6*math.pi,5))   ###### 1/18*math.pi  not sure the initial speed, and initial angel
    
    if click =='Super_simulton1':
        t = eval(click)
        super_simultons1.add(t(x,y,0.6*math.pi,4))
    
    if click =='Super_simulton2':
        t = eval(click)
        super_simultons2.add(t(x,y,0.6*math.pi,4))
    if click =='Super_simulton3':
        t = eval(click)
        super_simultons2.add(t(x,y,0.6*math.pi,4))
    if click =='Super_simulton4':
        t = eval(click)
        super_simultons2.add(t(x,y,0.6*math.pi,4))
    if click =='Remove':
        for i in [ static_simultons,mobile_simultons,super_simultons1,super_simultons2,super_simultons3,super_simultons4]:
           
            for b in list(i):
                
                if b.contains((x,y)):
                    remove(b) 
        
   # if click=='Reset':
   #     reset()
        
        

#add simulton s to the simulation
def add(s):
    if type(s)==Static_simulton:
        static_simultons.add(s)
    
    if type(s)==Mobile_simulton:
        mobile_simultons.add(s)
        
        
    if type(s)== Super_simulton1:
        super_simultons1.add(s)
        
    if type(s)== Super_simulton2:
        super_simultons2.add(s)
    if type(s)== Super_simulton3:
        super_simultons3.add(s)
    if type(s)== Super_simulton4:
        super_simultons4.add(s)
# remove simulton s from the simulation    
def remove(s):
    if type(s)==Static_simulton:
        static_simultons.remove(s)
    if type(s)==Mobile_simulton:
        mobile_simultons.remove(s)
    if type(s)== Super_simulton1:
        super_simultons1.remove(s)    
    if type(s)== Super_simulton2:
        super_simultons2.remove(s)  
    if type(s)== Super_simulton3:
        super_simultons3.remove(s)  
    if type(s)== Super_simulton4:
        super_simultons4.remove(s)  

#find/return a set of simultons that each satisfy predicate p    



#call update for every simulton in the simulation
def update_all():
    global cycle_count
    global static_simultons
    global running
    global avoid_victum_counter1
    global avoid_victum_counter2
    global avoid_victum_counter3
    global avoid_victum_counter4
    global scan_time1
    global scan_time2
    global scan_time3
    global scan_time4
#     global back_counter_left
#     global back_counter_right
#     global back_counter_top
#     global back_counter_bottom
    if avoid_victum_counter1!=0:
        avoid_victum_counter1-=1
    if avoid_victum_counter2!=0:
        avoid_victum_counter2-=1
    if avoid_victum_counter3!=0:
        avoid_victum_counter3-=1
    if avoid_victum_counter4!=0:
        avoid_victum_counter4-=1
    if scan_time1!=0:
        scan_time1-=1
    if scan_time2!=0:
        scan_time2-=1
    if scan_time3!=0:
        scan_time3-=1
    if scan_time4!=0:
        scan_time4-=1
    if running:
#         if back_counter_left>0:
#             back_counter_left-=1
#         if back_counter_right>0:
#             back_counter_right-=1
#             
#         if back_counter_top>0:
#             back_counter_top-=1
#             
#         if back_counter_bottom>0:
#             back_counter_bottom-=1
        cycle_count += 1
        for b in[ static_simultons,mobile_simultons,super_simultons1,super_simultons2,super_simultons3,super_simultons4]:
            for i in list(b):
                i.update()
        
        count_found=0
        for i in list(static_simultons):
            if i.get_find()==True:
                print(i.get_location()[0],i.get_location()[1])
                count_found+=1
        if count_found==len(list(static_simultons)):
            running=False
            print("mission complete")
            #print(count_found)
            #print(len(list(static_simultons)))
            

#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        
        controller.the_canvas.delete(o)
    
    for b in[ static_simultons,mobile_simultons,super_simultons1,super_simultons2,super_simultons3,super_simultons4]:
        for i in list(b):
            i.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(static_simultons))+" static_simultons/\n"+str(len(mobile_simultons))+" mobile_simultons/"+str(cycle_count)+" cycles")

 #+str(len(floaters))+'floaters/'+str(len(hunters))+'hunters'+str(len(blackholes))+'blackholes'+str(len(pulsators))+'pulsators' 
