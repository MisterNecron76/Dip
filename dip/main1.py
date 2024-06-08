import robomaster
import time
from robomaster import robot
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
root = Tk()

root.title("Robomaster")
root.geometry("550x365")




def connect():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    version = ep_robot.get_version()
    battary = ep_robot.get_battary()
    messagebox.showinfo("Успешное соединение. Robomaster Version", version)
    print("Robot version: {0}".format(version))
    #messagebox.showerror("Error", "Connect failed")


def first():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_chassis = ep_robot.chassis

    x_val = 1
    y_val = 3.5
    y = -10
    v_val = 3
    y2 = -1.5
    x = -10
    x2 = -0.5
    ep_chassis.move(x=x_val, y=0, z=0, xy_speed=0.8).wait_for_completed()
    ep_chassis.drive_wheels(w1=speed, w2=0, w3=0, w4=0)
    time.sleep(slp)
    ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=speed)
    time.sleep(slp)
    ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=speed1)
    time.sleep(slp)
    ep_chassis.drive_wheels(w1=speed, w2=0, w3=0, w4=0)
    time.sleep(slp)
    ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=speed)
    time.sleep(slp)
    ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=speed1)
    time.sleep(slp)
    ep_chassis.move(x=x_val, y=0, z=0, xy_speed=0.8).wait_for_completed()
    ep_robot.close()

def second():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_chassis = ep_robot.chassis

    x_val = 1.8
    y_val = 3.5
    speed = 50
    speed1 = 60
    slp = 1
    ep_chassis.move(x=x_val, y=0, z=0, xy_speed=0.8).wait_for_completed()
    ep_chassis.drive_wheels(w1=speed, w2=0, w3=0, w4=0)
    time.sleep(slp)
    ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=speed)
    time.sleep(slp)
    ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=speed1)
    time.sleep(slp)
    ep_chassis.move(x=x_val, y=0, z=0, xy_speed=0.8).wait_for_completed()
    ep_robot.close()

def third(): 
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_chassis = ep_robot.chassis
    
    x_val = 1.8
    y_val = 3.5
    z_val = 2
    speed = 50
    speed1 = 60
    slp = 1
    ep_chassis.drive_wheels(w1=speed, w2=0, w3=0, w4=0)
    time.sleep(slp)
    ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=speed)
    time.sleep(slp)
    ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=speed1)
    time.sleep(slp)
    p_chassis.move(x=0, y=0, z=z_val, z_speed=0.6).wait_for_completed()

def select():
    print("Selected " + str(var.get()))

var = IntVar()

button = Button(root, text="Robomaster Status",command=connect)
button.pack(anchor=NW)
Label(root,text="Выберите маршрут").pack(anchor=NW)
Radiobutton(text='Движение по маршруту', variable=var, value=1, command=first).pack(anchor=NW)
Radiobutton(text='Движение вперед с разворотом', variable=var, value=2, command=second).pack(anchor=NW)
Radiobutton(text='Движение вперед', variable=var, value=3, command=third).pack(anchor=NW)

img = ImageTk.PhotoImage(Image.open("R2.png"))

b = Label(image = img)

b.pack(anchor=CENTER)

root.mainloop()