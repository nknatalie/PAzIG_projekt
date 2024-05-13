from tkinter import *
from PIL import Image, ImageTk
from customtkinter import *
import random
import time
import keyboard
import pyodbc

czasCwiczenia = 0.0

bg_colour = '#285A88'


DRIVER_NAME='SQL SERVER'
SERVER_NAME='DESKTOP-7H7M0GT\SQLEXPRESS'
DARABASE_NAME='Pazig'
# tu można dodac jeszcze USERNAME oraz PASSWORD
connection_string=f"""
	DRIVER={{{DRIVER_NAME}}};
	SERVER={SERVER_NAME};
	DATABASE={DARABASE_NAME};
	Trust_Connection=yes;
"""
conn=pyodbc.connect(connection_string)
cursor=conn.cursor()
print(conn)


def load_frame1():
	page1_start.tkraise()
	ramka_start=CTkFrame(page1_start, corner_radius=10,fg_color='#5E7FA6')
	ramka_start.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

	obrazek_CR = ImageTk.PhotoImage(Image.open(f"wybor\CR.png").resize((100, 100), Image.BILINEAR))
	obrazek_TP = ImageTk.PhotoImage(Image.open(f"wybor\TP.png").resize((100,100), Image.BILINEAR))
	obrazek_KA = ImageTk.PhotoImage(Image.open(f"wybor\KA.png").resize((100,100), Image.BILINEAR))
	obrazek_RM = ImageTk.PhotoImage(Image.open(f"wybor\RM.png").resize((100,100), Image.BILINEAR))

	info_WybierzRozgrywke= CTkLabel(ramka_start,text="Wybierz rozgrywkę",fg_color='white', font=('Arial',60),corner_radius=32,width=250, height=75)
	info_WybierzRozgrywke.place(relx=0.5,rely=0.05,anchor='n')

	wybor_CzasReakcji= CTkButton(ramka_start, text="         Czas reakcji        ",image=obrazek_CR,compound='top', command=lambda: load_frame2("CR"), font=('Arial',30),corner_radius=32,width=300, height=100) 
	wybor_CzasReakcji.place(relx=0.15,rely=0.35,anchor='w')

	wybor_TreningPamieci=CTkButton(ramka_start,text="        Trening pamięci        ",image=obrazek_TP, compound='top', command= lambda: load_frame2("TP"),font=('Arial',30),corner_radius=32,width=300, height=100)
	wybor_TreningPamieci.place(relx=0.85, rely=0.35, anchor='e')

	wybor_KolejnoscAlfabetyczna= CTkButton(ramka_start, text="Kolejność alfabetyczna",image=obrazek_KA,compound='top', command=lambda:load_frame2("KA"), font=('Arial',30),corner_radius=32,width=300, height=100)
	wybor_KolejnoscAlfabetyczna.place(relx=0.15, rely=0.70, anchor='w')

	wybor_RownanieMatematyczne= CTkButton(ramka_start, text="Równanie matematyczne ",image=obrazek_RM,compound='top', command=lambda:load_frame2("RM"), font=('Arial',30),corner_radius=32,width=300, height=100)
	wybor_RownanieMatematyczne.place(relx=0.85, rely=0.70, anchor='e')


