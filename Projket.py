from tkinter import *
from PIL import *

# set colours
bg_colour = "#3d6466"


def load_frame1():
	frame1.tkraise()
	wybierz_gre= Button(frame1, text="cos")
	wybierz_gre.grid(row=0, column=0)

# initiallize app with basic settings
root = Tk()
root.title("Recipe Picker")
#root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))
 
# create a frame widgets
frame1 = Frame(root, width=500, height=600, bg=bg_colour)
frame2 = Frame(root, bg=bg_colour)

# place frame widgets in window
for frame in (frame1, frame2):
	frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame1()

root.mainloop()
