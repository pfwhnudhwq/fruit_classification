#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: xuchaoqian
# Created Time: 2020年02月29日 星期六 21时47分08秒
from abc import ABCMeta, abstractmethod
from fruits import fruits,lemon_status
from recognizer import recognizer
import cv2
import numpy as np

class lemon_recognizer(recognizer):
    '''
    lemon recognizer
    '''
    def __init__(self):
        super(lemon_recognizer,self).__init__()
        #perfect lemon color range
        #H(0-255)
        self.hmin=19
        self.hmax=34
        #S(0-255)
        self.smin=43
        self.smax=255
        #V(0-255)
        self.vmin=46
        self.vmax=255
        self.countThresh=1000
    def recognize(self,data,config):
        numRegion=len(config.points)
        if (numRegion<1):
            return
        resultList=[]
        for point in config.points:
            roi=data[point[1]:point[1]+config.height,point[0]:point[0]+config.width,:]
            result=self.recognize_roi(roi)
            resultList.append(result.value)
        return resultList
        #cv2.imshow("src",data)
        #cv2.waitKey(0)

    def recognize_roi(self,data):
        #rgb to hsv
        hsv=cv2.cvtColor(data,cv2.COLOR_BGR2HSV)
        lower=np.array([self.hmin,self.smin,self.vmin])
        upper=np.array([self.hmax,self.smax,self.vmax])
        thresh=cv2.inRange(hsv,lower,upper)
        #there is no lemon!
        if(np.sum(thresh/255.0)<self.countThresh):
            return lemon_status.error
        #find contours
        _,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        maxIndex=-1
        maxArea=0
        #the largest area is lemon!
        for i in range(len(contours)):
            area=cv2.contourArea(contours[i])
            if(area>maxArea):
                maxArea=area
                maxIndex=i
        if(maxIndex==-1):
            return lemon_status.error
        #contours of lemon inside
        tmpContours=[]
        for i in range(len(contours)):
            if(hierarchy[0][i][3]==maxIndex):
                if(cv2.contourArea(contours[i])>2):
                    tmpContours.append(contours[i])

        #lemon recognize result
        sumArea=sum([cv2.contourArea(contour) for contour in tmpContours])
        numDefects=len(tmpContours)
        result=lemon_status.error
        if(numDefects<=2 and sumArea<=20):
            result=lemon_status.perfect
        elif(numDefects<=6 and sumArea<=60):
            result=lemon_status.first
        elif(numDefects<=20 and sumArea<=200):
            result=lemon_status.second
        elif(numDefects<=40 and sumArea<=400):
            result=lemon_status.third
        else:
            result=lemon_status.rubbish

        #show result
        #cv2.drawContours(data,tmpContours,-1,(0,0,255),1)
        #x,y,w,h = cv2.boundingRect(contours[maxIndex])
        #cv2.rectangle(data,(x,y),(x+w,y+h),(0,255,0),2)
        #cv2.putText(data, str(result.value), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2) 
        #cv2.putText(data,str("%d,%d"%(numDefects,sumArea)),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        #cv2.imshow("contours",thresh)
        #cv2.imshow("src",data)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        return result

