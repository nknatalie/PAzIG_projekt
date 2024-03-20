from tkinter import *
from PIL import *
from customtkinter import *
# set colours
bg_colour = '#3652AD'
# the first frame 
def load_frame1():
	page1_start.tkraise()
	ramka_start=CTkFrame(page1_start, corner_radius=10,fg_color='#FFEAA7')
	ramka_start.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

	info_WybierzRozgrywke= CTkLabel(ramka_start,text="Wybierz rozgrywkę",fg_color='white', font=('Arial',40),corner_radius=32,width=250, height=75)
	info_WybierzRozgrywke.place(relx=0.5,rely=0.05,anchor='n')

	wybor_CzasReakcji= CTkButton(ramka_start, text="Czas reakcji",  command=lambda: load_frame2("czasu reakcji"), font=('Arial',30),corner_radius=32,width=300, height=100) 
	wybor_CzasReakcji.place(relx=0.15,rely=0.35,anchor='w')

	wybor_TreningPamieci=CTkButton(ramka_start,text="Trening pamięci",command= lambda: load_frame2("treningu pamięci"),font=('Arial',30),corner_radius=32,width=300, height=100)
	wybor_TreningPamieci.place(relx=0.65, rely=0.35, anchor='w')

	wybor_KolejnoscMatematyczna= CTkButton(ramka_start, text="Kolejność alfabetyczna",command=lambda:load_frame2("kolejności alfabetycznej"), font=('Arial',30),corner_radius=32,width=300, height=100)
	wybor_KolejnoscMatematyczna.place(relx=0.25, rely=0.755, anchor='s')

	wybor_RownanieMatematyczne= CTkButton(ramka_start, text="Równanie matematyczne",command=lambda:load_frame2("równania matematycznego"), font=('Arial',30),corner_radius=32,width=300, height=100)
	wybor_RownanieMatematyczne.place(relx=0.85, rely=0.70, anchor='e')


def load_frame2(cwiczenie):
	def dalej():
		poziom_trudnosci=radio_var_poziom.get()	
		if cwiczenie == "czasu reakcji":
			if poziom_trudnosci==1:
				load_frame3()
			elif poziom_trudnosci==2:
				pass
			elif poziom_trudnosci==3:
				pass
		elif cwiczenie == "treningu pamięci":
			if poziom_trudnosci==1:
				load_frame4()
			elif poziom_trudnosci==2:
				pass
			elif poziom_trudnosci==3:
				pass
		elif cwiczenie == "kolejności alfabetycznej":
			if poziom_trudnosci==1:
				load_frame5()
			elif poziom_trudnosci==2:
				pass
			elif poziom_trudnosci==3:
				pass
		elif cwiczenie == "równania matematycznego":
			if poziom_trudnosci==1:
				load_frame6()
			elif poziom_trudnosci==2:
				pass
			elif poziom_trudnosci==3:
				pass	
	page2_trudnosc.tkraise()
	info_wyborpoziomu=CTkLabel(page2_trudnosc,text=f'Wybierz poziom trudności dla {cwiczenie}',fg_color='white', font=('Arial',40),corner_radius=32,width=250, height=75 )
	info_wyborpoziomu.place(relx=0.5,rely=0.05,anchor='n')
	radio_var_poziom=IntVar()
	rb_latwy=CTkRadioButton(page2_trudnosc, text="Łatwy", font=('Arial',40,'bold'),value=1,variable=radio_var_poziom)
	rb_latwy.place(relx=0.15, rely=0.60,anchor='w')
	rb_sredni=CTkRadioButton(page2_trudnosc, text="Średni", font=('Arial',40,'bold'),value=2, variable=radio_var_poziom)
	rb_sredni.place(relx=0.45, rely=0.60,anchor='w')
	rb_trudny=CTkRadioButton(page2_trudnosc, text="Trudny", font=('Arial',40,'bold'),value=3,variable=radio_var_poziom)
	rb_trudny.place(relx=0.80, rely=0.60,anchor='w')

	zatwierdzenie_trudnosci=CTkButton(page2_trudnosc,text='Dalej',font=('Arial',40),corner_radius=32,width=250, height=75, command= dalej)
	zatwierdzenie_trudnosci.place(relx=0.5,rely=0.80,anchor='n')


def load_frame3():
	page3_CzasReakcji.tkraise()

def load_frame4():
	page4_TreningPamieci.tkraise()

def load_frame5():
	page5_KolejnoscAlfabetyczna.tkraise()

def load_frame6():
	page6_RownaniaMatematyczne.tkraise()

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
page2_trudnosc = Frame(root, bg=bg_colour)
page3_CzasReakcji = Frame(root, bg=bg_colour)
page4_TreningPamieci = Frame(root, bg=bg_colour)
page5_KolejnoscAlfabetyczna= Frame(root, bg=bg_colour)
page6_RownaniaMatematyczne=Frame(root,bg=bg_colour)

# place frame widgets in window
for frame in (page1_start, page2_trudnosc,page3_CzasReakcji,page4_TreningPamieci,page5_KolejnoscAlfabetyczna,page6_RownaniaMatematyczne):
	frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame1()
####
root.mainloop()
