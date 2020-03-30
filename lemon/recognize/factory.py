#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年02月29日 星期六 21时47分08秒
from abc import ABCMeta, abstractmethod
from enum import Enum
from recognizer import recognizer
from lemon_recognizer import *

import cv2
import numpy as np

class recognizer_factory(object):
    '''
    factory to generate recognizer
    '''
    def create_recognizer(self,fruit_name):
        result=recognizer()
        if fruit_name=='lemon':
            result=lemon_recognizer()
        else:
            print("no such recognizer!")
        return result

class deeplearning_factory(object):
    '''
    factory to generate dl recognizer
    '''
    def create_recognizer(self,fruit_name):
        result=recognizer()
        if fruit_name=='lemon':
            result=dl_lemon_recognizer()
        else:
            print("no such recognizer!")
        return result
