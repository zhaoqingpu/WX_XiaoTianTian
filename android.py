# -*- coding: UTF-8 -*-
import aircv as ac
import subprocess
import os
import json
import time

def matchImg(imgsrc,imgobj,confidence=0.7):
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc,imobj,confidence)
    if match_result is not None:
        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])
    return match_result


def screenshot():
    filePath = "/sdcard/waigua.png"
    runAdb("shell screencap -p "+filePath)
    runAdb("pull "+filePath+" android.png")
    return "android.png"


def runAdb(cmd):
    adb_path = "/Users/xxxxx/Library/Android/sdk/platform-tools/adb"
    print(adb_path+" "+cmd)
    #pipe = subprocess.Popen(adb_path+" "+cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process = os.popen(adb_path+" "+cmd)
    output = process.read()
    #print(output)
    return

def start_run():
    st = time.time()
    screenshot()
    et = time.time()
    print("截图耗时："+ str(et - st) )
    st = time.time()
    result = matchImg("android.png","b.png")
    et = time.time()
    print("找图耗时："+str((et - st)))
    if result is not None:
        print(result)
        print(str(result['result'][0])+"-"+str(result['result'][1]))
        print(str(result['confidence']))
        if result['confidence']>0.8 :
            runAdb("shell input tap "+str(result['result'][0])+" "+str(result['result'][1]))
            time.sleep(0.2)
            runAdb("shell input tap "+str(result['result'][0])+" "+str(result['result'][1]))
            time.sleep(30)
        else :
            print(str(result['confidence'])+"- small fail")
    else:
        print("not found")

while True:
    start_run()
