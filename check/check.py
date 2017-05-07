# coding=utf-8
import urllib,urllib2
import cookielib
import re
import hashlib
from bs4 import BeautifulSoup
import requests
import time
#username = raw_input("username: ")
#password = raw_input("psaaword: ")
#username = raw_input("username: ")
def check(username):
    password = '123456'
    m = hashlib.md5()
    m.update(password)
    login_id = m.hexdigest()
    #cookie处理
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    #本地调试
    proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8080'})
    postdata ='$$CDORequest$$=%3CCDO%3E%3CSTRF%20N%3D%22strServiceName%22%20V%3D%22UserService%22%2F%3E%3CSTRF%20N%3D%22strLoginId%22%20V%3D%22'+ username +'%22%2F%3E%3CSTRF%20N%3D%22strTransName%22%20V%3D%22SSOLogin%22%2F%3E%3CSTRF%20N%3D%22strPassword%22%20V%3D%22'+login_id+'%22%2F%3E%3CSTRF%20N%3D%22strVerifyCode%22%20V%3D%22%22%2F%3E%3CSTRF%20N%3D%22bIsCookieLogin%22%20V%3D%22change%22%2F%3E%3CSTRF%20N%3D%22Sessioncheck%22%20V%3D%22sessionErr%22%2F%3E%3CLF%20N%3D%22lSchoolId%22%20V%3D%220%22%2F%3E%3CLF%20N%3D%22lEduId%22%20V%3D%220%22%2F%3E%3C%2FCDO%3E'
    count1 = len(postdata)
    strc1 = str(count1)
    #登陆需要的headers
    headers = {

            'Host': 'sso.njcedu.com',
            'Content-Length': strc1,
            'Origin': 'http://sso.njcedu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2553.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Accept': '*/*',
            'Referer': 'http://sso.njcedu.com/login.htm',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en,zh;q=0.8,zh-CN;q=0.6,en-US;q=0.4,zh-TW;q=0.2'

        }
    url = 'http://sso.njcedu.com/handleTrans.cdo?strServiceName=UserService&strTransName=SSOLogin'
    request = urllib2.Request(url,postdata,headers)
    response = urllib2.urlopen(request)
    text = response.read()
    text0 = str(text)
    cj0 = str(cj)

    #判断是否登陆
    if 'strName' in text:
        print "login"
    else:
        print "logout"
    #token
    token1 = re.search(r'token=\w+ for',cj0)
    token2 = token1.group()
    token3 = re.sub(r'token=','',token2)
    token4 = re.sub(r' for','',token3)
    #print token4
    luserid1 = re.search(r'luserid=\w+ for',cj0)
    luserid2 = luserid1.group()
    luserid3 = re.sub(r'luserid=','',luserid2)
    luserid4 = re.sub(r' for','',luserid3)
    #print luserid4
    #key
    key_g = re.search(r'key=(.*?)<',text0)
    key = str(key_g.group(1))
    url_key = 'http://yzu.njcedu.com/teacher/Servlet/doLogin.svl?key='+key+'&jsonpCallback=callback&_=1446628151768'
    key_cookie = 'loginname='+username+'; '+'luserid='+luserid4+'; '+'token='+token4+';'


    #正则筛选学号前缀
    id = re.match(r'[a-z]*',username)
    school_id = id.group()
    sch_id = str(school_id)
    host_id =  sch_id + '.njcedu.com'
    #print host_id
    key_headers = {

                    'Host': host_id,
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2553.0 Safari/537.36',
                    'Accept': '*/*',
                    'Referer': 'http://sso.njcedu.com/login.htm?domain=yzu.njcedu.com',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'en,zh;q=0.8,zh-CN;q=0.6,en-US;q=0.4,zh-TW;q=0.2',
                    'Cookie': key_cookie
                    }
    request_key = urllib2.Request(url=url_key,headers=key_headers)
    response_key = urllib2.urlopen(request_key)
    c = response_key.info().getheader('Set-Cookie')
    schooltoken1 = re.search(r'schoolToken=(.*?);',c)
    schooltoken = schooltoken1.group(1)
    #userinfo
    cookie_user = key_cookie + 'schoolToken='+schooltoken
    user_url = 'http://yzu.njcedu.com/student/my/welcome/welcome.htm'
    user_header = {

                    'Host': 'yzu.njcedu.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2553.0 Safari/537.36',
                    'Accept': '*/*',
                    'Referer': 'http://sso.njcedu.com/login.htm?domain=yzu.njcedu.com',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'en,zh;q=0.8,zh-CN;q=0.6,en-US;q=0.4,zh-TW;q=0.2',
                    'Cookie': cookie_user



        }
    req_user = urllib2.Request(url=user_url,headers=user_header)
    res_user = urllib2.urlopen(req_user)
    user_text = str(res_user.read())
    url_id = re.search(r'window.parent.showPlan\((\d+)\)?',user_text)
    list_id = str(url_id.group(1))
    list_url = 'http://'+ host_id + '/student/prese/teachplan/listdetail.htm?id=' + list_id
    req_list = urllib2.Request(url=list_url,headers=user_header)
    res_list = urllib2.urlopen(req_list)
    list_text = str(res_list.read())
    list_unfi = list_text.count('观看')
    list_test = re.findall(r'\d+\.\d%',list_text)
#    count_100 = list_re.count('100.0%')
 #   print list_test
    if list_test.count('100.0%') != len(list_test):
    	print username + '   test_unfinished'
    if list_unfi >= 2:
        print username + '   video_unfinished'
    return
