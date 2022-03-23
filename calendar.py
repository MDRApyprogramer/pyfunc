# imports

from datetime import datetime
from tkinter import *
root = Tk()
clock = datetime.now()
c = clock.strftime('%I:%M:%S.%p')
calendar = clock.strftime('%Y/%b/%d')
Label(text = c, fg = 'cyan', bg = 'black', font = ('ds-digital',50)).pack()
Label(text = calendar, fg = 'cyan', bg = 'black', font = ('ds-digital',50)).pack()
root.geometry('374x150')
root.resizable(False, False)
root.mainloop()