def load_frame2(cwiczenie):
	page2_trudnosc.tkraise()

	for widget in page2_trudnosc.winfo_children():
		widget.destroy()	

	def show_info(cwiczenie):
		info_window = CTkToplevel(root)
		info_window.grab_set()
		info_window.title("Informacja")
		info_window.geometry('400x400')
		info_window.resizable(FALSE,FALSE) #width,height
		info_text=CTkLabel(info_window,font=('Arial',60))
		info_text.place(relx=0,rely=0)
		info_file=f'Informacja/{cwiczenie}.txt'
		
		with open(info_file,'r') as file:
			zawartosc=file.read()
			info_text.configure(text=zawartosc)
		
	
	if cwiczenie == 'CR':
		cwiczenia='czasu reakcji'
	elif cwiczenie == 'TP':
		cwiczenia='treningu pamięci'
	elif cwiczenie =='KA':
		cwiczenia='kolejności alfabetycznej'
	elif cwiczenie=='RM':
		cwiczenia="równania matematycznego"


	info_wyborpoziomu=CTkLabel(page2_trudnosc,text=f'Wybierz poziom trudności dla {cwiczenia}',fg_color='white', font=('Arial',60),corner_radius=32,width=250, height=85 )
	info_wyborpoziomu.place(relx=0.5,rely=0.05,anchor='n')
	wroc=ImageTk.PhotoImage(Image.open('zle.png').resize((20,20),Image.BILINEAR))
	button_wro=CTkButton(page2_trudnosc,image=wroc,text='Powrót do startu',command=load_frame1)
	button_wro.place(relx=0.9, rely=0.015)
	info_button=CTkButton(page2_trudnosc,text="Informacja", command=lambda: show_info(cwiczenie))
	info_button.place(relx=0.025,rely=0.025,anchor='w')


	def dalej():
		poziom_trudnosci=radio_var_poziom.get()
		if poziom_trudnosci !=0:
			if cwiczenie == 'CR':#"czasu reakcji":
				load_frame3(poziom_trudnosci)
			elif cwiczenie == 'TP':#"treningu pamięci":
				load_frame4(poziom_trudnosci)
			elif cwiczenie == 'KA':#"kolejności alfabetycznej":
				load_frame5(poziom_trudnosci)
			elif cwiczenie == 'RM':#"równania matematycznego":
				load_frame6(poziom_trudnosci)
		else:
			komunikat_brak_wyboru.place(relx=0.5,rely=0.15, anchor='n')

	obrazek_latwy = Image.open("Icons/latwy.png")  
	obrazek_latwy = obrazek_latwy.resize((125, 125), Image.BILINEAR)  
	obrazek_latwy = ImageTk.PhotoImage(obrazek_latwy)
	zdj_latwy = CTkLabel(page2_trudnosc, text='')
	zdj_latwy.configure(image=obrazek_latwy)
	zdj_latwy.place(relx=0.1625, rely=0.40, anchor='w')

	obrazek_sredni = Image.open("Icons/sredni.png")  
	obrazek_sredni = obrazek_sredni.resize((375, 225), Image.BILINEAR)  
	obrazek_sredni = ImageTk.PhotoImage(obrazek_sredni)
	zdj_sredni = CTkLabel(page2_trudnosc, text='')
	zdj_sredni.configure(image=obrazek_sredni)
	zdj_sredni.place(relx=0.4, rely=0.40, anchor='w')

	obrazek_trudny = Image.open("Icons/trudny.png")  
	obrazek_trudny = obrazek_trudny.resize((375, 225), Image.BILINEAR)  
	obrazek_trudny = ImageTk.PhotoImage(obrazek_trudny)
	zdj_trudny = CTkLabel(page2_trudnosc, text='')
	zdj_trudny.configure(image=obrazek_trudny)
	zdj_trudny.place(relx=0.760, rely=0.40, anchor='w')
	
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


def koniec(cwiczenie, poziom_trudnosci,wynikKoncowy,czasCwiczenia):
	page7_koniec.tkraise()
	ramka_koniec=CTkFrame(page7_koniec,corner_radius=10,fg_color='#5E7FA6' )
	ramka_koniec.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

	napis_TwojWynik=CTkLabel(ramka_koniec,text=f'Twój wynik: \n czas ćwiczenia: {czasCwiczenia} \n wynik końcowy:{wynikKoncowy}',fg_color='white', font=('Arial',60),corner_radius=32,width=500, height=100) 
	napis_TwojWynik.place(relx=0.5,rely=0.05, anchor='n')

	info_podajNIck= CTkLabel(ramka_koniec,text='Proszę podaj nick!',font=('Arial',60,'bold'))
	info_podajNIck.place(relx=0.5,rely=0.3,anchor='n')
	
	def clear_entry(event):
		if podaj_nick.get() == 'Podaj nick!':
			podaj_nick.delete(0, "end")
			
	def refill_entry(event):
		if not podaj_nick.get():
			podaj_nick.insert(0, 'Podaj nick!')

	podaj_nick = CTkEntry(ramka_koniec, font=('Arial', 60), corner_radius=32, width=250, height=75)
	podaj_nick.insert(0, 'Podaj nick!')
	podaj_nick.bind("<FocusIn>", clear_entry)
	podaj_nick.bind("<FocusOut>", refill_entry)
	podaj_nick.place(relx=0.5, rely=0.45, relwidth=0.50, relheight=0.30, anchor='n')

	def dalej():
		nick=podaj_nick.get()
		if nick != 'Podaj nick!' and nick !='':
			print(f'{cwiczenie}, {poziom_trudnosci}, {nick}')
	
			try:
				sql_query = f"INSERT INTO Tabela_Wynikow (Game_ID, Difficulty, Nick, Wynik, Avg_time) VALUES (?, ?, ?, ?, ?)" 
				# Execute the SQL Query 
				cursor.execute(sql_query, (cwiczenie, poziom_trudnosci,nick,wynikKoncowy,czasCwiczenia))
				# Commit the transaction
				conn.commit()
				print("Dane zostały pomyślnie wstawione do bazy danych.")
				wyniki (cwiczenie, poziom_trudnosci,nick,wynikKoncowy,czasCwiczenia)
			except Exception as e:
				print(f"Błąd podczas wstawiania danych do bazy danych: {str(e)}")
				#conn.rollback()
			'''
			finally:
					# Zamknięcie kursora i połączenia
					cursor.close()
					conn.close()			
			'''					
			
	wyniki_dalej= CTkButton(ramka_koniec,text="Dalej", font=('Arial',40),corner_radius=32,width=250, height=75,command= dalej)#lambda: wyniki (cwiczenie, poziom_trudnosci,nick,wynikKoncowy,czasCwiczenia))
	wyniki_dalej.place(relx=0.5, rely=0.85, anchor='n')


