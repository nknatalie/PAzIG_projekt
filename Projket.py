from tkinter import *
from PIL import *

# set colours
bg_colour = 'white' #"#3d6466"

# the first frame 
def load_frame1():
	page1_open.tkraise()
	page1_open.rowconfigure(0,weight=1)
	page1_open.columnconfigure(0,weight=1)
	wybierz_gre= Button(page1_open, text="cos")
	wybierz_gre.grid(row=0, column=0)


# initiallize app with basic settings
root = Tk()
root.title("Recipe Picker")
#root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))
root.resizable(1,1)
root.option_add('*Font', 'Arial 12')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.tk_setPalette(background='white')


# create a frame widgets
page1_open = Frame(root, width=500, height=600, bg=bg_colour)
page2_ = Frame(root, bg=bg_colour)

# place frame widgets in window
for frame in (page1_open, page2_):
	frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame1()

root.mainloop()
