#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年02月29日 星期六 21时47分08秒
from abc import ABCMeta,abstractmethod
class recognizer(object):
    '''
    abstract class
    '''
    def __init__(self):
        pass
    @abstractmethod
    def recognize(self,data,config):
        pass