def wyniki(cwiczenie,poziom_trudnosci,nick,wynikKoncowy,czasCwiczenia):
	page8_wyniki.tkraise()
	
	info_tabelawynikow=CTkLabel(page8_wyniki,text='Tabela wyników',fg_color='white', font=('Arial',60),corner_radius=32,width=250, height=85)
	info_tabelawynikow.place(relx=0.5,rely=0.05,anchor='n')
	PowrotStart_button=CTkButton(page8_wyniki,text='  Wróć do menu  ',font=('Arial',50,'bold'),corner_radius=32,width=250, height=75,command=load_frame1)
	PowrotStart_button.place(relx=0.3,rely=0.9,anchor='s')
	jeszczeRaz_button=CTkButton(page8_wyniki,text='Zagraj jeszcze raz',font=('Arial',50,'bold'),corner_radius=32,width=250, height=75,command=lambda:load_frame2(cwiczenie))
	jeszczeRaz_button.place(relx=0.725,rely=0.9,anchor='s')

	ramka_wyniki=CTkFrame(page8_wyniki,corner_radius=10,fg_color='#5E7FA6' )
	ramka_wyniki.place(relx=0.175,rely=0.15,relwidth=0.68,relheight=0.65)
	ramka_prostokat = CTkFrame(ramka_wyniki, corner_radius=0, bg_color='white')
	ramka_prostokat.place(relx=0.04, rely=0.06, relwidth=0.92, relheight=0.87)


	sql_query = f"SELECT TOP 10 Nick, Wynik FROM Tabela_Wynikow WHERE Game_ID = ? AND Difficulty = ? ORDER BY Wynik DESC"
	cursor=conn.cursor()
	cursor.execute(sql_query, (cwiczenie, poziom_trudnosci))
	wyniki = cursor.fetchall()

	for i, (nick, wynik) in enumerate(wyniki, start=1):
		label_numer = CTkLabel(ramka_prostokat, text=f"{i}.", font=('Arial', 40), width=50, height=50)
		label_numer.place(relx=0.15, rely=0.05 + i * 0.1, anchor='w')
        
		label_nick = CTkLabel(ramka_prostokat, text=f"{nick}", font=('Arial', 40), width=300, height=50)
		label_nick.place(relx=0.3, rely=0.05 + i * 0.1, anchor='w')
        
		label_wynik = CTkLabel(ramka_prostokat, text=f"{wynik}", font=('Arial', 40), width=200, height=50)
		label_wynik.place(relx=0.7, rely=0.05 + i * 0.1, anchor='w')

	#cursor.close()
	#conn.close()	
	

