from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO

red = 11
blue = 13
green = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, GPIO.LOW)
GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, GPIO.LOW)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.LOW)

win = Tk()
win.title("LED Toggle")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def rledToggle():
    if GPIO.input(11)==1:
        GPIO.output(red, GPIO.LOW)
        rledButton["text"] = "Turn red led on"
    else:
        GPIO.output(red, GPIO.HIGH)
        rledButton["text"] = "Turn red led off"
def bledToggle():
    if GPIO.input(13)==1:
        GPIO.output(blue, GPIO.LOW)
        bledButton["text"] = "Turn blue led on"
    else:
        GPIO.output(blue, GPIO.HIGH)
        bledButton["text"] = "Turn blue led off"
def gledToggle():
    if GPIO.input(15)==1:
        GPIO.output(green, GPIO.LOW)
        gledButton["text"] = "Turn green led on"
    else:
        GPIO.output(green, GPIO.HIGH)
        gledButton["text"] = "Turn green led off"
        
def close():
    GPIO.cleanup()
    win.destroy()
    
rledButton = Button(win, text = 'Turn RedLed on', font = myFont, command = rledToggle, bg='bisque2', height = 1, width = 24)
rledButton.grid(row=0,column=1)
bledButton = Button(win, text = 'Turn BlueLed on', font = myFont, command = bledToggle, bg='bisque2', height = 1, width = 24)
bledButton.grid(row=1,column=1)
gledButton = Button(win, text = 'Turn GreenLed on', font = myFont, command = gledToggle, bg='bisque2', height = 1, width = 24)
gledButton.grid(row=2,column=1)

exitButton = Button(win, text = 'exit', font = myFont, command = close, bg='red', height = 1, width = 6)
exitButton.grid(row=3,column=1)

win.protocol("WN_DELETE_WINDOW", close)

win.mainloop()