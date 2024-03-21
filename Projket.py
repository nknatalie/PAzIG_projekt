from tkinter import *
from PIL import *
from customtkinter import *
import random
import time
import timer

# set colours
bg_colour = '#3652AD'
# the first frame 
def load_frame1():
	page1_start.tkraise()
	ramka_start=CTkFrame(page1_start, corner_radius=10,fg_color='#FFEAA7')
	ramka_start.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

	info_WybierzRozgrywke= CTkLabel(ramka_start,text="Wybierz rozgrywkę",fg_color='white', font=('Arial',60),corner_radius=32,width=250, height=75)
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
		if poziom_trudnosci !=0:
			if cwiczenie == "czasu reakcji":
				load_frame3(poziom_trudnosci)
			elif cwiczenie == "treningu pamięci":
				load_frame4(poziom_trudnosci)
			elif cwiczenie == "kolejności alfabetycznej":
				load_frame5(poziom_trudnosci)
			elif cwiczenie == "równania matematycznego":
				load_frame6(poziom_trudnosci)
		else:
			komunikat_brak_wyboru.place(relx=0.5,rely=0.15, anchor='n')

	page2_trudnosc.tkraise()
	info_wyborpoziomu=CTkLabel(page2_trudnosc,text=f'Wybierz poziom trudności dla {cwiczenie}',fg_color='white', font=('Arial',60),corner_radius=32,width=250, height=75 )
	info_wyborpoziomu.place(relx=0.5,rely=0.05,anchor='n')
	radio_var_poziom=IntVar()
	rb_latwy=CTkRadioButton(page2_trudnosc, text="Łatwy", font=('Arial',45,'bold'),value=1,variable=radio_var_poziom)
	rb_latwy.place(relx=0.15, rely=0.60,anchor='w')
	rb_sredni=CTkRadioButton(page2_trudnosc, text="Średni", font=('Arial',45,'bold'),value=2, variable=radio_var_poziom)
	rb_sredni.place(relx=0.45, rely=0.60,anchor='w')
	rb_trudny=CTkRadioButton(page2_trudnosc, text="Trudny", font=('Arial',45,'bold'),value=3,variable=radio_var_poziom)
	rb_trudny.place(relx=0.80, rely=0.60,anchor='w')

	zatwierdzenie_trudnosci=CTkButton(page2_trudnosc,text='Dalej',font=('Arial',50),corner_radius=32,width=250, height=75, command= dalej)
	zatwierdzenie_trudnosci.place(relx=0.5,rely=0.80,anchor='n')

	komunikat_brak_wyboru=CTkLabel(page2_trudnosc, text="Wybierz poziom trudności!",fg_color='red',font=('Arial',40),corner_radius=32,width=250, height=75)
	komunikat_brak_wyboru.forget()


def load_frame3(poziom_trudnosci):
	page3_CzasReakcji.tkraise()
	info_zapamietajObiekt=CTkLabel(page3_CzasReakcji,text='Zapamiętaj obiekt!',fg_color='white', font=('Arial',60,'bold'),corner_radius=32,width=250, height=75 )
	info_zapamietajObiekt.place(relx=0.5,rely=0.05,anchor='n')
	if poziom_trudnosci==1:
		pass
	elif poziom_trudnosci==2:
		pass
	elif poziom_trudnosci==3:
		pass

def load_frame4(poziom_trudnosci):
	page4_TreningPamieci.tkraise()
	info_zapamietajKolejnosc=CTkLabel(page4_TreningPamieci,text='Zapamiętaj kolejność!',fg_color='white', font=('Arial',60,'bold'),corner_radius=32,width=250, height=75 ) 
	info_zapamietajKolejnosc.place(relx=0.5,rely=0.05,anchor='n')
	if poziom_trudnosci==1:
		pass
	elif poziom_trudnosci==2:
		pass
	elif poziom_trudnosci==3:
		pass

def load_frame5(poziom_trudnosci):
	page5_KolejnoscAlfabetyczna.tkraise()
	if poziom_trudnosci==1:
		pass
	elif poziom_trudnosci==2:
		pass
	elif poziom_trudnosci==3:
		pass

