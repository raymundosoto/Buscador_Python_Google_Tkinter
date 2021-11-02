# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:54:15 2021

@author: Raymundo Soto
"""


from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from googlesearch import search

def Crear_ventana():
    def clicked():
        texto_a_mostrar = txt_1.get()
        Label_1.configure(text='Buscando...' + texto_a_mostrar)
        #txt_scroll.insert(INSERT, texto_a_mostrar + '\n')
        resultados = search(texto_a_mostrar, tld='com', lang='eng', num=100,
                                   start=0, stop=100, pause=0.1)
        for i in resultados:
            txt_scroll.insert(INSERT, i + '\n')
        
    def Limpiar():
        txt_scroll.delete(1.0, END)
    
    def Cerrar():
        ventana.destroy()

    ventana= Tk()
    ventana.geometry('1000x400')
    ventana.title('Buscador de dominios con Python - Google y Tkinter')
    
    txt_1 = Entry(ventana, width=50)
    txt_1.grid(column=3, row = 2)
    txt_1.focus()
    
    Label_1 = Label(ventana, text= 'Buscador Google-Python'+ txt_1.get(), font=("Arial Bold", 20))
    Label_1.grid(column=3, row=0)
    
    Label_2 = Label(ventana, text= 'Palabras de búsqueda', font=("Arial Bold", 10))
    Label_2.grid(column=0, row=2)
    
    Boton_1 = Button(ventana, text = 'Realizar Búsqueda ', command=clicked)
    Boton_1.grid(column=4, row=2)
    
    txt_scroll = scrolledtext.ScrolledText(ventana,width=60,height=13)
    txt_scroll.grid(column=3,row=6)
    
    Label_3 = Label(ventana, text= 'Resultados de búsqueda', font=("Arial Bold", 10))
    Label_3.grid(column=3, row=10)
    
    Boton_limpiar = Button(ventana, text = 'Limpiar', command = Limpiar)
    Boton_limpiar.grid(column = 4, row=6)
    
    Boton_cerrar = Button(ventana, text = 'Cerrar', command = Cerrar)
    Boton_cerrar.grid(column = 4, row=9)
    
    ventana.mainloop()
    
    
if __name__ == '__main__':
    Crear_ventana()