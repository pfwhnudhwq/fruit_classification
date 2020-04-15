#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年03月30日 星期一 21时27分35秒

from tkinter import *
from tkinter.ttk import Notebook
from app import *
from .tabs import lemon_tab
from multiprocessing import Queue
import cv2
import numpy as np
from PIL import Image,ImageTk

class Main_gui:
    def __init__(self,config):
        self.config=config
        #load gui according configuration
        self.output=Queue()
        self.app=Main_app(config,self.output)
        #update gui thread
        self.update_app=update_gui_app(self.update,self.output)
        self.update_app.setDaemon(True)
        self.update_app.start()
        #init gui
        self.root=Tk()
        self.tabs=lemon_tab(config)
        self.width=self.config['gui_config']['width']
        self.height=self.config['gui_config']['height']
        self.init_gui()

    def init_gui(self):
        #main window
        self.init_main_window()
        #menu
        self.init_menu()
        #compoent
        self.init_compoent()

    def init_main_window(self):
        self.root.title("fruit classification")
        self.root.geometry(str(self.width)+"x"+str(self.height))
        self.root.resizable(width=False,height=False)

    def init_menu(self):
        menubar=Menu(self.root)
        menu_file=Menu(menubar,tearoff=False)
        for item in self.config['gui_config']['fruit_list']:
            menu_file.add_command(label=item,command=None)
        menubar.add_cascade(label='fruit',menu=menu_file)

        menu_edit=Menu(menubar,tearoff=False)
        for item in ['fuck','quit']:
            menu_edit.add_command(label=item,command=self.quit)
        menubar.add_cascade(label='edit',menu=menu_edit)
        self.root.config(menu=menubar)

    def init_compoent(self):
        #left frame
        fm_left=Frame(self.root)
        fm_left.pack(side=LEFT,fill=BOTH)
        #ad frame
        fm_ad=Frame(fm_left)
        fm_ad.pack(side=TOP,fill=BOTH)
        Label(fm_ad,text="联系人：曾志华").pack(padx=20,anchor=W)
        Label(fm_ad,text="联系电话：13973774745").pack(padx=20,anchor=W)
        #tags frame
        fm_tags=Frame(fm_left,pady=250)
        fm_tags.pack(side=TOP,fill=BOTH)
        Button(fm_tags,width=5,height=1,text="级别",relief=SUNKEN).pack(side=TOP,anchor=E)
        Button(fm_tags,width=5,height=1,text="重量").pack(side=TOP,anchor=E)
        Button(fm_tags,width=5,height=1,text="体积").pack(side=TOP,anchor=E)
        #right frame
        fm_right=Frame(self.root)
        fm_right.pack(side=LEFT,fill=BOTH)
        #image
        img=np.zeros((200,640),dtype=np.uint8)
        img=Image.fromarray(img)
        img=ImageTk.PhotoImage(img)
        self.label_img=Label(fm_right,image=img)
        self.label_img.image=img
        self.label_img.pack(side=TOP)
        #status
        fm_status=Frame(fm_right)
        self.label_fruit_list=[]
        self.label_status_list=[]
        for i in range(len(self.config['img_config']['points'])):
            fm_tmp=Frame(fm_status)
            label_fruit=Label(fm_tmp,text="级别：")
            label_status=Label(fm_tmp,text="体积：")
            label_fruit.pack(side=TOP,expand=YES,anchor=W)
            label_status.pack(side=TOP,expand=YES,anchor=W)
            fm_tmp.pack(side=LEFT,expand=YES,anchor=W)
            self.label_fruit_list.append(label_fruit)
            self.label_status_list.append(label_status)
        fm_status.pack(side=TOP,fill=BOTH)
        #buttons
        fm_buttons=Frame(fm_right)
        self.btn_start=Button(fm_buttons,text="start",command=self.start)
        self.btn_stop=Button(fm_buttons,text="stop",state=DISABLED,command=self.stop)
        self.btn_start.pack(side=LEFT,expand=YES,anchor=E)
        self.btn_stop.pack(side=LEFT,expand=YES,anchor=W)
        fm_buttons.pack(side=TOP,fill=BOTH,pady=10)
        #tab
        fm_config=Frame(fm_right)
        fm_config.pack(side=TOP,fill=BOTH)
        #quit
        fm_quit=Frame(fm_right)
        Button(fm_quit,text="save").pack(side=RIGHT)
        Button(fm_quit,text="reset").pack(side=RIGHT)
        fm_quit.pack(side=BOTTOM,fill=BOTH,pady=10)

    def update(self,result):
        #update gui
        #update status
        fruit_label="级别："+self.config['img_config']['fruit']
        for i in range(len(self.config['img_config']['points'])):
            self.label_fruit_list[i].config(text=fruit_label)
            self.label_status_list[i].config(text="体积："+str(result[0][i]))
        #update image
        img=cv2.resize(result[1],(640,200))
        img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        img=Image.fromarray(img)
        img=ImageTk.PhotoImage(image=img)
        self.label_img.config(image=img)
        self.label_img.image=img
        #update tabs
        #self.tabs.update()
    def start(self):
        if not (self.app._popen is None):
            self.app.terminate()
            self.app=Main_app(self.config,self.output)
        self.app.run_app()
        self.btn_start.config(state=DISABLED)
        self.btn_stop.config(state=NORMAL)
    def stop(self):
        self.app.terminate()
        self.btn_start.config(state=NORMAL)
        self.btn_stop.config(state=DISABLED)
    def show(self):
        self.root.mainloop()
    def quit(self):
        self.stop()
        self.root.quit()
        
