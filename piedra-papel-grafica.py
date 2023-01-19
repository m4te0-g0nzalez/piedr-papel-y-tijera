from tkinter import *
from tkinter import ttk
import random

#funciones
def piedra():
	posiciones_de_manos = ["piedra", "papel", "tijera"]
	bot = (random.choice(posiciones_de_manos))
	if bot == "piedra":
		Label(root, text="la pc tambien a elegido piedra, empate", width=30,height=10).grid(row=1, column=1)
	elif bot == "tijera":
		Label(root, text="la pc a elegido tijera, tu ganas", width=30,height=10).grid(row=1, column=1)
	elif bot == "papel":
		Label(root, text="la pc a elegido papel, tu pierdes", width=30,height=10).grid(row=1, column=1)		

		



def tijera():
	posiciones_de_manos = ["piedra", "papel", "tijera"]
	bot = (random.choice(posiciones_de_manos))
	if bot == "piedra":
		Label(root, text="la pc a elegido piedra, pierdes,", width=30,height=10).grid(row=3, column=1)
	elif bot == "tijera":
		Label(root, text="la pc a elegido tijera, empate", width=30,height=10).grid(row=3, column=1)
	elif bot == "papel":
		Label(root, text="la pc a elegido papel, tu ganas", width=30,height=10).grid(row=3, column=1)

def papel():
	posiciones_de_manos = ["piedra", "papel", "tijera"]
	bot = (random.choice(posiciones_de_manos))
	if bot == "piedra":
		Label(root, text="la pc a elegido piedra, ganas,", width=30,height=10).grid(row=2, column=1)
	elif bot == "tijera":
		Label(root, text="la pc a elegido tijera, pierdes", width=30,height=10).grid(row=2, column=1)
	elif bot == "papel":
		Label(root, text="la pc a elegido papel, empatas", width=30,height=10).grid(row=2, column=1)


root = Tk()
root.title("piedra, papel, o tijera")
root.geometry("390x485")
root.config(bg="grey")
#botones
boton = Button(root, text="piedra",width=20,height=10, command=piedra).grid(row=1, column=0)
boton = Button(root, text="papel",width=20,height=10, command=papel).grid(row=2, column=0)
boton = Button(root, text="tijera",width=20,height=10, command=tijera).grid(row=3, column=0)





root.mainloop()