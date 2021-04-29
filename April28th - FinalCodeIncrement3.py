# -*- coding: utf-8 -*-
import Tkinter  # python 2.7 formatting
import tkMessageBox  # message box tool
from decimal import Decimal  # for maths
import math
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt     #you may need to inatall matplotlib 

GravityList = ["Earth", "Moon", "Mars", "Jupiter", "Saturn"]

""" 

This function gives the y value for the graph given an x value. 

""" 

def x_to_y_func(inputx, initial_velocity, angle, height, gravity):  
  # 4 lines copied from Hugh's projectiles calc function   
  angle_float = float(angle)   
  angle_rad = math.radians(angle_float)  # converts angle to radians   
  Ux = float(initial_velocity * math.cos(angle_rad))  # finds the horizontal component of velocity   
  Uy = float(initial_velocity * math.sin(angle_rad))  # finds the vertical component of velocity   
  return float(inputx/Ux)*float(Uy-float(0.5*gravity*inputx/Ux))+float(height) 



def plotgraph(x,y):

    plt.style.use('ggplot')  #the style/theme I want my graph to take 
    #x = 0#x list 
    #y = 0#y list
    plt.plot(x, y, color='b', linewidth = 4) 
    plt.title('Trajectory Graph') 
    plt.xlabel('Range')
    plt.ylabel('Height') 
    plt.grid(True) #this adds a grid 
    plt.show() 

""" 
assign_xy_to_list function arguments: 
step: how much the x value (1 = 1 metre) should increase by in the list (1 should be good enough, otherwise we can make the step smaller) 
x_or_y: type in "x" or "y" here, if "x" will create the list for x values, if "y" will create the list for y values 
Inputs: input a list of the inputs taken from the calculator, important to calculate y values, in this case the list needs to be in the following order [height, velocity, angle, gravity] 
Outputs: input a list of the outputs calculated from the projectile_calc function, this is used so the lists know to end at the maximum range, this output list should be in the same order as the output of the calculator function (which is a list) 
""" 
def assign_xy_to_list(step, x_or_y, Inputs, Outputs): 
  i = 0 #Start graph at x=0 
  if x_or_y == "x": #For creating a list or x values 
    values_list = [] #Create new list 
    while i < Outputs[2]: #While x is less than the total range 
      values_list.append(i) #Add the x value to list 
      i = i + step #Determines the interval which x values are added 
    values_list.append(Outputs[2]) #Final entry is the x co-ordinate of the range 
    return values_list #Outputs list of x values 
  elif x_or_y == "y": 
    values_list = [] #For creating a list or y values 
    while i < Outputs[2]: #While x is less than the total range 
      values_list.append(x_to_y_func(i, Inputs[1], Inputs[2], Inputs[0], Inputs[3])) #Calculates y value using x, uses all the inputs. 
      i = i + step #Moves to next x value to use to calculate y 
    values_list.append(x_to_y_func(Outputs[2], Inputs[1], Inputs[2], Inputs[0], Inputs[3])) #Calculates y value when x is at maximum range (Should be 0)  
    return values_list #Outputs list of y values 

 


""" Harry 
This function can be copied into the code, theres a bit if code 
after the function which can be used to test how it works 

The first argument: input, is the input which is the value you want to check. 

The second argument: min, is the minimum bound, if left out it will not limit 
how small the input can be.  

The third argument: max, is the maximum bound, if left out it will not limit 
how large the input can be.

The fourth argument: cap, determines whether a value outside the range will return 
nothing, or just best closest value, if left out it won't return the closest value.   
"""


def checker(input, min="None", max="None", cap=False):
    # if isinstance(input, str): #Not sure if its entirely relevant
    try:  # Will try to convert the string to a float
        input = float(input)
        returnval = input  # Will return the value unless it doesnt lie in the boundaries
        if min != "None" and input < float(min):  # If theres a min value and the input exceeds it...
            if cap == False:
                returnval = "Outside range - Less than " + str(
                    min)  # This can be altered to fit whatever the code needs
            else:
                returnval = float(min)  # By making the cap value True rather than displaying an error...
                # It can return the best value within the bounaries.
        if max != "None" and input > float(max):  # If theres a max value and the input exceeds it...
            if cap == False:
                returnval = "Outside range - Greater than " + str(max)
            else:
                returnval = float(max)
        return returnval
    except ValueError:  # If theres an error converting string to float returns a string...
        return "Not a valid number"  # This can be altered to fit whatever the code needs


# Gravity function for calculation
def gravity(gravities):
    if gravities == "Earth":
        return 9.81
    elif gravities == "Moon":
        return 1.62
    elif gravities == "Mars":
        return 3.711
    elif gravities == "Jupiter":
        return 24.79
    elif gravities == "Saturn":
        return 10.44


