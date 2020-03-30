#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年02月29日 星期六 21时59分34秒

from recognize import recognizer_factory,deeplearning_factory
from abc import ABCMeta,abstractmethod
from multiprocessing import Process,Pipe,Queue
from fruits import *

import os
import cv2
import time

class App(object):
    '''
    app parent
    '''
    def __init__(self):
        self.processes=[]
        print("%s app init..."%type(self).__name__)
    def start(self,args=()):
        print("%s app start..."%type(self).__name__)
        process=Process(target=self.callback,args=args)
        self.processes.append(process)
        process.start()
    def join(self):
        print("wait for %s to complete"%type(self).__name__)
        for process in self.processes:
            process.join()
        self.processes=[]
    def stop(self):
        print("%s app stop..."%type(self).__name__)
        for process in self.processes:
            process.terminate()
        self.processes=[]
    @abstractmethod
    def callback(self):
       print("%s app has no function to execution!"%type(self).__name__)

class Data_app(App):
    '''
    data reader
    '''
    def __init__(self,config):
        super(Data_app,self).__init__()
        self.config=config
        self.data_path=config['datapath']
    def callback(self,con):
        for file_name in os.listdir(self.data_path):
            file_path=os.path.join(self.data_path,file_name)
            image_data=cv2.imread(file_path)
            con[0].send(image_data)
            con[1].send(image_data)
            time.sleep(1)

class Main_app(App):
    '''
    main application.
    '''
    def __init__(self,config):
        super(Main_app,self).__init__()
        self.config=config
        self.data_app=Data_app(config['data_config'])
        self.dl_app=DL_app(config['img_config'])
        self.img_app=Imgpro_app(config['img_config'])
        self.con=Pipe()
        self.dl_output=Queue()
        self.imgpro_output=Queue()
    def callback(self):
        self.dl_app.start((self.con,self.dl_output))
        self.img_app.start((self.con,self.imgpro_output))
        self.data_app.start((self.con,))
        #merge result
        while True:
            print self.dl_output.get()
            print self.imgpro_output.get()
    def stop(self):
        self.con[0].close()
        self.con[1].close()
        self.dl_app.stop()
        self.img_app.stop()
        self.data_app.stop()
        super(Main_app,self).stop()

class DL_app(App):
    '''
    deep learning application
    '''
    def __init__(self,config):
        super(DL_app,self).__init__()
        self.config=config
        self.factory=deeplearning_factory()
        self.recognizer=self.factory.create_recognizer(config['fruit'])
    def callback(self,con,q):
        while not con[0].closed:
            data=con[0].recv()
            result=self.recognizer.recognize(data,self.config)
            q.put(result)

class Imgpro_app(App):
    '''
    image processing app.
    '''
    def __init__(self,config):
        super(Imgpro_app,self).__init__()
        self.config=config
        self.factory=recognizer_factory()
        self.recognizer=self.factory.create_recognizer(config['fruit'])
    def callback(self,con,q):
        while not con[1].closed:
            data=con[1].recv()
            result=self.recognizer.recognize(data,self.config)
            q.put(result)

