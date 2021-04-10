# -*- coding: utf-8 -*-
import Tkinter  # python 2.7 formatting
import tkMessageBox  # message box tool
from decimal import Decimal  # for maths
import math

GravityList = ["Earth", "Moon", "Mars", "Jupiter", "Saturn"]

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
        returnval = "Outside range - Less than " + str(min)  # This can be altered to fit whatever the code needs
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

#Gravity function for calculation
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
        t = (2 * Uy)/g  # basic equation for time 
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
  gravInput = InitialGravity.get()
  VelInput = InitialVelocityInput.get()
  AngInput = AngleInput.get()
  HgtInput = InitialHeightInput.get()
  if isinstance(checker(VelInput, min=0), float) and isinstance(checker(AngInput, min=0, max=90), float) and isinstance(
          checker(HgtInput, min=0), float):

    VelInput = checker(VelInput, min=0)
    AngInput = checker(AngInput, min=0, max=90)
    HgtInput = checker(HgtInput, min=0)
    gravInput = gravity(gravInput)
    
    Outputs = projectile_calc(HgtInput, VelInput, AngInput, gravInput)
    tkMessageBox.showinfo("Working", "Time: "+str(Outputs[0]) + "\nFinal Speed: " + str(Outputs[1]) + "\nRange: " + str(Outputs[2]) + "\nMaximum Height: " + str(Outputs[3]) + "\n")

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
root.geometry("350x75+350+70")  # seemingly dimensions for main window


# separators are used for each window / section

# ------------Introduction------------
def introwin():  # introduction window
  introwin = Tkinter.Tk()
  introwin.wm_title("Introduction")

  # below \n is used in text. This makes a new line. Two can be as a line spacer
  lblIntro = Tkinter.Label(introwin,
                           text="To investigate the trajectory of aprojectile we will apply the \n equations of motion underconstant acceleration.The problem is \n two-dimensional, because a projectile is free to move both \n vertically and in a horizontal direction.")
  lblIntro.pack()  # above is label text for introduction, pack is to place it

  def kill():  # to close the individual window
    introwin.destroy()  # for some reason needed an indent here

  kill = Tkinter.Button(introwin, text="Close", command=kill)  # close button
  kill.pack()  # placing close button


# ------------Visualiser------------

def visualwin():  # calculator and visualiser window
  visualwin = Tkinter.Tk()
  visualwin.wm_title("Calculator and Visualiser")

  # Calculator start <<<<<<<<<<<<<<<<<<<<<<<

  # keep
  def kill():  # closes window
    visualwin.destroy()

  # keep end

  InitialVelocityText = Tkinter.Label(visualwin, text="Initial Velocity: ")
  AngleText = Tkinter.Label(visualwin, text="Initial Angle: ")
  InitialHeightText = Tkinter.Label(visualwin, text="Initial Height: ")
  GravityText = Tkinter.Label(visualwin, text="Gravity: ")

  global InitialVelocityInput
  global AngleInput
  global InitialHeightInput
  global GravityInput
  global InitialGravity

  InitialVelocityInput = Tkinter.Entry(visualwin)
  AngleInput = Tkinter.Entry(visualwin)
  InitialHeightInput = Tkinter.Entry(visualwin)

  InitialGravity = Tkinter.StringVar(visualwin)
  InitialGravity.set("Earth")
  GravityInput = Tkinter.OptionMenu(visualwin, InitialGravity, *GravityList)

  # keep
  ptoe = Tkinter.Button(visualwin, text="Calculate", command=calculator)  # Calculate button
  kill = Tkinter.Button(visualwin, text="Close", command=kill)  # Close button
  # keep end

  # Places all the labels and and entries
  InitialVelocityText.grid(row=1, column=1)
  InitialVelocityInput.grid(row=1, column=2)
  AngleText.grid(row=2, column=1)
  AngleInput.grid(row=2, column=2)
  InitialHeightText.grid(row=3, column=1)
  InitialHeightInput.grid(row=3, column=2)

  GravityText.grid(row=4, column=1)
  GravityInput.grid(row=4, column=2)

  ptoe.grid(row=5, column=1)
  kill.grid(row=6, column=1)
  # End of placing labels and entries


# Calculator end >>>>>>>>>>>>>>>>>>>>>>>>>>

# ------------Help------------

def helpwin():  # help window
  helpwin = Tkinter.Tk()
  helpwin.wm_title("Help")  # title bar

  lblHelp = Tkinter.Label(helpwin,
                          text="To navigate between pages, use the buttons on the bottom of each page. \n \n Read the introduction to understand the theory behind projectiles. \n \n Proceed to the Calculator and visualiser page to input variables and see \n changes to the chart realtime. \n \n When on the Calculator and Visualiser page, input values into the text \n boxes to to alter the Initial Vellocity and Initial Angle variables. \n \n Use the Combo box to select which celestial body’s gravity to use with \n the simulation. \n \n Once the values are selected, press the Calculate button to view the \n equation and graph, \n 'n Press back on thie Calculator and Visualiser page to return \n to the introduction page. There you can read the theory behind projectiles.")
  lblHelp.pack()  # placing text from above

  def kill():
    helpwin.destroy()  # close help

  kill = Tkinter.Button(helpwin, text="Close", command=kill)  # close button
  kill.pack()  # its placement


intro = Tkinter.Button(root, text="Introduction", command=introwin)  # introduction button link
visualiser = Tkinter.Button(root, text="Calculator and Visualiser", command=visualwin)  # etc
helper = Tkinter.Button(root, text="Help", command=helpwin)  # button called helper since help had a conflict

intro.pack()  # place intro button at the top
visualiser.pack()  #  etc
helper.pack()

root.mainloop()  # Lets go!

