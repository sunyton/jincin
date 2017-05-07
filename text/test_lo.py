# -*- coding: utf-8 -*-
import requests
import hashlib
from lxml import etree
import re
#login
username = raw_input("username: ")
password = raw_input("psaaword: ")


m = hashlib.md5()
m.update(password)
login_id = m.hexdigest()
postdata ='$$CDORequest$$=%3CCDO%3E%3CSTRF%20N%3D%22strServiceName%22%20V%3D%22UserService%22%2F%3E%3CSTRF%20N%3D%22strLoginId%22%20V%3D%22'+ username +'%22%2F%3E%3CSTRF%20N%3D%22strTransName%22%20V%3D%22SSOLogin%22%2F%3E%3CSTRF%20N%3D%22strPassword%22%20V%3D%22'+login_id+'%22%2F%3E%3CSTRF%20N%3D%22strVerifyCode%22%20V%3D%22%22%2F%3E%3CSTRF%20N%3D%22bIsCookieLogin%22%20V%3D%22change%22%2F%3E%3CSTRF%20N%3D%22Sessioncheck%22%20V%3D%22sessionErr%22%2F%3E%3CLF%20N%3D%22lSchoolId%22%20V%3D%220%22%2F%3E%3CLF%20N%3D%22lEduId%22%20V%3D%220%22%2F%3E%3C%2FCDO%3E'
count1 = len(postdata)
strc1 = str(count1)

headers = {

        'Host': 'sso.njcedu.com',
        'Content-Length': strc1,
        'Origin': 'http://sso.njcedu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Accept': '*/*',
        'Referer': 'http://sso.njcedu.com/login.htm',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,zh;q=0.8,zh-CN;q=0.6,en-US;q=0.4,zh-TW;q=0.2',
        'strServiceName': 'UserService'


    }
url = 'http://sso.njcedu.com/handleTrans.cdo?strServiceName=UserService&strTransName=SSOLogin'

s = requests.Session()

req = s.post(url=url,headers=headers,data=postdata)
#token = req.headers
#token
#token1 = str(token)
#token2 = re.search(r'token=(\w+);',token1)
#token3 = token2.group(1)
#print token3
login_info = req.text
print login_info
key1 = re.search(r'key=(.*)</STR>',login_info)
key = key1.group(1)
url_sch = "http://yzu.njcedu.com/teacher/Servlet/doLogin.svl?key="+key+"&jsonpCallback=callback&_=1451292636427"
headers_sch = {
    "Host": "yzu.njcedu.com",
"Accept": "*/*",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36",
"Referer": "http://sso.njcedu.com/login.htm",
"Accept-Encoding": "gzip, deflate, sdch",
"Accept-Language": "en,zh;q=0.8,zh-CN;q=0.6,en-US;q=0.4,zh-TW;q=0.2"

}
#cookies = {"token": "token="+token3}
req_sch = s.get(url=url_sch,headers=headers_sch)
schoolToken = req_sch.cookies['schoolToken']
print schoolToken
