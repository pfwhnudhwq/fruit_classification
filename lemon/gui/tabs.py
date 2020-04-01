#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年04月01日 星期三 13时33分23秒

from Tkinter import *

class lemon_tab:
    def __init__(self,config):
        self.config=config
        self.tabs=None
    def get_config(self):
        return self.config
    def set_config(self,config):
        self.config=config
    def set_tabs(self,root):
        if not self.tabs is None:
            return
        tab_defect=Frame(root,bg='green')
        root.add(tab_defect,text='defect')

        tab_volume=Frame(root,bg='red')
        root.add(tab_volume,text='volume')

        tab_weight=Frame(root,bg='black')
        root.add(tab_weight,text='weight')
        self.tabs=[tab_defect,tab_volume,tab_weight]
    def set_value(self):
        pass