def load_frame3(poziom_trudnosci):
	page3_CzasReakcji.tkraise()
	for widget in page3_CzasReakcji.winfo_children():
		widget.destroy()
	wroc=ImageTk.PhotoImage(Image.open('zle.png').resize((20,20),Image.BILINEAR))
	button_wro=CTkButton(page3_CzasReakcji,image=wroc,text='Powrót do startu',command=load_frame1)
	button_wro.place(relx=0.9, rely=0.015)

	global punkty 
	global wynikKoncowy
	wynikKoncowy=0
	punkty =0
	czasCwiczenia
	czas_naZapamiętaine = 4 if poziom_trudnosci==1 else 3 if poziom_trudnosci==2 else 2
	liczba_rund=5

	wyswietla_obrazki=CTkLabel(page3_CzasReakcji, text='')
	wyswietla_obrazki.place(relx=0.5, rely=0.6, anchor='s')
	info_kliknijspace=CTkLabel(page3_CzasReakcji, text='Kliknij w spacje',fg_color='white', font=('Arial',60,'bold'),corner_radius=32,width=250, height=75)

	def start(liczba_rund):
		global czasy
		czasy = []
		nonlocal czas_naZapamiętaine 

		for runda in range (liczba_rund):
			print(f"lr{runda}")
			info_kliknijspace.place_forget()
			global isPressed
			isPressed=0
			czas=time.time()
			obrazek = ImageTk.PhotoImage(Image.open(f"Czasreakcji\{1}.png").resize((300, 300), Image.BILINEAR))
			wyswietla_obrazki.configure(image=obrazek)
			page3_CzasReakcji.update()

			time.sleep(czas_naZapamiętaine)
			wyswietla_obrazki.configure(image='')
			info_kliknijspace.place(relx=0.5,rely=0.90, anchor='s')
			czasStart=time.time()
			obrazek2 = ImageTk.PhotoImage(Image.open(f"Czasreakcji\{2}.png").resize((300, 300), Image.BILINEAR))
			wyswietla_obrazki.configure(image=obrazek2)
			page3_CzasReakcji.update()
			while isPressed == 0:
				if keyboard.is_pressed("space"):
					print("kliknieto")
					isPressed = 1
					wynik = time.time() - czasStart
					czasy.append(wynik)
					print(wynik)

		global wynikKoncowy
		wynikKoncowy = round(sum(czasy) / len(czasy), 2)
		print(f"CR, {poziom_trudnosci, wynikKoncowy, czasCwiczenia}")
		koniec('CR',poziom_trudnosci,wynikKoncowy,czasCwiczenia)

	start(liczba_rund)


