# -*- coding: utf-8 -*-
try: #for working with both python 3 and 2.7 since libraries are different
    import tkinter as tk # python 3
    from tkinter import font as tkfont
except ImportError: # python 2
    import Tkinter as tk
    import tkFont as tkfont #so we can use fonts

class main(tk.Tk): #class for main window, this one has pages, this is the container
    #  help page not included.
    def __init__(self, *args, **kwargs): #create buttons,entries,etc especially for __init__
        tk.Tk.__init__(self, *args, **kwargs)#using args kwargs magic
        tk.Tk.wm_title(self, "Computer Applications Team 8: Projectiles")#main window title
        self.title_font = tkfont.Font(family='Helvetica', size=12, weight="normal")#, slant="italic") -- temp cut

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others, to simulate page turning/ page replace.
        # We dont want to open a new window for intro to visualiser page
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)#grid positions entities
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}# frames 
        for F in (StartPage, PageOne):#frames for loop
            page_name = F.__name__
            frame = F(parent=container, root=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise() #raise each frame above the other


class StartPage(tk.Frame): #----------------introduction page---------------

    def __init__(self, parent, root):
        tk.Frame.__init__(self, parent)
        self.root = root 
        self.root.geometry("700x350+500+200") #seemingly dimensions for main window
        
        label = tk.Label(self, text="Introduction", font= "Helvetica 18 bold") # Introduction text
        label.pack(side="top", fill="x", pady=10) #Introduction placement

        label2 = tk.Label(self, text="To investigate the trajectory of aprojectile we will apply the equations of \n motion underconstant acceleration.The problem is two-dimensional, because a \n projectile is free to move both vertically and in a horizontal direction.", font=root.title_font) 
        label2.pack(side="top", fill="x", pady=10)

        #comp1 = tk.PhotoImage(root, file="comp1.png")   failed attempt at an image import
        #label3 = tk.label(image=comp1)
        #label3.pack()#side="top", fill="x", pady=10)
        
       # label3 = tk.Label(self, text="", font=root.title_font)    # was a method of importing comp1 image
       # label3.pack(side="top", fill="x", pady=10)

        label3 = tk.Label(self, text="Consider a cannon-ball emerging from the muzzle of a cannon with a velocity V. \n The barrel of the cannon is inclined at an angle θ to the horizontal. \n It follows that the horizontal component of the velocity is", font=root.title_font)
        label3.pack(side="top", fill="x", pady=10)
        
        button1 = tk.Button(self, text="Proceed to Calculator and Visualiser",#Calculator and Visualiser button on intro page
                            command=lambda: root.show_frame("PageOne"))                 
        button1.pack(side="bottom")#location


class PageOne(tk.Frame): #--------------- visualiser page ----------------

    def __init__(self, parent, root):
        tk.Frame.__init__(self, parent)
        self.root = root
        label = tk.Label(self, text="Calculator and Visualiser", font= "Helvetica 18 bold") # Calculator and Visualiser text
        label.pack(side="top", fill="x", pady=10) #Calculator and Visualiser placement

        # entry not showing
        
        canvas1 = tk.Canvas(self)
        canvas1.pack()
        
        # Combobox pain
   # def grav_changed(event):
        
        #msg = f'You selected {grav_cb.get()}!'
        #showinfo(title='Result', message=msg)

        #grav for gravity
        # array
      #  gravs = ('Earth', 'Moon', 'Venus', 'Mars', 'Jupiter', 'Titan')

       # label = ttk.Label(text="Please select a gravity value:")
       # label.pack(fill='x', padx=5, pady=5)

        # create a combobox
       # selected_grav = tk.StringVar()

     #   grav_cb = ttk.Combobox(root, textvariable=selected_grav)
     #   grav_cb['values'] = gravs
     #   grav_cb['state'] = 'readonly'  # normal
     #   grav_cb.pack(fill='x', padx=5, pady=5)

     #   grav_cb.bind('<<ComboboxSelected>>', grav_changed)

        #combo end
        
        button = tk.Button(self, text="Back",
                           command=lambda: root.show_frame("StartPage"))
        button.pack(side="bottom")
        self.frame = tk.Frame(self.root)
        self.button1 = tk.Button(self.frame, text = 'Help', width = 5, command = self.new_window)
        self.button1.pack(side="top")
        self.frame.pack()
    def new_window(self):
        self.newwindow = tk.Toplevel(self.root)
        self.app = helpapp(self.newwindow)

class helpapp: # ----------------help window-------------------

    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.geometry("300x300+500+200")
        #self.label = tk.Label(self, text="Help", font= "Helvetica 18 bold") # help title text
        #self.label.pack(side="top", fill="x", pady=10) #help placement
        self.quitButton = tk.Button(self.frame, text = 'Close', width = 5, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.root.destroy()


if __name__ == "__main__":
    app = main()
    app.mainloop()
