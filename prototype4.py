# -*- coding: utf-8 -*-
import Tkinter #python 2.7 formatting
import tkMessageBox #message box tool
from decimal import Decimal # for maths

root = Tkinter.Tk() # root is home, base or main
root.wm_title("Computer Applications Team 8: Projectiles") #root/main window title 
root.geometry("350x70+350+70") #seemingly dimensions for main window

# separators are used for each window / section

#------------Introduction------------
def introwin(): #introduction window
    introwin = Tkinter.Tk()
    introwin.wm_title("Introduction")

    
     #below \n is used in text. This makes a new line. Two can be as a line spacer
    lblIntro = Tkinter.Label(introwin, text = "To investigate the trajectory of aprojectile we will apply the \n equations of motion underconstant acceleration.The problem is \n two-dimensional, because a projectile is free to move both \n vertically and in a horizontal direction.")
    lblIntro.pack() #above is label text for introduction, pack is to place it 

    def kill():# to close the individual window
        introwin.destroy() # for some reason needed an indent here

    kill = Tkinter.Button(introwin, text="Close", command = kill)# close button
    kill.pack() #placing close button

#------------Visualiser------------

def visualwin(): # calculator and visualiser window
    visualwin = Tkinter.Tk()
    visualwin.wm_title("Calculator and Visualiser")


     # Example visualiser start <<<<<<<<<<<<<<<<<<<<<<<


    def draw():

        c.delete('all')

        x=width.get()*4
        y=length.get()*4

        c.create_rectangle(x,y,0,0, fill='#000000')
        visualwin.after(10,draw)

    

    def calctemp():

        variable1=length.get()
        variable2=width.get()
    
        size = variable1*variable2

        variable3 = size*1850

        variable4 = variable3/2

        Q = variable4
        m = float(Q)/(float(335200))

        tkMessageBox.showinfo("Results", "You can boil " + str(m) +" Litres of room temperature water per minute.")
  
    #keep
    def kill(): #closes window
        visualwin.destroy()
    #keep end

    c = Tkinter.Canvas(visualwin, width=200, height=200)

    length = Tkinter.Scale(visualwin, from_=50, to=0)
    width = Tkinter.Scale(visualwin, from_=0, to=50, orient = Tkinter.HORIZONTAL)

    #keep
    ptoe  = Tkinter.Button(visualwin, text="Calculate", command = calctemp) # Close window button
    kill = Tkinter.Button(visualwin, text="Close", command = kill) # Places close button
    #keep end
    
    length.grid(row=2, column = 2)
    width.grid(row=3, column = 3)
    ptoe.grid(row=4, column = 3)
    c.grid(row=2, column = 3)
    kill.grid(row=5, column = 3)

    visualwin.after(10, draw)

# Example visualiser end >>>>>>>>>>>>>>>>>>>>>>>>>>

#------------Help------------

def helpwin(): # help window
    helpwin = Tkinter.Tk()
    helpwin.wm_title("Help") #title bar

    lblHelp = Tkinter.Label(helpwin, text = "To navigate between pages, use the buttons on the bottom of each page. \n \n Read the introduction to understand the theory behind projectiles. \n \n Proceed to the Calculator and visualiser page to input variables and see \n changes to the chart realtime. \n \n When on the Calculator and Visualiser page, input values into the text \n boxes to to alter the Initial Vellocity and Initial Angle variables. \n \n Use the Combo box to select which celestial body’s gravity to use with \n the simulation. \n \n Once the values are selected, press the Calculate button to view the \n equation and graph, \n 'n Press back on thie Calculator and Visualiser page to return \n to the introduction page. There you can read the theory behind projectiles.")
    lblHelp.pack() #placing text from above

    def kill():
        helpwin.destroy()#close help

    kill = Tkinter.Button(helpwin, text="Close", command = kill)# close button
    kill.pack() # its placement

    

intro = Tkinter.Button(root, text = "Introduction", command = introwin)# introduction button link
visualiser = Tkinter.Button(root, text = "Calculator and Visualiser", command = visualwin) # etc
helper = Tkinter.Button(root, text = "Help", command = helpwin) # button called helper since help had a conflict

intro.pack() #place intro button at the top
visualiser.pack() # etc
helper.pack() 

root.mainloop()# Lets go!
