#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年04月01日 星期三 16时20分42秒
from multiprocessing import Process,Pipe,Queue
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
            if data is None:
                return
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
            if data is None:
                return
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
    def __init__(self,config):
        Process.__init__(self)
        self.config=config
        self.con1=Pipe(duplex=False)
        self.con2=Pipe(duplex=False)
        self.dl_output=Queue()
        self.imgpro_output=Queue()
        self.data_app=Data_app(self.config['data_config'],[self.con1[1],self.con2[1]])
        self.dl_app=DL_app(self.config['img_config'],self.con1[0],self.dl_output)
        self.img_app=Imgpro_app(self.config['img_config'],self.con2[0],self.imgpro_output)
    def run_app(self):
        self.dl_app.start()
        self.img_app.start()
        self.data_app.start()
        self.start()
    def run(self):
        while True:
            print self.dl_output.get()
            print self.imgpro_output.get()
    def terminate(self):
        self.data_app.terminate()
        self.dl_app.terminate()
        self.img_app.terminate()
        Process.terminate(self)
