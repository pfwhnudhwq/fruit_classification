#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年04月28日 星期二 22时04分08秒

from tkinter import *
from tkinter.ttk import *

class Plan:
    def __init__(self):
        self.root=None
    def init_gui(self,config):
        #root 
        self.root=Toplevel()
        self.root.protocol("WM_DELETE_WINDOW",self.cancel)
        self.root.title("方案设置")
        screenWidth=self.root.winfo_screenwidth()
        screenHeight=self.root.winfo_screenheight()
        w=600
        h=450
        x=(screenWidth-w)/2
        y=(screenHeight-h)/2
        self.root.geometry("%dx%d+%d+%d"%(w,h,x,y))
        self.root.resizable(width=False,height=False)

        #notebook
        self.nb=Notebook(self.root)
        self.nb.pack(padx=10,pady=10,fill=BOTH,expand=YES)

        frame1=Frame(self.root)
        level_list=["级别一","级别二","级别三","级别四"]
        self.cbtn_list=[]
        self.out_list=[]
        for i in range(len(level_list)):
            pw=PanedWindow(frame1)
            tmp_cbtn=Checkbutton(pw,text=level_list[i])
            tmp_cbtn.pack(side=LEFT,padx=20)
            Label(pw,text="出口：").pack(side=LEFT)
            optuple=("1","1","2","3","4","5")
            var=StringVar(pw)
            opt=OptionMenu(pw,var,*optuple)
            opt.pack(side=LEFT)
            pw.pack(side=TOP,anchor=W,padx=10,pady=10)

        self.nb.add(frame1,text="级别方案")
        frame2=Frame(self.root)
        frame3=Frame(self.root)
        self.nb.add(frame2,text="重量方案")
        self.nb.add(frame3,text="体积方案")

        #btn
        pw_btn=PanedWindow(self.root)
        pw_btn.pack(side=TOP,fill=BOTH,padx=10,pady=10)
        btn_confirm=Button(pw_btn,text="确认",command=self.confirm)
        btn_cancel=Button(pw_btn,text="取消",command=self.cancel)
        btn_confirm.pack(side=RIGHT)
        btn_cancel.pack(side=RIGHT)

    def cancel(self):
        self.root.destroy()
        self.root=None
    def confirm(self):
        self.root.destroy()
        self.root=None
    def show(self,config):
        if not self.root is None:
            self.root.destroy()
            self.root=None
        else:
            self.init_gui(config)

