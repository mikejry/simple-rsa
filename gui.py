import tkinter.filedialog
import tkinter as tk


from rsa import Cipher
from primes import Prime

HEIGHT = 800
WIDTH = 900
COLLORBUTTON='#bfbfbf'
COLORBACKGROUND='#3d3d5c'
COLORBUT1='#1a1a1a'





class Cache:
   

    def __init__(self):
        
        self.x = 17
        self.y = 13
        self.szyfrRsa = Cipher(self.x, self.y)

    def default(self):
        
        self.x = 17
        self.y = 13

    def makeRSA(self):
        
        self.szyfrRsa = Cipher(self.x, self.y)

    def changeKeyX(self,pierwsza):
        
        self.x = pierwsza.primeNumber
        


    def changeKeyY(self,pierwsza):
        
        self.y = pierwsza.primeNumber
        

pamiec=Cache()


def onwpiszliczbepierwszaX(Text):
    
    number = Text.get("1.0", "end-1c")
    pierwsza = Prime(number)
    pamiec.changeKeyX(pierwsza)
    on_zaktualizuj_widok_tekst(pierwsza.primeNumber, Text)
    labelLpierwsza.update_idletasks()


def onwpiszliczbepierwszaY(Text):
    
    number = Text.get("1.0", "end-1c")
    pierwsza = Prime(number)
    pamiec.changeKeyY(pierwsza)
    on_zaktualizuj_widok_tekst(pierwsza.primeNumber, Text)



def onczytajzpliku(T):
    
    try:
        x = tk.filedialog.askopenfilename()
        T.insert(tk.END, open(x, "r").read())
    except FileNotFoundError:
        "Nie wybrano pliku"


def onzapisztekst(T,nazwaPliku):
    
    T_info=T.get("1.0", "end-1c")
    with open(nazwaPliku, "w") as theFile:
        for listitem in T_info:
            theFile.write('%s' % listitem)
    theFile.close()


def onszyfruj_wiadomosc(T,T2):
    
    T_info = T.get("1.0", "end-1c")
    tekstZaszyfrowany = pamiec.szyfrRsa.encode(T_info)
    on_zaktualizuj_widok_tekst(tekstZaszyfrowany,T2)

def on_zaktualizuj_widok_tekst(tekst,T):
    
    T.config(state=tk.NORMAL)
    T.delete("1.0", tk.END)
    T.insert(tk.END, tekst)

def on_odszyfruj_wiadomość(T,T1):
    
    T_info = T.get("1.0", "end-1c")
    theInts=[]
    for val in T_info.split():
        theInts.append(int(val))
    tekstOdszyfrowany=pamiec.szyfrRsa.decode(theInts)
    on_zaktualizuj_widok_tekst(tekstOdszyfrowany, T1)

def on_wygeneruj_klucz(T1,T2,e,d,n):
    
    pamiec.makeRSA()
    on_zaktualizuj_widok_tekst(pamiec.x, T1)
    on_zaktualizuj_widok_tekst(pamiec.y, T2)
    on_zaktualizuj_widok_tekst(pamiec.szyfrRsa.klucz_pub, e)
    on_zaktualizuj_widok_tekst(pamiec.szyfrRsa.klucz_pryw, d)
    on_zaktualizuj_widok_tekst(pamiec.szyfrRsa.n, n)

def on_wygeneruj_klucz_default(T1,T2,e,d,n):
    pamiec.default()
    pamiec.makeRSA()
    on_zaktualizuj_widok_tekst("17", T1)
    on_zaktualizuj_widok_tekst("13", T2)
    on_zaktualizuj_widok_tekst(pamiec.szyfrRsa.klucz_pub, e)
    on_zaktualizuj_widok_tekst(pamiec.szyfrRsa.klucz_pryw, d)
    on_zaktualizuj_widok_tekst(pamiec.szyfrRsa.n, n)




root = tk.Tk()




canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

