#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年03月01日 星期日 13时53分10秒

from enum import Enum
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

class apple_status(Enum):
    '''
    apple status
    '''
    error=-1

