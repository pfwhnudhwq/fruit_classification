#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年03月30日 星期一 21时26分09秒

from config import load_config 
from gui import Main_gui
import os

if __name__=="__main__":
    config_path="yaml/config.yaml"
    config=load_config(config_path)
    gui=Main_gui(config)
    gui.show()
