#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年03月27日 星期五 18时09分40秒
import yaml

def load_config(path):
    config=None
    with open(path,"r") as file:
        data=file.read()
        data=yaml.load(data)
        config=data
    return config
    
if __name__=="__main__":
    #default config
    #gui
    result={}
    gui_config={
            'width':800,
            'height':640,
            }
    #application config
    app_config={
            }
    #image processing config
    img_config={
            'fruit':'lemon',
            'points':[(16,95),(171,95),(326,95),(481,95),(636,95),(791,95),(946,95),(1101,95)],
            'width':145,
            'height':185
            }
    #data config
    data_config={
            'datapath':'../lemon_pic'
            }
    result['gui_config']=gui_config
    result['app_config']=app_config
    result['img_config']=img_config
    result['data_config']=data_config
    
    with open("default.yaml","w") as file:
        yaml.dump(result,file)
