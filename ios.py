# -*- coding: UTF-8 -*-
import wda
import aircv as ac
import subprocess
import os
import json
import time
import random

driver = wda.Client()
session = driver.session()

def matchImg(imgsrc,imgobj,confidence=0.7):
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc,imobj,confidence)
    if match_result is not None:
        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])
    return match_result


def screenshot():
    driver.screenshot("ios.png")

def tab(x, y):
    x = x+rdm(6)
    y = y+rdm(8)
    print(str(x)+"_"+str(y))
    session.tap(x/2, y/2)

def rdm(x):
    return int(random.random()*x-x/2)

def start_run():
    time.sleep(3)
    st = time.time()
    screenshot()
    et = time.time()
    print("截图耗时："+ str(et - st) )
    st = time.time()
    result = matchImg("ios.png","c.png")
    et = time.time()
    print("找图耗时："+str((et - st)))
    if result is not None:
        print(result)
        print(str(result['result'][0])+"-"+str(result['result'][1]))
        print(str(result['confidence']))
        if result['confidence']>0.8 :
            tab(result['result'][0],result['result'][1])
            time.sleep(40)
        else :
            print(str(result['confidence'])+"- small fail")
    else:
        print("not found")

while True:
   start_run()
