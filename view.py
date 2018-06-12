'''
Created on Feb 7, 2018

@author: Haoran
'''
from tkinter import Tk,Frame,TOP,LEFT,BOTTOM,RAISED,BOTH

# import controller to call/create widgets and position them in the view
import controller


# Construct a simple root window
root = Tk()
root.title("Simulation")
root.protocol("WM_DELETE_WINDOW",quit)
root.resizable(width=False, height=False)
frame0=Frame(root)
frame = Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)
# Place buttons simply at the top
frame0.pack(side=TOP)
frame.pack(side=TOP)
frame2.pack(side=TOP)
frame3.pack(side=TOP)
frame4.pack(side=TOP)
controller.progress     (frame0,text="0 updates/0 simultons",width=25,relief=RAISED).pack(side=LEFT)
controller.reset_button (frame,text="Reset")     .pack(side=LEFT)
controller.start_button (frame,text="Start")     .pack(side=LEFT)
controller.stop_button  (frame,text="Stop")      .pack(side=LEFT)
controller.step_button  (frame,text="Step")      .pack(side=LEFT)
controller.object_button(frame,text="Remove")    .pack(side=LEFT)
controller.object_button(frame2,text="Static_simulton")      .pack(side=LEFT)
controller.object_button(frame2,text="Mobile_simulton")      .pack(side=LEFT)
controller.object_button(frame3,text="Super_simulton1")   .pack(side=LEFT)
controller.object_button(frame3,text="Super_simulton2").pack(side=LEFT)
controller.object_button(frame4,text="Super_simulton3")  .pack(side=LEFT)
controller.object_button(frame4,text="Super_simulton4")    .pack(side=LEFT)
# controller.object_button(frame,text="Special")   .pack(side=LEFT)


 
# Place canvas in the space below
controller.simulation_canvas(root,width=400,height=400,bg="yellow").pack(side=BOTTOM,expand=True,fill=BOTH)