#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年04月28日 星期二 22时04分08秒

from tkinter import *

class Plan:
    def __init__(self,root,config):
        self.config=config
        self.root=Toplevel(root)
        self.root.transient(root)
        self.init_gui()
    def init_gui(self):
        Label(self.root,text="测试").pack()
