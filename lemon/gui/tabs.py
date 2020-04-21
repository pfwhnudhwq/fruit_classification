#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年04月01日 星期三 13时33分23秒

from tkinter import *

class lemon_tab:
    def __init__(self,root,config=None):
        self.config=config
        self.root=root
        self.init_tabs()
        self.current_index=None
    def init_tabs(self):
        self.tabs=[]
        #level tab
        #left
        self.fm_level=Frame(self.root)
        pwleft=PanedWindow(self.fm_level,orient=VERTICAL,width=200)
        pwleft.pack(side=LEFT,fill=BOTH)
        leftframe=LabelFrame(pwleft,text="系统设置")
        pwleft.add(leftframe)
        Label(leftframe,text="持续时间:",font="Helvetic 10").pack(anchor=W,pady=5,padx=5)
        Label(leftframe,text="收果个数:",font="Helvetic 10").pack(anchor=W,pady=5,padx=5)
        Label(leftframe,text="上果率:",font="Helvetic 10").pack(anchor=W,pady=5,padx=5)
        Label(leftframe,text="运行速度:",font="Helvetic 10").pack(anchor=W,pady=5,padx=5)
        #center
        pwcenter=PanedWindow(self.fm_level,orient=VERTICAL)
        pwcenter.pack(side=LEFT,expand=YES,fill=BOTH)
        centerframe=LabelFrame(pwcenter,text="详细统计")
        pwcenter.add(centerframe)
        pwcleft=PanedWindow(centerframe,orient=VERTICAL)
        pwcleft.pack(side=LEFT,expand=YES,fill=BOTH)
        pwcright=PanedWindow(centerframe,orient=VERTICAL)
        pwcright.pack(side=LEFT,expand=YES,fill=BOTH)
        for i in range(4):
            tmp_str="%s级果:"%str(i+1)
            tmp_label_f=Label(pwcleft,text=tmp_str,font="Helvetic 10")
            tmp_label_f.pack(anchor=W,pady=5,padx=5)
            
            tmp_label_n=Label(pwcright,text="出口:",font="Helvetic 10")
            tmp_label_n.pack(anchor=W,pady=5,padx=5)
        #right
        pwright=PanedWindow(self.fm_level,orient=VERTICAL,width=200)
        pwright.pack(side=LEFT,fill=BOTH)
        rightframe=LabelFrame(pwright,text="出口设置")
        pwright.add(rightframe)
        self.spin_list=[]
        for i in range(4):
            tmp_str="%s级果出口"%str(i+1)
            tmp_pane=PanedWindow(rightframe)
            tmp_pane.pack(side=TOP,anchor=W,pady=5)
            Checkbutton(tmp_pane,text=tmp_str,font="Helvetic 10").pack(side=LEFT,padx=10,expand=YES)
            tmp_spin=Spinbox(tmp_pane,width=3,from_=1,to=30,increment=2)
            tmp_spin.pack(side=LEFT,expand=YES,padx=10)
            self.spin_list.append((tmp_pane,tmp_spin))
        #weight tab
        self.fm_weight=Frame(self.root)
        lb_weight=Label(self.fm_weight,text="重量分类尚未开发！")
        lb_weight.pack(expand=YES,fill=BOTH)
        #volume tab
        self.fm_volume=Frame(self.root)
        lb_volume=Label(self.fm_volume,text="体积分类尚未开发！")
        lb_volume.pack(expand=YES,fill=BOTH)
        self.tabs=[self.fm_level,self.fm_weight,self.fm_volume]
    def set_index(self,index):
        if index==self.current_index:
            return
        if index>len(self.tabs):
            return
        if not self.current_index is None:
            self.tabs[self.current_index].pack_forget()
        self.tabs[index].pack(expand=YES,fill=BOTH)
        self.current_index=index

