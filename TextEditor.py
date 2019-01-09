import sys
from tkinter import *
import tkinter.filedialog
root=Tk('Text Editor')
text=Text(root)
text.grid()
def saveas():
    global text
    t=text.get("1.0",'end-1c')
    location=tkinter.filedialog.asksaveasfilename()
    file1=open(location, 'w+')
    file1.write(t)
    file1.close()
button=Button(root, text="save", command=saveas)
button.grid()
root.mainloop() #infinite loop that starts the process
