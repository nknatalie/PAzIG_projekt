from tkinter import *
from PIL import *
from customtkinter import *
# set colours
bg_colour = '#3652AD'
# the first frame 
def load_frame1():
	page1_start.tkraise()
	ramka=CTkFrame(page1_start, corner_radius=10,fg_color='#FFEAA7')
	ramka.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

	info_wr= CTkLabel(ramka,text="Wybierz rozgrywkę",fg_color='white', font=('Arial',40),corner_radius=32,width=250, height=75)
	info_wr.place(relx=0.5,rely=0.05,anchor='n')
	wybor_cr= CTkButton(ramka, text="Czas reakcji",  command=load_frame2, font=('Arial',30),corner_radius=32,width=300, height=100) 
	wybor_cr.place(relx=0.15,rely=0.35,anchor='w')

	wybor_tr=CTkButton(ramka,text="Trening pamięci",command=load_frame3,font=('Arial',30),corner_radius=32,width=300, height=100)
	wybor_tr.place(relx=0.65, rely=0.35, anchor='w')

	wybor_ka= CTkButton(ramka, text="Kolejność matematyczna",command=load_frame4, font=('Arial',30),corner_radius=32,width=300, height=100)
	wybor_ka.place(relx=0.25, rely=0.755, anchor='s')

	wybor_rm= CTkButton(ramka, text="Równanie matemtyczne",command=load_frame5, font=('Arial',30),corner_radius=32,width=300, height=100)
	wybor_rm.place(relx=0.85, rely=0.70, anchor='e')


def load_frame2():
	page2_.tkraise()

def load_frame3():
	page3_.tkraise()

def load_frame4():
	page4_.tkraise()

def load_frame5():
	page5_.tkraise()
	
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
page4_ = Frame(root, bg=bg_colour)
page5_ = Frame(root, bg=bg_colour)

# place frame widgets in window
for frame in (page1_start, page2_,page3_,page4_,page5_):
	frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame1()
####
root.mainloop()