def load_frame4(poziom_trudnosci):
	page4_TreningPamieci.tkraise()
	for widget in page4_TreningPamieci.winfo_children():
		widget.destroy()
	wroc=ImageTk.PhotoImage(Image.open('zle.png').resize((20,20),Image.BILINEAR))	
	button_wro=CTkButton(page4_TreningPamieci,image=wroc,text='Powrót do startu',command=load_frame1)
	button_wro.place(relx=0.9, rely=0.015)


	global czasCwiczenia #
	global wynikKoncowy
	global punkty
	punkty = 0
	wynikKoncowy = 0
	
	czasCwiczenia = time.time()

	liczba_rund=3 if poziom_trudnosci==1 else  5 if poziom_trudnosci==2 else 8 
	liczba_obrazkow =3 if poziom_trudnosci==1 else 4 if poziom_trudnosci==2 else 5
	obrazki = [CTkLabel(page4_TreningPamieci,text='') for _ in range(liczba_obrazkow)]
	comboboxy=[CTkComboBox(page4_TreningPamieci,values=[str(i + 1) for i in range(liczba_obrazkow)])for _ in range (liczba_obrazkow)]
	
	info_ZapamietajPodajKolejnosc=CTkLabel(page4_TreningPamieci,text='Zapamiętaj kolejność!',fg_color='white', font=('Arial',60,'bold'),corner_radius=32,width=250, height=75 ) 
	info_ZapamietajPodajKolejnosc.place(relx=0.5,rely=0.05,anchor='n')
	
	info_niepoprawniezaznaczone= CTkLabel(page4_TreningPamieci,text='',fg_color='red', font=('Arial',40,'bold'),corner_radius=32,width=250, height=75)
	
	mierzy_czas=CTkLabel(page4_TreningPamieci,text='',fg_color='white', font=('Arial',60,'bold'),corner_radius=32,width=250, height=75)
	mierzy_czas.place(relx=0.5,rely=0.90, anchor='s')
	button_dalej=CTkButton(page4_TreningPamieci,text='Dalej', font=('Arial',60,'bold'),corner_radius=32,width=250, height=75)

	def nowarunda():
		nonlocal liczba_rund
		liczba_rund -=1
		if 0<=liczba_rund:
			for obrazek in obrazki:
				obrazek.configure(image='')
				obrazek.place_forget()
			for combobox in comboboxy:
				combobox.place_forget()
			button_dalej.place_forget()
			info_niepoprawniezaznaczone.place_forget()
			mierzy_czas.place(relx=0.5,rely=0.90, anchor='s')
			start_rundy()

	def sprawdz(orginalna,etykieta,combo): 
		tabZgodnisci=[]
		wszystkie_zaznaczone = all(combo[i].get()for i in range(len(etykieta)))
		if wszystkie_zaznaczone:
			for i in range(len(etykieta)):
				sprawdzana=combo[i].get()
				#print(sprawdzana,type(sprawdzana))
				if sprawdzana:
					if sprawdzana not in  [combo[j].get() for j in range(len(etykieta)) if j != i]: # sprawdza czy się powtarza, CZY ROBIMY, ŻE NIE MOŻNA WYBRAĆ TEGO SAMEGO NUMERKA?
						if orginalna[i]==etykieta[int(sprawdzana)-1]:
							tabZgodnisci.append(1)
						else:
							tabZgodnisci.append(0)
					else:
						print("powtarza sie")
						info_niepoprawniezaznaczone.configure(text="Powtarza się")
						info_niepoprawniezaznaczone.place(relx=0.5,rely=0.15,anchor='n')
						return
				else:
					break
		else:
			print("Zaznacz")
			info_niepoprawniezaznaczone.configure(text='Zaznacz wszystko')
			info_niepoprawniezaznaczone.place(relx=0.5,rely=0.15,anchor='n') # to mozna gdzies indziej przenieść
			return
		global punkty
		punkty += sum(tabZgodnisci)
		print(tabZgodnisci, punkty)
		nowarunda()

		return tabZgodnisci
	
	def start_rundy():
		global czasCwiczenia
		global wynikKoncowy
		nonlocal liczba_rund
		if 0<=liczba_rund:
			tablica=[] 
			while len(tablica) < liczba_obrazkow:
				x = random.randrange(1, 10) # TU TRZEBA PAMIĘTAĆ, DRUGI PARAMETR POWINNIEN MIEĆ TAKA SAMĄ WARTOŚĆ ILE JEST OBRAZKÓW W FOLDERZE
				if x not in tablica:
					tablica.append(x)
					obrazek = ImageTk.PhotoImage(Image.open(f"Treningpamieci\{x}.png").resize((300, 300), Image.BILINEAR))
					obrazki[len(tablica) - 1].configure(image=obrazek)  
					obrazki[len(tablica) - 1].place(relx=len(tablica)  / (liczba_obrazkow + 1), rely=0.40, anchor='center')
					#print(tablica[len(tablica) - 1]) 

			start_time=time.perf_counter()
			while time.perf_counter()-start_time<5:
				pozostaly_czas=int(5-(time.perf_counter()-start_time))
				mierzy_czas.configure(text=f'{pozostaly_czas}')
				page4_TreningPamieci.update()
			mierzy_czas.place_forget() 
					
			tablica2=tablica.copy()

			random.shuffle(tablica)
					#print(tablica)

			for i,x in enumerate(tablica):
				obrazek = ImageTk.PhotoImage(Image.open(f"Treningpamieci\{x}.png").resize((300, 300), Image.BILINEAR))
				obrazki[i].configure(image=obrazek)  
				obrazki[i].place(relx=(i + 1) / (liczba_obrazkow + 1), rely=0.40, anchor='center')
				#print(tablica[i])
				combobox = comboboxy[i]
				combobox.place(relx=(i + 1) / (liczba_obrazkow + 1), rely=0.60, anchor='center')
				combobox.set('') 


			info_ZapamietajPodajKolejnosc.configure(text='Podaj kolejność!')
			page4_TreningPamieci.update()
		
		if 0<liczba_rund:
			button_dalej.place(relx=0.5,rely=0.90, anchor='s')
			button_dalej.configure(text='Dalej')
			button_dalej.configure(command= lambda: sprawdz(tablica2,tablica,comboboxy))
		else:
			czasCwiczenia = round(time.time() - czasCwiczenia, 2) #tu trzeba bedzie odjąć czas który się odlicza
			wynikKoncowy = punkty * 50 + round((60 - czasCwiczenia) * 50)
			print(czasCwiczenia, punkty, wynikKoncowy)
			button_dalej.place(relx=0.5,rely=0.90, anchor='s')
			button_dalej.configure(text='Koniec')
			button_dalej.configure(command=lambda: koniec ("TP", poziom_trudnosci,wynikKoncowy,czasCwiczenia))

	start_rundy()

