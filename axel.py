#!/usr/bin/env python3
#---coding---utf_8---#
import os, getpass, time
import tkinter as tk

root = tk.Tk()

top = tk.Tk()
top.title("AXEL Download manager GUI")



L1 = tk.Label(top, text="Paste the download link:")
L1.pack()
E1 = tk.Entry(top, bd =5,width=50)

E1.pack()



def start():
   url = E1.get()
   os.system("axel %s" % url )
   
B = tk.Button(top, text ="Download now!", command=start)


B.pack()

top.mainloop()