def projectile_calc(height, initial_velocity, angle, gravity):
    angle_float = float(angle)
    angle_rad = math.radians(angle_float)  # converts angle to radians
    Ux = float(initial_velocity * math.cos(angle_rad))  # finds the horizontal component of velocity
    Uy = float(initial_velocity * math.sin(angle_rad))  # finds the vertical component of velocity
    g = gravity
    height = float(height)
    if height == 0:  # for when height = 0 then
        A = float(0 - g)  # for obvious reasons
        t = (2 * Uy) / g  # basic equation for time
        t_max_height = Uy / g
        x = Ux * t  # horizontal displacement
        y = Uy * t - 0.5 * g * (t ** 2)  # vertical displacement
        Y_max = Uy * t_max_height - (g * t_max_height ** 2) / 2  # vertical distance from ground
        Vx = Ux  # initial velocity in x is the same as final velocity in x for obvious reasons
        Vy = Uy + (A * t)  # equation for velocity component in y
        V = math.sqrt((Vx ** 2) + (Vy ** 2))  # magnitude of final velocity
        S = (initial_velocity * t) + (0.5 * A * t ** 2)  # equation for distance
        return [t, V, x, Y_max]  # this returns the values as a list
    elif height > 0:
        A = float(0 - g)
        t = (Uy + math.sqrt((Uy ** 2) + 2 * g * height)) / g  # equation for time taking height into account
        t_max_height = Uy / g
        x = Ux * t  # horizontal displacement / also for this case the range
        y = Uy * t - 0.5 * g * (t ** 2)  # vertical displacement
        Y_max = height + (Uy * t_max_height - (g * t_max_height ** 2) / 2)  # max vertical displacement from ground
        Vx = Ux
        Vy = Uy - (g * t)  # equation for velocity component in y
        V = math.sqrt((Vx ** 2) + (Vy ** 2))  # magnitude of final velocity
        S = (initial_velocity * t) + (0.5 * A * t ** 2)  # equation for distance,
        # ^ not too sure if this works for projectiles with height greater than 0
        return [t, V, x, Y_max]  # this returns the values as a list



def calculator():
    plt.close('all')
    gravInput = InitialGravity.get()
    VelInput = InitialVelocityInput.get()
    AngInput = AngleInput.get()
    HgtInput = InitialHeightInput.get()
    if isinstance(checker(VelInput, min=0), float) and isinstance(checker(AngInput, min=0, max=90),
                                                                  float) and isinstance(
            checker(HgtInput, min=0), float):

        VelInput = checker(VelInput, min=0)
        AngInput = checker(AngInput, min=0, max=90)
        HgtInput = checker(HgtInput, min=0)
        gravInput = gravity(gravInput)

        values = projectile_calc(HgtInput, VelInput, AngInput, gravInput)
        Inputs = [HgtInput, VelInput, AngInput, gravInput] 

        time = values[0]
        final_speed = values[1]
        range = values[2]
        max_height = values[3]

        Outputs = [time, final_speed, range, max_height]

        time_text["text"] = str(round(Outputs[0], 3)) + " s"
        final_speed_text["text"] = str(round(Outputs[1], 3)) + " m/s"
        horizontal_displacement_text["text"] = str(round(Outputs[2], 3)) + " m"
        max_vertical_displacement["text"] = str(round(Outputs[3], 3)) + " m"
        
        
        x_list = assign_xy_to_list(1, "x", Inputs, Outputs)
        y_list = assign_xy_to_list(1, "y", Inputs, Outputs)
        #print(x_list)
        #print(y_list)
        plotgraph(x_list,y_list)


    else:
        OutputError = "The following input(s) are invalid:\n"
        if isinstance(checker(VelInput, min=0), str):
            OutputError = OutputError + "Initial Velocity. " + checker(VelInput, min=0) + "\n"
        if isinstance(checker(AngInput, min=0, max=90), str):
            OutputError = OutputError + "Initial Angle. " + checker(AngInput, min=0, max=90) + " degrees\n"
        if isinstance(checker(HgtInput, min=0), str):
            OutputError = OutputError + "Initial Height. " + checker(HgtInput, min=0) + "\n"
        tkMessageBox.showerror("Invalid Values", OutputError)


root = Tkinter.Tk()  # root is home, base or main
root.wm_title("Computer Applications Team 8: Projectiles")  # root/main window title
root.geometry("500x300")  # seemingly dimensions for main window

# separators are used for each window / section

