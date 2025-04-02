import tkinter as tk
from gpiozero import LED
root = tk.Tk()
root.title("Traffic Control station")
root.geometry("900x600")
import tkinter.font as tkFont

#hardware
redLed = LED(27)
greenLed = LED(22)
yellowLed = LED(17) 

#my functions
def RedOn():
        redLed.on()
        greenLed.off()
        yellowLed.off()
def YellowOn():
        yellowLed.on()
        greenLed.off()
        redLed.off()
def GreenOn():
        greenLed.on()
        yellowLed.off()
        redLed.off()
myFont = tkFont.Font(family  = "helvetica", size = 12, weight = "bold")

redButton = tk.Button(root, text = "Red Light", font = myFont, command = RedOn, bg = "red", fg = "white", width = 25, height = 2)
GreenButton = tk.Button(root, text = "Green Light", font = myFont, command = GreenOn, bg = "green", fg = "white", width = 25, height = 2)
yellowButton = tk.Button(root, text = "Yellow Light", font = myFont, command = YellowOn, bg = "yellow", fg = "white", width = 25, height = 2)
redButton.pack(pady=10)
GreenButton.pack(pady=10)
yellowButton.pack(pady=10)
root.mainloop()


