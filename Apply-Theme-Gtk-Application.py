#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coded by : abosloh
# email : abosloh.654@gmail.com
# page : https://github.com/abosloh

import pygtk
pygtk.require("2.0")
import gtk

# replace style gtk
# change abosloh to your name
gtk.rc_parse('/home/abosloh/.themes/Faience/gtk-2.0/gtkrc')

win = gtk.Window(gtk.WINDOW_TOPLEVEL) # create window
win.resize(300,300) # resize window

box = gtk.VBox() # create box

button1 = gtk.Button("Click!") # create button1
box.pack_start(button1) # add button1 into box
button2 = gtk.Button("Click!") # create button2
box.pack_start(button2) # add button2 into box
button3 = gtk.Button("Click!") # create button3
box.pack_start(button3) # add button3 into box
entry = gtk.Entry()# create entry
box.pack_start(entry)# add entry into box

win.add(box) # add box into window
win.show_all() # show window
gtk.main()
