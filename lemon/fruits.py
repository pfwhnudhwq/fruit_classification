#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年03月01日 星期日 13时53分10秒

from enum import Enum

class fruits(Enum):
    '''
    fruits enum
    '''
    lemon=1

class lemon_status(Enum):
    '''
    lemon status
    '''
    error=-1
    perfect=0
    first=1
    second=2
    third=3
    rubbish=4

