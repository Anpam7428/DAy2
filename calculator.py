from tkinter import *

def call(event):
        global sc_Value
        text=event.widget.cget("text")
        if text =='C':
            sc_Value.set("")
            screen.update()
        elif text=="=":
              if sc_Value.get().isdigit():
                  value=int(sc_Value.get())
              else:
                  value=eval(sc_Value.get())

              sc_Value.set(value)
        elif text=='exit':
            root.destroy()
        else:
            sc_Value.set(sc_Value.get()+text)
            screen.update()

root=Tk()
root.geometry("600x1000")

sc_Value=StringVar()
sc_Value.set("")
screen= Entry(root,textvariable=sc_Value, font=("lucida 40 bold"))
screen.pack(fill=X,ipadx=8, padx=10, pady=10)

f=Frame(root, bg="gray", padx=50)
b1=Button(f, text="9", command=sc_Value,padx=14.5, pady=15,font=("lucida 35 bold"))
b1.pack(padx=10,pady=10,side=LEFT)
b1.bind("<Button-1>", call)
b2=Button(f, text="8" , command=sc_Value,padx=14.5, pady=15,font=("lucida 35 bold"))
b2.pack(padx=10,pady=10,side=LEFT)
b2.bind("<Button-1>", call)
b3=Button(f, text="7" , command=sc_Value,padx=14.5, pady=15,font=("lucida 35 bold"))
b3.pack(padx=10,pady=10,side=LEFT)
b3.bind("<Button-1>", call)
b4=Button(f, text="C" , command=sc_Value,padx=14.5, pady=15,font=("lucida 35 bold"))
b4.pack(padx=10,pady=10,side=LEFT)
b4.bind("<Button-1>", call)
f.pack()

f=Frame(root, bg="gray", padx=50)
b1=Button(f, text="6" , command=sc_Value,padx=16, pady=15,font=("lucida 35 bold"))
b1.pack(padx=10,side=LEFT, pady=10)
b1.bind("<Button-1>", call)
b2=Button(f, text="5" , command=sc_Value,padx=16, pady=15,font=("lucida 35 bold"))
b2.pack(padx=10,side=LEFT, pady=10)
b2.bind("<Button-1>", call)
b3=Button(f, text="4" , command=sc_Value,padx=16, pady=15,font=("lucida 35 bold"))
b3.pack(padx=10,side=LEFT, pady=10)
b3.bind("<Button-1>", call)
b4=Button(f, text="+" , command=sc_Value,padx=16, pady=15,font=("lucida 35 bold"))
b4.pack(padx=10,side=LEFT, pady=10)
b4.bind("<Button-1>", call)
f.pack()
f=Frame(root, bg="gray", padx=50)
b1=Button(f, text="3" , command=sc_Value,padx=17, pady=15,font=("lucida 35 bold"))
b1.pack(padx=10,side=LEFT, pady=10)
b1.bind("<Button-1>", call)
b2=Button(f, text="2" , command=sc_Value,padx=17, pady=15,font=("lucida 35 bold"))
b2.pack(padx=10,side=LEFT, pady=10)
b2.bind("<Button-1>", call)
b3=Button(f, text="1" , command=sc_Value,padx=17, pady=15,font=("lucida 35 bold"))
b3.pack(padx=10,side=LEFT, pady=10)
b3.bind("<Button-1>", call)
b4=Button(f, text="-" , command=sc_Value,padx=17, pady=15,font=("lucida 35 bold"))
b4.pack(padx=10,side=LEFT, pady=10)
b4.bind("<Button-1>", call)
f.pack()

f=Frame(root, bg="gray", padx=50)
b1=Button(f, text="." , command=sc_Value,padx=25, pady=15,font=("lucida 35 bold"))
b1.pack(padx=10,side=LEFT, pady=10)
b1.bind("<Button-1>", call)
b2=Button(f, text="0" , command=sc_Value,padx=18, pady=15,font=("lucida 35 bold"))
b2.pack(padx=10,side=LEFT, pady=10)
b2.bind("<Button-1>", call)
b3=Button(f, text="/" , command=sc_Value,padx=18, pady=15,font=("lucida 35 bold"))
b3.pack(padx=10,side=LEFT, pady=10)
b3.bind("<Button-1>", call)
b4=Button(f, text="*" , command=sc_Value,padx=18, pady=15,font=("lucida 35 bold"))
b4.pack(padx=10,side=LEFT, pady=10)
b4.bind("<Button-1>", call)
f.pack()

f=Frame(root, bg="gray", padx=50)
b1=Button(f, text="00" , command=sc_Value,padx=25, pady=15,font=("lucida 35 bold"))
b1.pack(padx=10,side=LEFT, pady=10)
b1.bind("<Button-1>", call)
b2=Button(f, text="exit" , command=sc_Value,padx=18, pady=15,font=("lucida 35 bold"))
b2.pack(padx=10,side=LEFT, pady=10)
b2.bind("<Button-1>", call)

b4=Button(f, text="=" , command=sc_Value,padx=18, pady=15,font=("lucida 35 bold"))
b4.pack(padx=10,side=LEFT, pady=10)
b4.bind("<Button-1>", call)
f.pack()




root.mainloop()