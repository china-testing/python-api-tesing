#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 技术支持：https://www.jianshu.com/u/69f40328d4f0 
# 技术支持 https://china-testing.github.io/
# https://github.com/china-testing/python-api-tesing/blob/master/practices/tk/tk3.py
# 项目实战讨论QQ群630011153 144081101
# CreateDate: 2018-11-29


import tkinter as tk

root = tk.Tk()
root.title('tkinter控件')
#create a frame widget for placing menu
my_menu_bar = tk.Frame(root, relief='raised', bd=2)
my_menu_bar.pack(fill=tk.X)

# Create  Menu Widget 1 and Sub Menu 1
my_menu_button = tk.Menubutton(
    my_menu_bar,
    text='菜单1',
)
my_menu_button.pack(side=tk.LEFT)
#menu widget
my_menu = tk.Menu(my_menu_button, tearoff=0)
my_menu_button['menu'] = my_menu
my_menu.add('command', label='子菜单1')  #Add Sub Menu 1

# Create  Menu2 and Submenu2
menu_button_2 = tk.Menubutton(
    my_menu_bar,
    text='菜单2',
)
menu_button_2.pack(side=tk.LEFT)
my_menu_2 = tk.Menu(menu_button_2, tearoff=0)
menu_button_2['menu'] = my_menu_2
my_menu_2.add('command', label='子菜单2')  # Add Sub Menu 2

#
#
# my_frame_1  and its contents
#

# creating a frame (my_frame_1)
my_frame_1 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
my_frame_1.pack(side=tk.LEFT)

# add label to to my_frame_1
tk.Label(my_frame_1, text='标签').pack()

#add entry widget to my_frame_1
tv = tk.StringVar()  #discussed later
tk.Entry(my_frame_1, textvariable=tv).pack()
tv.set('I am an entry widget')

#add button widget to my_frame_1
tk.Button(my_frame_1, text='tk.Button widget').pack()

#add check button widget to my_frame_1
tk.Checkbutton(my_frame_1, text='Checktk.Button Widget').pack()

#add radio buttons to my_frame_1
tk.Radiobutton(my_frame_1, text='Radio tk.Button  Un', value=1).pack()
tk.Radiobutton(my_frame_1, text='Radio tk.Button  Dos', value=2).pack()
tk.Radiobutton(my_frame_1, text='Radio tk.Button  Tres', value=3).pack()

#tk.OptionMenu Widget
tk.Label(my_frame_1, text='Example of tk.OptionMenu Widget:').pack()
tk.OptionMenu(my_frame_1, '', "Option A", "Option B", "Option C").pack()

#adding my_image image
tk.Label(my_frame_1, text='Image Fun with Bitmap Class:').pack()
my_image = tk.BitmapImage(file="gir.xbm")
my_label = tk.Label(my_frame_1, image=my_image)
my_label.image = my_image  # keep a reference!
my_label.pack()

#
#
# frame2 and widgets it contains.
#
#

#create another frame(my_frame_2) to hold a list box, Spinbox Widget,Scale Widget, :
my_frame_2 = tk.Frame(root, bd=2, relief=tk.GROOVE)
my_frame_2.pack(side=tk.RIGHT)

#add Photimage Class Widget to my_frame_2
tk.Label(
    my_frame_2, text='Image displayed with \nPhotoImage class widget:').pack()
dance_photo = tk.PhotoImage(file='dance.gif')
dance_photo_label = tk.Label(my_frame_2, image=dance_photo)
dance_photo_label.image = dance_photo
dance_photo_label.pack()

#add my_listbox widget to my_frame_2
tk.Label(my_frame_2, text='Below is an example of my_listbox widget:').pack()
my_listbox = tk.Listbox(my_frame_2, height=4)
for line in ['Listbox Choice 1', 'Choice 2', 'Choice 3', 'Choice 4']:
  my_listbox.insert(tk.END, line)
my_listbox.pack()

#spinbox widget
tk.Label(my_frame_2, text='Below is an example of spinbox widget:').pack()
tk.Spinbox(my_frame_2, values=(1, 2, 4, 8, 10)).pack()

#scale widget
tk.Scale(
    my_frame_2, from_=0.0, to=100.0, label='Scale widget',
    orient=tk.HORIZONTAL).pack()

#LabelFrame
label_frame = tk.LabelFrame(
    my_frame_2, text="LabelFrame Widget", padx=10, pady=10)
label_frame.pack(padx=10, pady=10)
tk.Entry(label_frame).pack()

#message widget
tk.Message(my_frame_2, text='I am a Message widget').pack()

#
#
# tk.Frame 3
#
#

my_frame_3 = tk.Frame(root, bd=2, relief=tk.SUNKEN)

#text widget and associated tk.Scrollbar widget
my_text = tk.Text(my_frame_3, height=10, width=40)
file_object = open('textcontent.txt', encoding='utf-8')
file_content = file_object.read()
file_object.close()
my_text.insert(tk.END, file_content)
my_text.pack(side=tk.LEFT, fill=tk.X, padx=5)

#add scrollbar widget to the text widget
my_scrollbar = tk.Scrollbar(my_frame_3, orient=tk.VERTICAL, command=my_text.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
my_text.configure(yscrollcommand=my_scrollbar.set)
my_frame_3.pack()

#
#
# tk.Frame 4
#
#
#create another frame(my_frame_4)
my_frame_4 = tk.Frame(root)
my_frame_4.pack()

my_canvas = tk.Canvas(my_frame_4, bg='white', width=340, height=80)
my_canvas.pack()
my_canvas.create_oval(20, 15, 60, 60, fill='red')
my_canvas.create_oval(40, 15, 60, 60, fill='grey')
my_canvas.create_text(
    130, 38, text='I am a tk.Canvas Widget', font=('arial', 8, 'bold'))

#
#
# A paned window widget
#
#

tk.Label(root, text='Below is an example of Paned window widget:').pack()
tk.Label(
    root,
    text='Notice you can adjust the size of each pane by dragging it').pack()
my_paned_window_1 = tk.PanedWindow()
my_paned_window_1.pack(fill=tk.BOTH, expand=2)
left_pane_text = tk.Text(my_paned_window_1, height=6, width=15)
my_paned_window_1.add(left_pane_text)
my_paned_window_2 = tk.PanedWindow(my_paned_window_1, orient=tk.VERTICAL)
my_paned_window_1.add(my_paned_window_2)
top_pane_text = tk.Text(my_paned_window_2, height=3, width=3)
my_paned_window_2.add(top_pane_text)
bottom_pane_text = tk.Text(my_paned_window_2, height=3, width=3)
my_paned_window_2.add(bottom_pane_text)

root.mainloop()
