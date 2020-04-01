#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年03月30日 星期一 21时27分35秒

from Tkinter import *
from app import *

class Main_gui:
    def __init__(self,config):
        self.config=config['gui_config']
        #load gui according configuration
        self.app=Main_app(config)
        #init gui
        self.root=Tk()
        self.width=self.config['width']
        self.height=self.config['height']
        self.init_gui()

    def init_gui(self):
        #main window
        self.init_main_window()
        #menu
        self.init_menu()
        #compoent
        self.init_compoent()
        #fm = Frame(self.root)
        #Button(fm, text='Top').pack(side=TOP, anchor=W, fill=X, expand=YES)
        #Button(fm, text='Center').pack(side=TOP, anchor=W, fill=X, expand=YES)
        #Button(fm, text='Bottom').pack(side=TOP, anchor=W, fill=X, expand=YES)
        #fm.pack(side=LEFT, fill=BOTH, expand=YES)

        #fm2 = Frame(self.root)
        #Button(fm2, text='Left').pack(side=LEFT)
        #Button(fm2, text='This is the Center button').pack(side=LEFT)
        #Button(fm2, text='Right',command=self.app.start).pack(side=LEFT)        
        #fm2.pack(side=LEFT, padx=10)

    def init_main_window(self):
        self.root.title("fruit classification")
        self.root.geometry(str(self.width)+"x"+str(self.height))
        self.root.resizable(width=False,height=False)
    def init_menu(self):
        menubar=Menu(self.root)
        menu_file=Menu(menubar,tearoff=False)
        for item in ['fuck','quit']:
            menu_file.add_command(label=item,command=None)
        menubar.add_cascade(label='file',menu=menu_file)

        menu_edit=Menu(menubar,tearoff=False)
        for item in ['fuck','quit']:
            menu_edit.add_command(label=item,command=self.quit)
        menubar.add_cascade(label='edit',menu=menu_edit)
        self.root.config(menu=menubar)
    def init_compoent(self):
        #status
        fm_status=Frame(self.root)
        fm_status_1=Frame(fm_status)
        Label(fm_status_1,text="fruit:").pack(side=TOP,fill=BOTH,anchor=W)
        Label(fm_status_1,text="status:").pack(side=TOP,fill=BOTH,anchor=W)
        fm_status_2=Frame(fm_status)
        Label(fm_status_2,text="fruit:").pack(side=TOP,fill=BOTH,anchor=W)
        Label(fm_status_2,text="status:").pack(side=TOP,fill=BOTH,anchor=W)
        fm_status_3=Frame(fm_status)
        Label(fm_status_3,text="fruit:").pack(side=TOP,fill=BOTH,anchor=W)
        Label(fm_status_3,text="status:").pack(side=TOP,fill=BOTH,anchor=W)
        fm_status_4=Frame(fm_status)
        Label(fm_status_4,text="fruit:").pack(side=TOP,fill=BOTH,anchor=W)
        Label(fm_status_4,text="status:").pack(side=TOP,fill=BOTH,anchor=W)
        fm_status_1.pack(side=LEFT,expand=YES,anchor=W)
        fm_status_2.pack(side=LEFT,expand=YES,anchor=W)
        fm_status_3.pack(side=LEFT,expand=YES,anchor=W)
        fm_status_4.pack(side=LEFT,expand=YES,anchor=W)
        fm_status.pack(side=TOP,fill=BOTH)
        #buttons
        fm_buttons=Frame(self.root)
        Button(fm_buttons,text="start").pack(side=LEFT,expand=YES,anchor=E)
        Button(fm_buttons,text="stop").pack(side=LEFT,expand=YES,anchor=W)
        fm_buttons.pack(side=TOP,fill=BOTH,pady=10)
        #tag
        #quit

    def show(self):
        self.root.mainloop()
    def quit(self):
        self.app.stop()
        self.root.quit()
        
