from tkinter import *
from PIL import *
from customtkinter import *
# set colours
bg_colour = '#3652AD'
# the first frame 
def load_frame1():
	page1_start.tkraise()
	page1_start.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
	page1_start.columnconfigure((0,1,2,3,4,5),weight=1)
	ramka=CTkFrame(page1_start, width=1600, height=1000,corner_radius=10,fg_color='#FFEAA7')
	#ramka.place(relx=0.5,rely=0.5, anchor=CENTER)
	#ramka.place(x=150,y=100)
	#ramka.grid(row=1, rowspan=6, column=1, columnspan=4)
	ramka.grid(row=1, rowspan=7, column=1, columnspan=4, sticky="nsew")
	info_wr= CTkLabel(ramka,text="Wybierz rozgrywkę",fg_color='white', font=('Arial',26),corner_radius=32 )
	info_wr.grid(row=2,column=2,columnspan=2,ipadx=100, ipady=20)

	wybor_cr= CTkButton(ramka, text="Czas reakcji",  command=load_frame2, font=('Arial',20),corner_radius=32) 
	wybor_cr.grid(row=3, column=1,columnspan=2,ipadx=170, ipady=40)
	wybor_tr=CTkButton(ramka,text="Trening pamięci",command=load_frame3,font=('Arial',20),corner_radius=32)
	wybor_tr.grid(row=3,column=3,columnspan=2,ipadx=170, ipady=40)
	wybor_ka= CTkButton(ramka, text="Kolejność matematyczna",command=load_frame3, font=('Arial',20),corner_radius=32)
	wybor_ka.grid(row=5, column=1,columnspan=2,ipadx=100, ipady=40)
	wybor_rm= CTkButton(ramka, text="Równanie matemtyczne",command=load_frame3, font=('Arial',20),corner_radius=32)
	wybor_rm.grid(row=5, column=3,columnspan=2,ipadx=120, ipady=40)


def load_frame2():
	page2_.tkraise()

def load_frame3():
	page3_.tkraise()
	
# initiallize app with basic settings
root = CTk()
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
