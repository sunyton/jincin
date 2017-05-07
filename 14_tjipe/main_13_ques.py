#coding=utf-8
import ques_13
import time
import re
fo = open("list.txt",'r')
list1 = fo.read().split()
length = len(list1)
count = 0
while count <= length:
    username = list1[count]
    print username
    ques_13.hack_video(username)
    time.sleep(5)
    count = count + 1
    if count >= length:
        break
