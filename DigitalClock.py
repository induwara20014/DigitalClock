from tkinter import Tk, Label
import time 

root = Tk()
root.title("Clock")

def present_time():
    display_time = time.strftime("%I:%M:%S %p")  # Corrected %P to %p
    digi_clock.config(text=display_time)
    digi_clock.after(200, present_time)

digi_clock = Label(root, font=("arial", 150), bg="red", fg="black")
digi_clock.pack()

present_time()
root.mainloop()

