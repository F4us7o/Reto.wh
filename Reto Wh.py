import sys
from tkinter import*

def click() :
    num=int(entrada_txt.get())
    numx=int(num)
    for x in range(1,11):
        producto=num*x
        print(num,'X',x,'=',producto)


reto=Tk()
reto.title('Reto Wh')

vp=Frame(reto)
vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
vp.columnconfigure(0,weight=1)  
vp.rowconfigure(0,weight=1)


boton=Button(vp,text='Mostrar tabla',command=click)
boton.grid(column=1,row=1)

etiqueta=Label(vp,text='Resultado')
etiqueta.grid(column=2,row=2,sticky=(W,E))

valor=""
entrada_txt=Entry(vp,width=10,textvariable=valor)
entrada_txt.grid(column=2,row=1)

reto.mainloop()
