#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 技术支持：https://www.jianshu.com/u/69f40328d4f0 
# 技术支持 https://china-testing.github.io/
# https://github.com/china-testing/python-api-tesing/blob/master/practices/tk/tk1.py
# 项目实战讨论QQ群630011153 144081101
# CreateDate: 2018-11-27

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()   

# Add a title       
win.title("Python GUI")  

# Modify adding a Label
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

# Modified Button Click Function
def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + 
                     number_chosen.get())

# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)                                 # <= change column to 2

# Creating three checkbuttons
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(3)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)                     

# GUI Callback function 
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   


# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold",  "Red"]   

# We have also changed the callback function to be zero-based, using the list 
# instead of module-level global variables 
# Radiobutton Callback
def radCall():
    radSel=radVar.get()
    win.configure(background=colors[radSel])

# create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
radVar.set(99)                                 
 
# Now we are creating all three Radiobutton widgets within one loop
for col in range(3):                             
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=5, sticky=tk.W) 

# Using a scrolled Text control    
scr = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

name_entered.focus()      # Place cursor into name Entry

#======================
# Start GUI
#======================
win.mainloop()