# Temperature Test Gauge
# TkGaugePB.py 9-22-16
# python3

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Temperature")
root.geometry("300x350")

var = DoubleVar()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    
Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
    
Canvas.create_circle_arc = _create_circle_arc

def Rounded(t,b,l,r,d,w, canvas, **kwargs):
        canvas.create_circle(l, t, d, fill="grey90", outline="black", width=w)  #tl
        canvas.create_circle(l, b, d, fill="grey90", outline="black", width=w)  #bl
        canvas.create_circle(r, t, d, fill="grey90", outline="black", width=w)  #tr
        canvas.create_circle(r, b, d, fill="grey90", outline="black", width=w)  #br

        canvas.create_rectangle(l,(t-d),r,(b+d), outline="", fill="grey90")  #vertrec
        canvas.create_rectangle((l-d),t,(r+d),b, outline="", fill="grey90")  #horzrec

        canvas.create_line(l,(t-d),r,(t-d), fill="black", width=w)  #thorz
        canvas.create_line(l,(b+d),r,(b+d), fill="black", width=w)  #bhorz
        canvas.create_line((l-d),t,(l-d),b, fill="black", width=w)  #lvert
        canvas.create_line((r+d),t,(r+d),b, fill="black", width=w)  #rvert

def calculate(*args):
    global bar
    try:
        value = float(var.get())
        v3 = value * 100
        Mend = int(v3 * -1.8)+224
        canvas.delete(bar)
        bar = canvas.create_circle_arc(150, 150, 90, style="arc", outline="red", width=15, start=225, end=Mend)
        canvas.itemconfig(v1, text="%.1f" % (v3))
    except ValueError:
        pass

canvas = Canvas(root, width=300, height=300, borderwidth=0, highlightthickness=0)
canvas.grid(column=0)

canvas.create_circle(150, 150, 105, outline="grey40", width=5)
canvas.create_circle(150, 150, 109, outline="grey99", width=1)
canvas.create_circle(150, 150, 100, fill="white", outline="grey70", width=5)
canvas.create_circle(150, 150, 20, fill="grey70", outline="black", width=2)
canvas.create_circle_arc(150, 150, 80, style="arc", outline="black", width=1, start=225, end=-45)

tick = 225
while (tick >= -45):
    canvas.create_circle_arc(150, 150, 78, style="arc", outline="black", width=4, start=tick, end=tick-1)
    tick = tick -9
    
canvas.create_text(150,25,  font=("Roboto", 11, ),text="Temperature" )    
canvas.create_text(102,201, font=("Roboto", 11, ),text="0")
canvas.create_text(85,150,  font=("Roboto", 11, ),text="25")
canvas.create_text(101,105, font=("Roboto", 11, ),text="50")
canvas.create_text(150,85,  font=("Roboto", 11, ),text="75")
canvas.create_text(195,105, font=("Roboto", 11, ),text="100")
canvas.create_text(212,150, font=("Roboto", 11, ),text="125")
canvas.create_text(191,201, font=("Roboto", 11, ),text="150")
canvas.create_text(150,214, font=("Roboto", 11, ),text="degrees" )
canvas.create_text(150,230, font=("Roboto", 11, ),text="Fahreheit" )

Rounded(188,195,131,168,6,1,canvas)

v1 = canvas.create_text(150,191, font=("Roboto", 12, ),text="0.0")
bar = canvas.create_circle_arc(150, 150, 90, style="arc", outline="red", width=15, start=225, end=224)

scale =  Scale(root, 
               orient=HORIZONTAL, 
               length=220, 
               from_=0, to=1.50,
               command=calculate, 
               variable = var, 
               digits=4,
               repeatinterval = 10, 
               resolution = 0.005).grid(column=0, row=0, sticky=S)

Exit = ttk.Button(root, text='Exit', command=root.destroy).grid(column=0, row=2, pady=13)

root.mainloop()
