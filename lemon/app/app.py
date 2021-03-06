#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年04月01日 星期三 16时20分42秒
from multiprocessing import Process,Pipe,Queue
from threading import Thread
import cv2
import os
import time
from recognize import recognizer_factory,deeplearning_factory

class Data_app(Process):
    '''
    load data
    '''
    def __init__(self,config,cons):
        Process.__init__(self)
        self.config=config
        self.cons=cons
        self.data_path=config['datapath']
    def run(self):
        for file_name in os.listdir(self.data_path):
            file_path=os.path.join(self.data_path,file_name)
            image_data=cv2.imread(file_path)
            [con.send(image_data) for con in self.cons]
            time.sleep(1)
    def terminate(self):
        #[con.send(None) for con in self.cons]
        [con.close for con in self.cons]
        Process.terminate(self)

class DL_app(Process):
    '''
    app for deep learning
    '''
    def __init__(self,config,con,q):
        Process.__init__(self)
        self.config=config
        self.con=con
        self.q=q
        self.factory=deeplearning_factory()
        self.recognizer=self.factory.create_recognizer(config['fruit'])
    def run(self):
        while not self.con.closed:
            data=self.con.recv()
            result=self.recognizer.recognize(data,self.config)
            self.q.put(result)
    def terminate(self):
        self.con.close()
        Process.terminate(self)

class Imgpro_app(Process):
    '''
    app for image processing
    '''
    def __init__(self,config,con,q):
        Process.__init__(self)
        self.config=config
        self.con=con
        self.q=q
        self.factory=recognizer_factory()
        self.recognizer=self.factory.create_recognizer(config['fruit'])
    def run(self):
        while not self.con.closed:
            data=self.con.recv()
            result=self.recognizer.recognize(data,self.config)
            self.q.put(result)
    def terminate(self):
        self.con.close()
        Process.terminate(self)

class Main_app(Process):
    '''
    main app:
    data load
    deep learning 
    image processing
    '''
    def __init__(self,config,q):
        Process.__init__(self)
        self.config=config
        self.con1=Pipe(duplex=False)
        self.con2=Pipe(duplex=False)
        self.dl_output=Queue()
        self.imgpro_output=Queue()
        self.data_app=Data_app(self.config['data_config'],[self.con1[1],self.con2[1]])
        self.dl_app=DL_app(self.config['img_config'],self.con1[0],self.dl_output)
        self.img_app=Imgpro_app(self.config['img_config'],self.con2[0],self.imgpro_output)
        self.output=q
    def run_app(self):
        if not (self.dl_app.is_alive()):
            self.dl_app.start()
        if not (self.img_app.is_alive()):
            self.img_app.start()
        if not (self.data_app.is_alive()):
            self.data_app.start()
        if not (self.is_alive()):
            self.start()
    def run(self):
        while True:
            dl_result=self.dl_output.get()
            img_result=self.imgpro_output.get()
            #merge result
            self.output.put(img_result)
            #send control 
    def terminate(self):
        if (self.data_app.is_alive()):
            self.data_app.terminate()
        if (self.dl_app.is_alive()):
            self.dl_app.terminate()
        if (self.img_app.is_alive()):
            self.img_app.terminate()
        if (self.is_alive()):
            Process.terminate(self)

class update_gui_app(Thread):
    '''
    update gui
    '''
    def __init__(self,func,q):
        Thread.__init__(self)
        self.func=func
        self.q=q
    def run(self):
        while True:
            result=self.q.get()
            self.func(result)
