from tkinter import *
from PIL import *
from tkinter import ttk

# set colours
bg_colour = 'navy' #"#3d6466"

# the first frame 
def load_frame1():
	page1_start.tkraise()
	page1_start.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
	page1_start.columnconfigure((0,1,2,3,4,5),weight=1)
	ramka=Frame(page1_start, bg='blue', width=1600, height=800)
	#ramka.place(x=150,y=100)
	ramka.grid(row=1, rowspan=6, column=1, columnspan=4)
	info_wr= Label(page1_start,text="Wybierz rozgrywkę",fg='black',bg='white')
	info_wr.grid(row=2,column=2,columnspan=2,padx=20,pady=40, sticky='ew')

	wybor_cr= Button(page1_start, text="Czas reakcji",command=load_frame2,fg='white',bg='navy') # czy chcemy zaokrąglone rogi?
	wybor_cr.grid(row=3, column=1,columnspan=2,ipadx=100, ipady=40)
	wybor_tr=Button(page1_start,text="Trening pamięci",command=load_frame3,fg='white',bg='navy')
	wybor_tr.grid(row=3,column=4,padx=20,pady=40, sticky='ew')
	wybor_ka= Button(page1_start, text="Kolejność matematyczna",command=load_frame3, fg='white',bg='navy' )
	wybor_ka.grid(row=5, column=1,padx=20,pady=40, sticky='ew')
	wybor_rm= Button(page1_start, text="Równanie matemtyczne",command=load_frame3, fg='white',bg='navy' )
	wybor_rm.grid(row=5, column=4,padx=20,pady=40, sticky='ew')


def load_frame2():
	page2_.tkraise()

def load_frame3():
	page3_.tkraise()
	
# initiallize app with basic settings
root = Tk()
root.title("Ćwiczenia")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.resizable(1,1)
root.option_add('*Font', 'Arial 20')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# create a frame widgets
page1_start = Frame(root, bg=bg_colour) # width=500, height=600,
page2_ = Frame(root, bg=bg_colour)
page3_ = Frame(root, bg=bg_colour)

# place frame widgets in window
for frame in (page1_start, page2_,page3_):
	frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame1()
####
root.mainloop()
