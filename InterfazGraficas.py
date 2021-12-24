from tkinter import *
from math import *
from tkinter.font import BOLD
#VENTANA PARA LA INTERFAZ
Ventana= Tk()
Ventana.title("Calculadora de carlos fx3000")
Ventana.geometry("400x600")
Ventana.resizable(False,False)
Ventana.config(background="gray42")
#PROPIEDADES DE LOS BOTONES
color_boton="gray99"
ANCHO_boton = 10
alto_boton = 3
#FUNCIONES
operador =""
Texto= StringVar()
def clear():
    global operador
    operador =""
    Texto.set("0")
def click(b):
    global operador
    operador += str(b)
    Texto.set(operador)
def resultado():
    global operador
    try:
        r = str(eval(operador))
    except: r = "ERROR"
    Texto.set(r)
clear()
#Botones de la primera fila
Boton0 =Button(Ventana,text="0",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(0)).grid(row=1,column=0,pady=10)
Boton1 =Button(Ventana,text="1",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(1)).grid(row=1,column=1,pady=10)
Boton2 =Button(Ventana,text="2",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(2)).grid(row=1,column=2,pady=10)
Boton3 =Button(Ventana,text="3",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(3)).grid(row=1,column=3,pady=10)
# BOTONES DE LA SEGUNDAD FILA
Boton4 =Button(Ventana,text="4",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(4)).grid(row=2,column=0,pady=10)
Boton5 =Button(Ventana,text="5",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(5)).grid(row=2,column=1,pady=10)
Boton6 =Button(Ventana,text="6",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(6)).grid(row=2,column=2,pady=10)
Boton7 =Button(Ventana,text="7",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(7)).grid(row=2,column=3,pady=10)
# BOTONES DE LA TERCERA FILA
Boton8 =Button(Ventana,text="8",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(8)).grid(row=3,column=0,pady=10)
Boton9 =Button(Ventana,text="9",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(9)).grid(row=3,column=1,pady=10)
BotonPI =Button(Ventana,text="π",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click("pi")).grid(row=3,column=2,pady=10)
BotonPUNTO =Button(Ventana,text=".",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(".")).grid(row=3,column=3,pady=10)
# BOTONES DE LA CUARTA FILA
BotonSUMA =Button(Ventana,text="+",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click("+")).grid(row=4,column=0,pady=10)
BotonRESTA =Button(Ventana,text="-",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click("-")).grid(row=4,column=1,pady=10)
BotonDIVICION =Button(Ventana,text="/",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click("/")).grid(row=4,column=2,pady=10)
BotonMULTI =Button(Ventana,text="*",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click("*")).grid(row=4,column=3,pady=10)
#BOTONES DE LA QUINTA FILA
BotonRAIZ =Button(Ventana,text="√",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click("sqrt")).grid(row=5,column=0,pady=10)
BotonCLEAR =Button(Ventana,text="C",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=clear).grid(row=5,column=1,pady=10)
BotonEXP =Button(Ventana,text="EXP",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click("EXP")).grid(row=5,column=2,pady=10)
BotonIGUAL =Button(Ventana,text="=",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=resultado).grid(row=5,column=3,pady=10)
#BOTONES DE LA SEXTA FILA
BotonPariz =Button(Ventana,text="(",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click("(")).grid(row=6,column=0,pady=10)
BotonPAREDE =Button(Ventana,text=")",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click(")")).grid(row=6,column=1,pady=10)
BotonLG =Button(Ventana,text="log",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click("log")).grid(row=6,column=2,pady=10)
Botonpor =Button(Ventana,text="%",bg=color_boton,width=ANCHO_boton,height=alto_boton,command=lambda:click("%")).grid(row=6,column=3,pady=10)
Pantalla=Entry(Ventana,font=("arial",20,"bold"),width=22,borderwidth=10,background="dodger blue",textvariable=Texto)
Pantalla.grid(row=0,column=0, columnspan=4,padx=20,pady=20 )
Ventana.mainloop()
