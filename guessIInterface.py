import random
import tkinter
from tkinter import *




pencere = Tk()
pencere.title("ÇILGIN SAYISAL LOTO TAHMİN PROGRAMI")
pencere.geometry('1024x768')
#pencere.iconbitmap("sayisal.ico")

#resim=PhotoImage(file="sayisal.png")
#resimEtiket=Label(pencere,image=resim)
#resimEtiket.pack()


etiket1=tkinter.Label(pencere,text="LÜTFEN TAHMİN EDİLECEK KOLON SAYISINA TIKLAYINIZ",fg="red",font="20")
etiket1.pack()
etiket2=tkinter.Label(pencere,text="                 ")
etiket2.pack()

def temizle():
    yazi1.config(text="1.KOLON")
    yazi2.config(text="2.KOLON")
    yazi3.config(text="3.KOLON")
    yazi4.config(text="4.KOLON")

def clicked1():

    liste = [87,74,1,5,62,83,21,73,71,18,72,13,22,11,52,3,43,39,27,45,82,70,32,89,88,19,8,90,
             15,12,85,29,55,54,56,42,61,46,69,44,33,63,23,20,6,64,30,65,41,37,60,4,75,79]

    guess = sorted(random.sample(liste, 6))


    yazi1.config(text=guess)
    yazi2.config(text="2.KOLON")
    yazi3.config(text="3.KOLON")
    yazi4.config(text="4.KOLON")

def clicked2():
    liste = [87, 74, 1, 5, 62, 83, 21, 73, 71, 18, 72, 13, 22, 11, 52, 3, 43, 39, 27, 45, 82, 70, 32, 89, 88, 19, 8, 90,
             15, 12, 85, 29, 55, 54, 56, 42, 61, 46, 69, 44, 33, 63, 23, 20, 6, 64, 30, 65, 41, 37, 60, 4, 75, 79]

    guess1 = sorted(random.sample(liste, 6))
    guess2 = sorted(random.sample(liste, 6))

    yazi1.config(text=guess1)
    yazi2.config(text=guess2)
    yazi3.config(text="3.KOLON")
    yazi4.config(text="4.KOLON")

def clicked3():
    liste = [87, 74, 1, 5, 62, 83, 21, 73, 71, 18, 72, 13, 22, 11, 52, 3, 43, 39, 27, 45, 82, 70, 32, 89, 88, 19, 8, 90,
             15, 12, 85, 29, 55, 54, 56, 42, 61, 46, 69, 44, 33, 63, 23, 20, 6, 64, 30, 65, 41, 37, 60, 4, 75, 79]

    guess1 = sorted(random.sample(liste, 6))
    guess2 = sorted(random.sample(liste, 6))
    guess3 = sorted(random.sample(liste, 6))

    yazi1.config(text=guess1)
    yazi2.config(text=guess2)
    yazi3.config(text=guess3)
    yazi4.config(text="4.KOLON")

def clicked4():
    liste = [87, 74, 1, 5, 62, 83, 21, 73, 71, 18, 72, 13, 22, 11, 52, 3, 43, 39, 27, 45, 82, 70, 32, 89, 88, 19, 8, 90,
             15, 12, 85, 29, 55, 54, 56, 42, 61, 46, 69, 44, 33, 63, 23, 20, 6, 64, 30, 65, 41, 37, 60, 4, 75, 79]

    guess1 = sorted(random.sample(liste, 6))
    guess2 = sorted(random.sample(liste, 6))
    guess3 = sorted(random.sample(liste, 6))
    guess4 = sorted(random.sample(liste, 6))

    yazi1.config(text=guess1)
    yazi2.config(text=guess2)
    yazi3.config(text=guess3)
    yazi4.config(text=guess4)


yazi1=tkinter.Label(pencere,text="1.KOLON",font="5")
yazi1.pack()

yazi2=tkinter.Label(pencere,text="2.KOLON",font="5")
yazi2.pack()

yazi3=tkinter.Label(pencere,text="3.KOLON",font="5")
yazi3.pack()

yazi4=tkinter.Label(pencere,text="4.KOLON",font="5")
yazi4.pack()





buton1 = Button(pencere)
buton1.config(text="1 kolon", bg="blue", fg="yellow",font="5", command=clicked1)
buton1.pack()

buton2 = Button(pencere)
buton2.config(text="2 kolon", bg="yellow", fg="blue",font="5", command=clicked2)
buton2.pack()

buton3 = Button(pencere)
buton3.config(text="3 kolon", bg="green", fg="black", font="5",command=clicked3)
buton3.pack()

buton4 = Button(pencere)
buton4.config(text="4 kolon", bg="orange", fg="white",font="5", command=clicked4)
buton4.pack()

butonTemizle=Button(pencere)
butonTemizle.config(text="Temizle",font="5", command=temizle)
butonTemizle.pack()

built=tkinter.Label(pencere,text="BUILT BY SİNAN YILDIRIM",bg="yellow",fg="blue",font="100")
built.pack()



mainloop()