frameGeneruj=tk.Frame(root, bg=COLORBACKGROUND)
frameGeneruj.place(relwidth=1,relheight=0.3)
info=tk.Label(frameGeneruj,text='Aby wygenerować klucz wpisz liczby pierwsze i zatwierdź OK lub pomiń, aby wrócić do wartości domyślnych',bg='#cccccc')
info.place( rely=0.0, relx=0.1 , relheight=0.1, relwidth=0.8)
labelLpierwsza=tk.Label(frameGeneruj, text="Podaj liczbę")
labelLpierwsza.place(rely=0.1, relx=0.1, relheight=0.1, relwidth=0.1)
entrylpierwsza=tk.Text(frameGeneruj,bg='#bfbfbf')
entrylpierwsza.place(rely=0.2, relx=0.1, relheight=0.1, relwidth=0.1)
entrylpierwsza.insert("1.0", '17')
buttonok1=tk.Button(frameGeneruj, text="OK", command=lambda:onwpiszliczbepierwszaX(entrylpierwsza), activebackground=COLLORBUTTON,bg=COLORBUT1,fg='white')
buttonok1.place( rely=0.3, relx=0.1 , relheight=0.09, relwidth=0.1)
labelLpierwsza=tk.Label(frameGeneruj, text="Podaj liczbę")
labelLpierwsza.place(rely=0.1, relx=0.8, relheight=0.1, relwidth=0.1)
entryldruga=tk.Text(frameGeneruj,bg='#bfbfbf')
entryldruga.insert("1.0", '13')
entryldruga.place(rely=0.2, relx=0.8, relheight=0.1, relwidth=0.1)
buttonok2=tk.Button(frameGeneruj, text="OK", command=lambda:onwpiszliczbepierwszaY(entryldruga), activebackground=COLLORBUTTON,bg=COLORBUT1,fg='white')
buttonok2.place( rely=0.3, relx=0.8, relheight=0.09, relwidth=0.1)
# wartosci n, e i d
labelKP=tk.Label(frameGeneruj, text="Para (e,n) tworzy klucz publiczny, para (d,n) tworzy klucz prywatny",bg='#cccccc')
labelKP.place(rely=0.5, relx=0.15, relheight=0.1, relwidth=0.7)
labelE=tk.Label(frameGeneruj, text="e:")
labelE.place(rely=0.6, relx=0.15, relheight=0.1, relwidth=0.1)
entryE=tk.Text(frameGeneruj,bg='#bfbfbf')
entryE.place(rely=0.7,relx=0.15,relheight=0.1,relwidth=0.1)
entryE.insert("1.0", pamiec.szyfrRsa.klucz_pub)
labelD=tk.Label(frameGeneruj, text="d:")
labelD.place(rely=0.6, relx=0.45, relheight=0.1, relwidth=0.1)
entryD=tk.Text(frameGeneruj,bg='#bfbfbf')
entryD.place(rely=0.7,relx=0.45,relheight=0.1,relwidth=0.1)
entryD.insert("1.0", pamiec.szyfrRsa.klucz_pryw)
labelN=tk.Label(frameGeneruj, text="n:")
labelN.place(rely=0.6, relx=0.75, relheight=0.1, relwidth=0.1)
entryN=tk.Text(frameGeneruj,bg='#bfbfbf')
entryN.place(rely=0.7,relx=0.75,relheight=0.1,relwidth=0.1)
entryN.insert("1.0", pamiec.szyfrRsa.n)
buttonGeneruj= tk.Button(frameGeneruj, text="Wygeneruj klucz",command=lambda:on_wygeneruj_klucz(entrylpierwsza,entryldruga,entryE,entryD,entryN), activebackground=COLLORBUTTON,bg=COLORBUT1,fg='white')
buttonGeneruj.place( rely=0.1, relx=0.4 , relheight=0.15, relwidth=0.2)
buttonPomin=tk.Button(frameGeneruj, text="Pomiń",command=lambda:on_wygeneruj_klucz_default(entrylpierwsza,entryldruga,entryE,entryD,entryN) ,activebackground=COLLORBUTTON,bg=COLORBUT1,fg='white')
buttonPomin.place( rely=0.25, relx=0.4 , relheight=0.15, relwidth=0.2)


framelewa=tk.Frame(root, bg=COLORBACKGROUND)
framelewa.place(relx=0.0, rely=0.3, relwidth=0.5, relheight=0.7)
entrylewa=tk.Text(framelewa,bg='#bfbfbf')
entrylewa.place(rely=0.2, relx=0.1, relheight=0.7, relwidth=0.8)
buttonlewa= tk.Button(framelewa, text="Zaszyfruj",command=lambda: onszyfruj_wiadomosc(entrylewa,entryprawa), activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonlewa.place( rely=0.9, relx=0.35 , relheight=0.1, relwidth=0.3)
buttonczyta1= tk.Button(framelewa, text="Czytaj z pliku", command=lambda: onczytajzpliku(entrylewa), activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonczyta1.place( rely=0.05, relx=0.15 , relheight=0.1, relwidth=0.3)
buttonpisze1= tk.Button(framelewa, text="Zapisz do pliku", command=lambda: onzapisztekst(entrylewa, "tekst.txt"), activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonpisze1.place( rely=0.05, relx=0.55, relheight=0.1, relwidth=0.3)





frameprawa=tk.Frame(root, bg=COLORBACKGROUND)
frameprawa.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.7)
entryprawa=tk.Text(frameprawa,bg='#bfbfbf')
entryprawa.place(rely=0.2, relx=0.1, relheight=0.7, relwidth=0.8)
buttonprawa= tk.Button(frameprawa, text="Odszyfruj",command=lambda: on_odszyfruj_wiadomość(entryprawa,entrylewa),activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonprawa.place( rely=0.9, relx=0.35 , relheight=0.1, relwidth=0.3)
buttonczyta2= tk.Button(frameprawa, text="Czytaj z pliku",command=lambda: onczytajzpliku(entryprawa), activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonczyta2.place( rely=0.05, relx=0.15 , relheight=0.1, relwidth=0.3)
buttonpisze2= tk.Button(frameprawa, text="Zapisz do pliku", command=lambda: onzapisztekst(entryprawa, "nowytekst.txt"), activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonpisze2.place( rely=0.05, relx=0.55 , relheight=0.1, relwidth=0.3)

root.mainloop()
