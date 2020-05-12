#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年03月01日 星期日 13时53分10秒

from enum import Enum


class lemon_status(Enum):
    '''
    lemon status
    '''
    # 空
    error = -1
    # 完美果
    perfect = 0
    # 一级果
    first = 1
    # 二级果
    second = 2
    # 三级果
    third = 3
    # 干果、次品
    rubbish = 4
    # 果蒂
    goti = 5


class apple_status(Enum):
    '''
    apple status
    '''
    error = -1
