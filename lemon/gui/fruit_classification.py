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

    def show(self):
        self.app.start()
        #show gui
        self.root.mainloop()
        
