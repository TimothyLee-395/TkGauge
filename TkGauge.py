# RPM Test Gauge
# TkGauge.py 8-22-16
# python3

from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("RPM")
root.geometry("300x380")

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
    
def point(degree, interval, radius):
        angle = degree * (360.0 / interval)
        radiansPerDegree = math.pi / 180
        pointX = int( round( radius * math.sin(angle * radiansPerDegree) ))
        pointY = int( round( radius * math.cos(angle * radiansPerDegree) ))
        return (pointX), (pointY)

def calculate(*args):
    try:
        value = float(var.get())
        v3 = int(value * 2000)
        value = value * 100
        var2 = int(value * 0.64)-250
        x, y = point(var2,360,117)
        scaledX, scaledY = (x + 150), (150 - y)
        canvas.delete('pointer')
        canvas.create_line(150, 150, scaledX, scaledY, width=2, arrow='last', arrowshape=(115,115,4), fill='red', tag='pointer')
        canvas.itemconfig(v1, text="%d" % (v3))
    except ValueError:
        pass

canvas = Canvas(root, width=300, height=300, borderwidth=0, highlightthickness=0)
canvas.grid()

canvas.create_circle(150, 150, 134, outline="grey99", width=1)
canvas.create_circle(150, 150, 130, outline="grey40", width=5)
canvas.create_circle(150, 150, 125, fill="white", outline="grey70", width=5)
canvas.create_circle(150, 150, 20, fill="grey85", outline="black", width=1)
canvas.create_circle(150, 150, 6, fill="red", outline="red")
canvas.create_circle_arc(150, 150, 120, style="arc", outline="black", width=1, start=340, end=20)

tick = 340
while (tick >= 20):
    canvas.create_circle_arc(150, 150, 118, style="arc", outline="black", width=4, start=tick, end=tick-1)
    tick = tick -4

tick = 340
while (tick >= 20):
    canvas.create_circle_arc(150, 150, 116, style="arc", outline="black", width=8, start=tick, end=tick-1)
    tick = tick -16    
    
canvas.create_text(247,189,  font=("Roboto", 10, ),text="0")
canvas.create_text(210,231,  font=("Roboto", 10, ),text="1000")
canvas.create_text(161,254,  font=("Roboto", 10, ),text="2000")
canvas.create_text(108,243,  font=("Roboto", 10, ),text="3000")
canvas.create_text(72,207,   font=("Roboto", 10, ),text="4000")
canvas.create_text(57,150,   font=("Roboto", 10, ),text="5000")
canvas.create_text(72,95,    font=("Roboto", 10, ),text="6000")
canvas.create_text(108,57,   font=("Roboto", 10, ),text="7000")
canvas.create_text(163,47,   font=("Roboto", 10, ),text="8000")
canvas.create_text(210,70,   font=("Roboto", 10, ),text="9000")
canvas.create_text(235,112,  font=("Roboto", 10, ),text="10000")

Rounded(145,155,228,261,6,1,canvas)
v1 = canvas.create_text(245,150, font=("Roboto", 11, ),text="0")
canvas.create_text(200,150, font=("Roboto", 12, ),text="RPM")

x, y = point(-250,360,118)
scaledX, scaledY = (x + 150), (150 - y)
canvas.create_line(150, 150, scaledX, scaledY, width=2, arrow='last', arrowshape=(90,90,4), fill='red', tag='pointer')

scale =  Scale(root, 
               orient=HORIZONTAL, 
               length=220, 
               from_=0, to=5,
               command=calculate, 
               variable = var, 
               digits=3,
               repeatinterval = 10, 
               resolution = 0.01).grid(column=0, row=1, sticky=N)
                    
Exit = ttk.Button(root, text='Exit', command=root.destroy).grid(column=0, row=2, pady=10)                    
                    
root.mainloop()
