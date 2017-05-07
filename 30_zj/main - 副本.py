#coding=utf-8
import video_82_40
import time
import ques_82_40
fo = open("list.txt",'r')
list1 = fo.read().split()
length = len(list1)
count = 0
while count <= length:
    username = list1[count]
    print username
    video_82_40.hack_video(username)
    ques_82_40.ques(username)
    time.sleep(5)
    count = count + 1
    if count >= length:
        break