def load_frame6(poziom_trudnosci):
	page6_RownaniaMatematyczne.tkraise()
	info_rozwiazRownanie=CTkLabel(page6_RownaniaMatematyczne,text='Rozwiąż równanie!',fg_color='white', font=('Arial',60,'bold'),corner_radius=32,width=250, height=75 )
	info_rozwiazRownanie.place(relx=0.5,rely=0.05,anchor='n')

	liczba_rund=5 if poziom_trudnosci==1 else  7 if poziom_trudnosci==2 else 10 

	if poziom_trudnosci==1:
		liczby =[random.randint(1,10) for _ in range(3)]
		operatory=[random.choice(["+","-"]) for _ in range(2)]
	elif poziom_trudnosci==2:
		liczby =[random.randint(1,10) for _ in range(3)]
		operatory=[random.choice(["+","-","*"]) for _ in range(2)]
	elif poziom_trudnosci==3:
		liczby =[random.randint(1,10) for _ in range(5)]
		operatory=[random.choice(["+","-","*","/"]) for _ in range(3)]

	rownanie = " ".join(str(liczba) + " " + operator for liczba, operator in zip(liczby, operatory)) + str(liczby[-1])  ## CZY WYNIK ROBIMY UJEMNY ??
	wynik=eval(rownanie)

	info_rownanie=CTkLabel(page6_RownaniaMatematyczne,text=rownanie,fg_color='white',font=('Arial',55),corner_radius=10)#,width=250, height=50)
	info_rownanie.place(relx=0.3, rely=0.3,relwidth=0.3,relheight=0.25, anchor='n')

	podaj_Wynik=CTkEntry(page6_RownaniaMatematyczne, font=('Arial',55,'bold'),corner_radius=10)
	podaj_Wynik.place(relx=0.85, rely=0.425,relwidth=0.2,relheight=0.2, anchor='e')


	rownanie = " ".join(str(liczba) + " " + operator for liczba, operator in zip(liczby, operatory)) + str(liczby[-1])  ## CZY WYNIK ROBIMY UJEMNY ??
	wynik=eval(rownanie)

	def sprawdz():
		nonlocal liczba_rund
		wpisany_wynik=podaj_Wynik.get().strip()
		if wpisany_wynik==str(wynik):
			podaj_Wynik.configure(fg_color='green')
			liczba_rund=nastepna_runda(poziom_trudnosci,liczba_rund)
			if liczba_rund>0:
				przycisk_sprawdz_rownanie.configure(text='Dalej')
			else:
				przycisk_sprawdz_rownanie.configure(text='Koniec rund',state='disabled')
		elif wpisany_wynik !='': # kiedy użytkownik nic nie wpisze to nic się nie dzieje
			podaj_Wynik.configure(fg_color='red')
			liczba_rund=nastepna_runda(poziom_trudnosci,liczba_rund)
			#podaj_Wynik.configure(state='disabled') # czy chcemy tak robić?
			if liczba_rund>0:
				przycisk_sprawdz_rownanie.configure(text='Dalej')
				przycisk_sprawdz_rownanie.configure(text='Koniec rund',state='disabled')

	def nastepna_runda(poziom_trudnosci,liczba_rund):
		nonlocal liczby,operatory,rownanie,wynik
		if liczba_rund >0:
			liczba_rund -=1
			if poziom_trudnosci==1:
				liczby =[random.randint(1,10) for _ in range(3)]
				operatory=[random.choice(["+","-"]) for _ in range(2)]
			elif poziom_trudnosci==2:
				liczby =[random.randint(1,10) for _ in range(3)]
				operatory=[random.choice(["+","-","*"]) for _ in range(2)]
			elif poziom_trudnosci==3:
				liczby =[random.randint(1,10) for _ in range(5)]
				operatory=[random.choice(["+","-","*","/"]) for _ in range(3)]
			
			rownanie = " ".join(str(liczba) + " " + operator for liczba, operator in zip(liczby, operatory)) + str(liczby[-1])  ## CZY WYNIK ROBIMY UJEMNY ??
			wynik=eval(rownanie)
			info_rownanie.configure(text=rownanie)
			podaj_Wynik.delete(0,'end')
			podaj_Wynik.configure(fg_color='white')
			przycisk_sprawdz_rownanie.configure(text='Sprawdź', command=sprawdz)
		return liczba_rund


	przycisk_sprawdz_rownanie=CTkButton(page6_RownaniaMatematyczne, text='Sprawdź',font=('Arial',60,'bold'),corner_radius=32,width=250, height=75, command=sprawdz)
	przycisk_sprawdz_rownanie.place(relx=0.5, rely=0.85, anchor='s')




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