# ------------Introduction------------
def introwin():  # introduction window
    introwin = Tkinter.Tk()
    introwin.wm_title("Introduction")

    # below \n is used in text. This makes a new line. Two can be as a line spacer
    lblIntro = Tkinter.Label(introwin,
                             text="To investigate the trajectory of a projectile we will apply the \n equations of motion under constant acceleration.The problem is \n two-dimensional, because a projectile is free to move both \n vertically and in a horizontal direction.")
    lblIntro.pack()  # above is label text for introduction, pack is to place it

    def kill():  # to close the individual window
        introwin.destroy()  # for some reason needed an indent here

    kill = Tkinter.Button(introwin, text="Close", command=kill)  # close button
    kill.pack()  # placing close button


# ------------Visualiser------------



# ------------Help------------

def helpwin():  # help window
    helpwin = Tkinter.Tk()
    helpwin.wm_title("Help")  # title bar

    lblHelp = Tkinter.Label(helpwin,
                            text="To navigate between pages, use the buttons at the top of each page. \n \n Read the introduction to understand the theory behind projectiles. \n \n Proceed to the calculator and input variables where a chart will display\n it's trajectory. \n \n When on the calculator inputs, the alter the values in the text \n boxes to alter the Initial Velocity, Initial Angle and Initial Height variables. \n \n Use the Combo box to select which celestial body’s gravity to use with \n the simulation. \n \n Once the values are selected, press the Calculate button to view the \n output parameters and graph.")
    lblHelp.pack()  # placing text from above

    def kill():
        helpwin.destroy()  # close help

    kill = Tkinter.Button(helpwin, text="Close", command=kill)  # close button
    kill.pack()  # its placement


intro = Tkinter.Button(root, text="Introduction", command=introwin)  # introduction button link
helper = Tkinter.Button(root, text="Help", command=helpwin)  # button called helper since help had a conflict

# for input values
inputs_header = Tkinter.Label(root, text=('INPUTS:'))
InitialVelocityText = Tkinter.Label(root, text="Initial Velocity (m/s): ")
AngleText = Tkinter.Label(root, text="Initial Angle  (degrees°): ")
InitialHeightText = Tkinter.Label(root, text="Initial Height (m): ")
GravityText = Tkinter.Label(root, text="Gravity (m/s²)")

# keep
ptoe = Tkinter.Button(root, text="Calculate", command=calculator)  # Calculate button
# keep end

global InitialVelocityInput
global AngleInput
global InitialHeightInput
global GravityInput
global InitialGravity
global Outputs
Outputs = [0, 0, 0, 0]

InitialVelocityInput = Tkinter.Entry(root)
AngleInput = Tkinter.Entry(root)
InitialHeightInput = Tkinter.Entry(root)

InitialGravity = Tkinter.StringVar(root)
InitialGravity.set("Earth")
GravityInput = Tkinter.OptionMenu(root, InitialGravity, *GravityList)

# try:
#     calculate = calculator()
# except TypeError :
#     break

# for output values
output_header = Tkinter.Label(root, text=('OUTPUTS:'))
time_text_base = Tkinter.Label(root, text=('Total Time: '))
final_speed_text_base = Tkinter.Label(root, text=('Final Speed: '))
horizontal_displacement_text_base = Tkinter.Label(root, text=('Distance Travelled: '))
max_vertical_displacement_base = Tkinter.Label(root, text=('Max Height: '))

time_text = Tkinter.Label(root, text="")
final_speed_text = Tkinter.Label(root, text="")
horizontal_displacement_text = Tkinter.Label(root, text="")
max_vertical_displacement = Tkinter.Label(root, text="")

time_text.place(x=200, y=200)
final_speed_text.place(x=200, y=220)
horizontal_displacement_text.place(x=200, y=240)
max_vertical_displacement.place(x=200, y=260)

# Places all the labels and and entries
inputs_header.place(x=5, y=80)
output_header.place(x=5, y=180)
InitialVelocityText.place(x=100, y=100)
InitialVelocityInput.place(x=230, y=100)
AngleText.place(x=100, y=120)
AngleInput.place(x=230, y=120)
InitialHeightText.place(x=100, y=140)
InitialHeightInput.place(x=230, y=140)
time_text_base.place(x=100, y=200)
final_speed_text_base.place(x=100, y=220)
horizontal_displacement_text_base.place(x=100, y=240)
max_vertical_displacement_base.place(x=100, y=260)

GravityText.place(x=5, y=100)
GravityInput.place(x=10, y=120)

ptoe.place(x=260, y=160)
# End of placing labels and entries


# Calculator end >>>>>>>>>>>>>>>>>>>>>>>>>>

intro.place(x=1, y=1)  # place intro button at the top
helper.place(x=90, y=1)

root.mainloop()  # Lets go!


