from tkinter import *
import time
from threading import Thread
import threading

top = Tk()
top.geometry("300x700")


class r(Thread):
    def run(self):
        while True:
            for r in range(5):
                time.sleep(0.1)
                r = Frame(top, height=180, width=180, bg='red')
                r.place(x=10, y=10)
                time.sleep(0.5)
                r.destroy()

            for k in range(3):
                time.sleep(0.1)
                y = Frame(top, height=180, width=180, bg='yellow')
                y.place(x=10, y=200)
                time.sleep(0.5)
                y.destroy()

            for g in range(5):
                time.sleep(0.2)
                g = Frame(top, height=180, width=180, bg='green')
                g.place(x=10, y=390)
                time.sleep(0.5)
                g.destroy()


k = r()

k.start()

top.config()
top.mainloop()