def load_frame5(poziom_trudnosci):
	page5_KolejnoscAlfabetyczna.tkraise()
	for widget in page5_KolejnoscAlfabetyczna.winfo_children():
		widget.destroy()
	wroc=ImageTk.PhotoImage(Image.open('zle.png').resize((20,20),Image.BILINEAR))
	button_wro=CTkButton(page5_KolejnoscAlfabetyczna,image=wroc,text='Powrót do startu',command=load_frame1)
	button_wro.place(relx=0.9, rely=0.015)
	ramka_KA=CTkFrame(page5_KolejnoscAlfabetyczna,corner_radius=10,fg_color='#dbda79')
	ramka_KA.place(relx=0.2,rely=0.25,relwidth=0.6,relheight=0.6)

	global czasCwiczenia 
	global wynikKoncowy
	global punkty
	punkty = 0
	wynikKoncowy = 0
	czasCwiczenia = time.time()

	liczba_rund=3 if poziom_trudnosci==1 else  4 if poziom_trudnosci==2 else 5 
	liczba_slow = 4 if poziom_trudnosci==1 else 5 if poziom_trudnosci==2 else 6

	info_kolejnoscalfabetyczna=CTkLabel(page5_KolejnoscAlfabetyczna,text='Ułóż podane słowa w kolejności alfabetycznej:',fg_color='white', font=('Arial',60,'bold'),corner_radius=32,width=250, height=75 ) 
	info_kolejnoscalfabetyczna.place(relx=0.5,rely=0.05,anchor='n')

	info_jakieslowasa= CTkLabel(page5_KolejnoscAlfabetyczna,text='',font=('Arial',45))
	info_jakieslowasa.place(relx=0.5,rely=0.15, anchor='n')

	numery = []
	listarozijana = []

	ListaSlow = []

	with open ("Kolejnośćalfabetyczna.txt", 'r',encoding='utf-8') as file:
		slowa = file.read().split(";")
		for slowo in slowa:
			ListaSlow.append(slowo)
	
	SlowadoUlozenia=[]

	def nowa_runda():  # albo robimy funkcję albo w def sprawdź damy tą jedną linijkę kodu (tak jak napisałam poniżej)
		listarozijana.clear()
		start()

	def sprawdz():
		global SlowadoUlozenia
		wybrane_slowa = [option_menu["text"] for option_menu in listarozijana]
		posortowane_slowa = sorted(SlowadoUlozenia)
		if wybrane_slowa == posortowane_slowa:
			print("Kolejność poprawna!")
			#listarozijana.clear()
			global punkty
			punkty += len(wybrane_slowa)
			print(punkty)
			start()
			#nowa_runda()
		else:
			print("Błędna kolejność!")
			checkTab = []
			for el in range(len(wybrane_slowa)):
				if wybrane_slowa[el] == posortowane_slowa[el]:
					checkTab.append(1)
				else:
					checkTab.append(0)
			punkty += sum(checkTab)
			print(punkty)
			#listarozijana.clear()
			start()
			#nowa_runda()

	def start():
		global czasCwiczenia, SlowadoUlozenia
		nonlocal liczba_rund
		liczba_rund -=1
		if 0<= liczba_rund:
			SlowadoUlozenia =random.sample(ListaSlow,liczba_slow)
			slowa_string = ", ".join(SlowadoUlozenia) 
			info_jakieslowasa.configure(text=slowa_string)
			for menu in listarozijana:
				menu.grid_forget()
				menu.destroy()

			listarozijana.clear()			
			for i in range(liczba_slow):
				numery.append(CTkLabel(ramka_KA, text=str(i + 1), font=('Arial',55,'bold')))
				numery[i].place(relx=0.325, rely=0.15 + 0.15 * i, anchor='center')
				listarozijana_var = StringVar(ramka_KA)
				listarozijana_var.set("Wybierz słowo")
				listarozijana.append(OptionMenu(ramka_KA, listarozijana_var, *SlowadoUlozenia))
				listarozijana[i].place(relx=0.575, rely=0.15 + 0.15 * i, anchor='center')
		if liczba_rund ==0:
			czasCwiczenia = round(time.time() - czasCwiczenia, 2)
			global wynikKoncowy
			wynikKoncowy = punkty * 50 + (60 - czasCwiczenia) * 50
			print(czasCwiczenia, punkty, wynikKoncowy)
			przycisk_dalej.configure(text='Koniec')
			przycisk_dalej.configure(command=lambda: koniec ("KA", poziom_trudnosci,wynikKoncowy,czasCwiczenia))
		
					
	przycisk_dalej= CTkButton(page5_KolejnoscAlfabetyczna,text='Dalej', font=('Arial',60,'bold'),corner_radius=32,width=250, height=75,command=sprawdz)
	przycisk_dalej.place(relx=0.94, rely=0.87,anchor='e')

	start()


