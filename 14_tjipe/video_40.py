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
def hack_video(username):
    password = '123456'
    #用于md5加密的密码转换
    m = hashlib.md5()
    m.update(password)
    login_id = m.hexdigest()
    #cookie处理
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    #本地调试
    #proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8080'})
    postdata ='$$CDORequest$$=%3CCDO%3E%3CSTRF%20N%3D%22strServiceName%22%20V%3D%22UserService%22%2F%3E%3CSTRF%20N%3D%22strLoginId%22%20V%3D%22'+ username +'%22%2F%3E%3CSTRF%20N%3D%22strTransName%22%20V%3D%22SSOLogin%22%2F%3E%3CSTRF%20N%3D%22strPassword%22%20V%3D%22'+login_id+'%22%2F%3E%3CSTRF%20N%3D%22strVerifyCode%22%20V%3D%22%22%2F%3E%3CSTRF%20N%3D%22bIsCookieLogin%22%20V%3D%22change%22%2F%3E%3CSTRF%20N%3D%22Sessioncheck%22%20V%3D%22sessionErr%22%2F%3E%3CLF%20N%3D%22lSchoolId%22%20V%3D%220%22%2F%3E%3CLF%20N%3D%22lEduId%22%20V%3D%220%22%2F%3E%3C%2FCDO%3E'
    count1 = len(postdata)
    strc1 = str(count1)
    #登陆需要的headers
    headers = {

            'Host': 'sso.njcedu.com',
            'Content-Length': strc1,
            'Origin': 'http://sso.njcedu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2540.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Accept': '*/*',
            'Referer': 'http://sso.njcedu.com/login.htm',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en,zh;q=0.8,zh-CN;q=0.6,en-US;q=0.4,zh-TW;q=0.2',
            'strServiceName': 'UserService'


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
        
    #re正则筛选出 token,luserid,key
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
    #post_get函数封装,获得courseware
    #def post_get(list_id):
    course_url = 'http://course.njcedu.com/course.svl?lId=1303&time=1445440862714'
    Course_cookie = 'loginname='+username+'; '+'luserid='+luserid4+'; '+'token='+token4
    course_headers = {

                    'Host': 'course.njcedu.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2541.0 Safari/537.36',
                    'X-Requested-With': 'ShockwaveFlash/19.0.0.226',
                    'Accept': '*/*',
                    'Referer': 'http://course1.njcedu.com/course.htm?courseId=50&userId=37700006733&schoolId=204&lPanId=0',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'en,zh;q=0.8,zh-CN;q=0.6,en-US;q=0.4,zh-TW;q=0.2',
                    'Cookie': Course_cookie
                    }
    request = urllib2.Request(url=course_url,headers=course_headers)
    response = urllib2.urlopen(request)
    text = response.headers
    course_cookie = str(text)
    course_cookie1 = re.search(r'Courseware.* D',course_cookie)
    course_cookie2 = course_cookie1.group()
    courseware = re.sub(r' D','',course_cookie2)
    #return courseware
    out_ware = courseware
    out_ware1 = re.sub(r'Courseware_\d+=','',out_ware)
    #print out_ware1
    #等待响应
    time.sleep(35)


    #post刷时函数定义，方便调用
    #url_func = 'http://course1.njcedu.com/Servlet/recordStudy.svl'
    def hack_video(list_id):
        url_func = 'http://course1.njcedu.com/Servlet/recordStudy.svl'
        data_func = 'lUserId='+luserid4+'&strStartTime=0&lCourseId='+list_id+'&lSchoolId=204'
        count = len(data_func)
        strc = str(count)
        headers_func = {

                'Host': 'course1.njcedu.com',
                'Content-Length': strc,
                'Origin': 'http://flash.njcedu.com',
                'X-Requested-With': 'ShockwaveFlash/19.0.0.228',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2542.0 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'Referer': 'http://flash.njcedu.com/P2PPlayer/P2PPlayer.swf?v=5',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en,zh;q=0.8,zh-CN;q=0.6,en-US;q=0.4,zh-TW;q=0.2',
                'Cookie': 'loginname='+username+'; luserid='+ luserid4 + '; token='+token4+';'+ 'Courseware_'+luserid4 + list_id +'='+out_ware1


        }
    #tianjin 473 benxiao 204
        data_func = 'lUserId='+luserid4+'&strStartTime=0&lCourseId='+list_id+'&lSchoolId=473'
        #print data_func
        #print headers_func
        #print url_func
        r = requests.post(url=url_func,data=data_func,headers=headers_func)
        code = r.status_code
        print code
        
        i = 1
        while code == 200:
            r = requests.post(url=url_func,data=data_func,headers=headers_func)
            i = i+1
            if i > 40:
                print list_id+'  finished\r'
                break
        return

    hack_video('1303')
    hack_video('1304')
    hack_video('1305') 
    hack_video('1329')
    hack_video('1330')
    hack_video('1331')
    hack_video('1322')
    hack_video('1323')
    hack_video('1285')
    hack_video('1286')
    hack_video('1287')
    hack_video('1289')
    hack_video('1324')
    hack_video('1292')
    hack_video('1294')



    print 'All Finished,登陆查看，如果还有未完成的请重新运行'
    return




    
    
    
