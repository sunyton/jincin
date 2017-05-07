#coding=utf-8
import video
import time
import re
#import ques
fo = open("list.txt",'r')
list1 = fo.read().split()
length = len(list1)
count = 0
while count <= length:
    username = list1[count]
    print username
    video.hack_video(username)
#    ques.hack_video(username)
    time.sleep(5)
    count = count + 1
    if count >= length:
        break
