from tkinter import *
from PIL import *

# set colours
bg_colour = 'navy' #"#3d6466"

# the first frame 
def load_frame1():
	page1_start.tkraise()
	page1_start.rowconfigure((0,1,2,3,4),weight=1)
	page1_start.columnconfigure((0,1,2,3,4),weight=1)
	wybor_cs= Button(page1_start, text="Czas reakcji",command=load_frame2)
	wybor_cs.grid(row=1, column=1,padx=40,pady=(0,40), sticky='ew')

def load_frame2():
	page2_.tkraise()

# initiallize app with basic settings
root = Tk()
root.title("Ćwiczenia")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.resizable(0,0)
root.option_add('*Font', 'Arial 12')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.tk_setPalette(background='white')


# create a frame widgets
page1_start = Frame(root, width=500, height=600, bg=bg_colour)
page2_ = Frame(root, bg=bg_colour)

# place frame widgets in window
for frame in (page1_start, page2_):
	frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame1()
####
root.mainloop()
