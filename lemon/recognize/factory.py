#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年02月29日 星期六 21时47分08秒
from abc import ABCMeta, abstractmethod
from enum import Enum
from fruits import fruits,lemon_status
from lemon_recognizer import lemon_recognizer

import cv2
import numpy as np

class recognizer_factory(object):
    '''
    factory to generate recognizer
    '''
    def create_recognizer(self,fruit_name):
        result=None
        if fruit_name==fruits.lemon:
            result=lemon_recognizer()
        else:
            pass
        return result

class deeplearning_factory(object):
    '''
    factory to generate dl recognizer
    '''
    def create_recognizer(self,fruit_name):
        result=None
        if fruit_name==fruits.lemon:
            result=lemon_recognizer()
        else:
            pass
        return result