def load_frame6(poziom_trudnosci): 
	page6_RownaniaMatematyczne.tkraise()
	for widget in page6_RownaniaMatematyczne.winfo_children():
		widget.destroy()
	wroc=ImageTk.PhotoImage(Image.open('zle.png').resize((20,20),Image.BILINEAR))
	button_wro=CTkButton(page6_RownaniaMatematyczne,image=wroc,text='Powrót do startu',command=load_frame1)
	button_wro.place(relx=0.9, rely=0.015)

	global czasCwiczenia #
	global wynikKoncowy
	global punkty
	punkty = 0
	wynikKoncowy = 0
	czasCwiczenia = time.time()

	info_rozwiazRownanie=CTkLabel(page6_RownaniaMatematyczne,text='Rozwiąż równanie!',fg_color='white', font=('Arial',60,'bold'),corner_radius=32,width=250, height=75 )
	info_rozwiazRownanie.place(relx=0.5,rely=0.05,anchor='n')

	info_o_wyniku=CTkLabel(page6_RownaniaMatematyczne, text='')
	info_o_wyniku.place(relx=0.5, rely=0.75, anchor='s')

	liczba_rund=4 if poziom_trudnosci==1 else  6 if poziom_trudnosci==2 else 9 # 5 rund dla łatwej; 7 dla średniej; 10 dla trudnej

	if poziom_trudnosci==1:
		liczby =[random.randint(1,10) for _ in range(2)]
		operatory=[random.choice(["+"]) for _ in range(1)]
	elif poziom_trudnosci==2:
		liczby =[random.randint(1,10) for _ in range(3)]
		operatory=[random.choice(["+","-"]) for _ in range(2)]	
	elif poziom_trudnosci==3:
		liczby =[random.randint(1,10) for _ in range(5)]
		#operatory=[random.choice(["+","-","*"]) for _ in range(3)] # tylko jedno mnożenie 
		operatory=[]
		ilosc_mnozenia = 0
		for _ in range(3):
			if ilosc_mnozenia == 0:
				operator= random.choice(["+","-","*"])
			else:
				operator=random.choice(["+","-"])
			if operator == "*":
				ilosc_mnozenia +=1
			operatory.append(operator)
					

	rownanie = " ".join(str(liczba) + " " + operator for liczba, operator in zip(liczby, operatory)) + " "+ str(liczby[-1])  ## CZY WYNIK ROBIMY UJEMNY ??
	wynik=eval(rownanie)

	info_rownanie=CTkLabel(page6_RownaniaMatematyczne,text=rownanie,fg_color='white',font=('Arial',55),corner_radius=10)#,width=250, height=50)
	info_rownanie.place(relx=0.3, rely=0.3,relwidth=0.3,relheight=0.25, anchor='n')

	znak_rownosci=CTkLabel(page6_RownaniaMatematyczne,text='=',font=('Arial',160,'bold'),text_color='white')
	znak_rownosci.place(relx=0.57, rely=0.42, anchor='e')

	podaj_Wynik=CTkEntry(page6_RownaniaMatematyczne, font=('Arial',55,'bold'),corner_radius=10, justify=CENTER)
	podaj_Wynik.place(relx=0.85, rely=0.425,relwidth=0.2,relheight=0.2, anchor='e')
	
	def sprawdz():
		nonlocal liczba_rund,poziom_trudnosci
		global czasCwiczenia,wynikKoncowy
		wpisany_wynik=podaj_Wynik.get().strip()
		if wpisany_wynik.isdigit():
			if wpisany_wynik==str(wynik):
				obrazek_ok_dp=ImageTk.PhotoImage(Image.open('ok.png').resize((75,75),Image.BILINEAR))
				info_o_wyniku.configure(image=obrazek_ok_dp)
				global punkty
				punkty += 1
				print(punkty)
			elif wpisany_wynik !='': # kiedy użytkownik nic nie wpisze to nic się nie dzieje
				obrazek_nie_ok_dp=ImageTk.PhotoImage(Image.open('zle.png').resize((100,100),Image.BILINEAR))
				info_o_wyniku.configure(image=obrazek_nie_ok_dp)
		
		if liczba_rund>0:
			page6_RownaniaMatematyczne.after(1000,nastepna_runda)
		else:
			page6_RownaniaMatematyczne.after(1000,lambda: koniec("RM", poziom_trudnosci,wynikKoncowy,czasCwiczenia))
		
 
	def nastepna_runda():#poziom_trudnosci,liczba_rund):
		global czasCwiczenia
		nonlocal liczby,operatory,rownanie,wynik,liczba_rund
		info_o_wyniku.configure(image='')
		if liczba_rund >0:
			liczba_rund -=1
			if poziom_trudnosci==1:
				liczby =[random.randint(1,10) for _ in range(2)]
				operatory=[random.choice(["+"]) for _ in range(1)]
			elif poziom_trudnosci==2:
				liczby =[random.randint(1,10) for _ in range(3)]
				operatory=[random.choice(["+","-"]) for _ in range(2)]
			elif poziom_trudnosci==3:
				liczby =[random.randint(1,10) for _ in range(5)]
				#operatory=[random.choice(["+","-","*"]) for _ in range(3)]
				operatory=[]
				ilosc_mnozenia=0
				for _ in range(3):
					if ilosc_mnozenia ==0:
						operator= random.choice(["+","-","*"])
					else:
						operator=random.choice(["+","-"])
					if operator == "*":
						ilosc_mnozenia +=1
					operatory.append(operator)				
			
			rownanie = " ".join(str(liczba) + " " + operator for liczba, operator in zip(liczby, operatory)) + " " +  str(liczby[-1])  
			wynik=eval(rownanie)
			info_rownanie.configure(text=rownanie)
			podaj_Wynik.delete(0,'end')
			podaj_Wynik.configure(fg_color='white')
			przycisk_sprawdz_rownanie.configure(text='Sprawdź', command=sprawdz)
		if liczba_rund==0:
			czasCwiczenia = round(time.time() - czasCwiczenia, 2)
			global wynikKoncowy
			wynikKoncowy = punkty * 50 + (60 - czasCwiczenia) * 50
			print(czasCwiczenia, punkty, wynikKoncowy)
			przycisk_sprawdz_rownanie.configure(text='Koniec', command= sprawdz )#("RM", poziom_trudnosci,wynikKoncowy,czasCwiczenia))
		return liczba_rund


	przycisk_sprawdz_rownanie=CTkButton(page6_RownaniaMatematyczne, text='Sprawdź',font=('Arial',60,'bold'),corner_radius=32,width=250, height=75, command=sprawdz)
	przycisk_sprawdz_rownanie.place(relx=0.5, rely=0.85, anchor='s')



root = CTk()
root.title("Ćwiczenia")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.resizable(1,1)
root.option_add('*Font', 'Arial 20')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

page1_start = Frame(root, bg=bg_colour) # width=500, height=600,
page2_trudnosc = Frame(root, bg=bg_colour)
page3_CzasReakcji = Frame(root, bg='#3A7A5E')
page4_TreningPamieci = Frame(root, bg='#c93448')
page5_KolejnoscAlfabetyczna= Frame(root, bg='#dedb2f')
page6_RownaniaMatematyczne=Frame(root,bg=bg_colour)
page7_koniec=Frame(root,bg=bg_colour)
page8_wyniki= Frame(root,bg=bg_colour)

for frame in (page1_start, page2_trudnosc,page3_CzasReakcji,page4_TreningPamieci,page5_KolejnoscAlfabetyczna,page6_RownaniaMatematyczne,page7_koniec,page8_wyniki):
	frame.grid(row=0, column=0, sticky="nesw")


load_frame1()

root.mainloop()
