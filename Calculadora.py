from tkinter import *


raiz=Tk()

miFrame=Frame(raiz)


miFrame.pack()

operacion=""
resultado=0
#-----------------------------PANTALLA

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg="#03f943",justify="right")


#-------------Pulsaciones Teclado--------------------


def numeroPulsado(numero):
	global operacion

	if operacion != "":

		numeroPantalla.set(numero)
		operacion=""

	else:

		numeroPantalla.set(numeroPantalla.get()+numero)


#------------BORRAR------------------

def Borrador():

	numeroPantalla.set("")


#-----------OPERACIONES---------------------------

def suma(numero):

	global operacion

	global resultado

	resultado+=numero

	operacion="suma"

	numeroPantalla.set(resultado)

def resta():
	pass

def division():
	pass

def multiplicacion():
	pass

def IGUAL():

	global resultado

	numeroPantalla.set(resultado+int(numeroPantalla.get()))
	resultado=0
#----------------FILA 1----------------------------

boton9=Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=1)

boton8=Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)

boton7=Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=3)

botonDividir=Button(miFrame,text="/",width=3)
botonDividir.grid(row=2,column=4)

#----------------FILA 2-------------------------------

boton6=Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=1)

boton5=Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)

boton4=Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=3)

botonMultiplicar=Button(miFrame,text="x",width=3)
botonMultiplicar.grid(row=3,column=4)

#--------------------FILA 3---------------------------------------

boton3=Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=1)

boton2=Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)

boton1=Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=3)

botonRestar=Button(miFrame,text="-",width=3)
botonRestar.grid(row=4,column=4)

#--------------------FILA 4---------------------------------------


boton0=Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)

botonComa=Button(miFrame,text=",",width=3,command=lambda:numeroPulsado(","))
botonComa.grid(row=5,column=2)

botonIgual=Button(miFrame,text="=",width=3,command=lambda:IGUAL())
botonIgual.grid(row=5,column=3)

botonSuma=Button(miFrame,text="+",width=3, command=lambda:suma(int(numeroPantalla.get())))
botonSuma.grid(row=5,column=4)

#--------------FILA 5---------------------------

botonBorrar=Button(miFrame,width=3,text="Borrar",command=Borrador)
botonBorrar.grid(row=6,column=4)


raiz.mainloop()
