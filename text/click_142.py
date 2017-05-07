# -*- coding: utf-8 -*-
import requests
import hashlib
from lxml import etree
import re
#login
username = raw_input("username: ")
password = raw_input("psaaword: ")
time_record = raw_input("time_record: ")

#用于md5加密的密码转换
m = hashlib.md5()
m.update(password)
login_id = m.hexdigest()
postdata ='$$CDORequest$$=%3CCDO%3E%3CSTRF%20N%3D%22strServiceName%22%20V%3D%22UserService%22%2F%3E%3CSTRF%20N%3D%22strLoginId%22%20V%3D%22'+ username +'%22%2F%3E%3CSTRF%20N%3D%22strTransName%22%20V%3D%22SSOLogin%22%2F%3E%3CSTRF%20N%3D%22strPassword%22%20V%3D%22'+login_id+'%22%2F%3E%3CSTRF%20N%3D%22strVerifyCode%22%20V%3D%22%22%2F%3E%3CSTRF%20N%3D%22bIsCookieLogin%22%20V%3D%22change%22%2F%3E%3CSTRF%20N%3D%22Sessioncheck%22%20V%3D%22sessionErr%22%2F%3E%3CLF%20N%3D%22lSchoolId%22%20V%3D%220%22%2F%3E%3CLF%20N%3D%22lEduId%22%20V%3D%220%22%2F%3E%3C%2FCDO%3E'
count1 = len(postdata)
strc1 = str(count1)
#登陆需要的headers
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
login_info = req.text
if 'key' in login_info:
    print 'login succesful'
else:
    print 'login failed'
        
#print login_info
luserid = re.search(r'N="lId" V="(\w+)"',login_info)
luserid = luserid.group(1)
#scholltoken
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
req_sch = s.get(url=url_sch,headers=headers_sch)
schoolToken = req_sch.cookies['schoolToken']



#time add
def addtime(luserid):
	url_time = "http://yzu.njcedu.com/student/prese/examin/handleTrans.cdo?strServiceName=StudentExminService&strTransName=modifyStudentExaminUsedTime"
	time_data = "$$CDORequest$$=%3CCDO%3E%3CSTRF%20N%3D%22%24strDestNodeName%24%22%20V%3D%22TeachingBusiness%22%2F%3E%3CSTRF%20N%3D%22strServiceName%22%20V%3D%22StudentExminService%22%2F%3E%3CSTRF%20N%3D%22strTransName%22%20V%3D%22modifyStudentExaminUsedTime%22%2F%3E%3CLF%20N%3D%22lSchoolId%22%20V%3D%22204%22%2F%3E%3CLF%20N%3D%22lUserId%22%20V%3D%22" + luserid + "%22%2F%3E%3CLF%20N%3D%22lExaminId%22%20V%3D%2210200000048%22%2F%3E%3CLF%20N%3D%22lPlanId%22%20V%3D%2210200000026%22%2F%3E%3CLF%20N%3D%22nExaminType%22%20V%3D%220%22%2F%3E%3CNF%20N%3D%22nUsedTime%22%20V%3D%221%22%2F%3E%3C%2FCDO%3E"
	count_t = len(time_data)
	str_time = str(count_t)

	headers_time = {
	    "Host": "yzu.njcedu.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate",
	"Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
	"Referer": "http://yzu.njcedu.com/student/prese/examin/pager.htm?lId=10200000048&nExaminType=0",
	"Content-Length": str_time
	    
	    
	}
	s.post(url=url_time,headers=headers_time,data=time_data)
	return

i = 1
while (i < int(time_record)):
	addtime(luserid)
	
	i = i + 1
	print "+" + str(i)

#test_0
test_data = "$$CDORequest$$=%3CCDO%3E%3CSTRF%20N%3D%22%24strDestNodeName%24%22%20V%3D%22TeachingBusiness%22%2F%3E%3CSTRF%20N%3D%22strServiceName%22%20V%3D%22StudentExminService%22%2F%3E%3CSTRF%20N%3D%22strTransName%22%20V%3D%22markStudentExamin%22%2F%3E%3CLF%20N%3D%22lSchoolId%22%20V%3D%22204%22%2F%3E%3CLF%20N%3D%22lUserId%22%20V%3D%22" +luserid+ "%22%2F%3E%3CLF%20N%3D%22lExaminId%22%20V%3D%2210200000048%22%2F%3E%3CLF%20N%3D%22lPlanId%22%20V%3D%2210200000026%22%2F%3E%3CLF%20N%3D%22nExaminType%22%20V%3D%220%22%2F%3E%3CSTRF%20N%3D%22strAnswer0%22%20V%3D%220%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%22%2F%3E%3CSTRF%20N%3D%22strAnswer1%22%20V%3D%22%22%2F%3E%3CNF%20N%3D%22nCommitType%22%20V%3D%221%22%2F%3E%3CNF%20N%3D%22nExaminState%22%20V%3D%222%22%2F%3E%3CSTRF%20N%3D%22strToken%22%20V%3D%22%22%2F%3E%3C%2FCDO%3E"

count2 = len(test_data)
strc2 = str(count2)
headers_test = {
	"Host": "yzu.njcedu.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
"Referer": "http://yzu.njcedu.com/student/prese/examin/pager.htm?lId=10200000048&nExaminType=0",
"Content-Length": strc2,
#"Cookie": JSESSIONID=FF0A31EF9B147408855BAC9F42C33C9E; pgv_pvi=8683465728; pgv_si=s5805861888; loginname=yzu_132003104; luserid=37700006733; token=f66919b9d3836d1c28ab33040a8c89aa88748a666eb05efb9e67a086921d5f3a720dafb54248a124e1f61a32c1a9cd1c4a73a93bf21d6c6402d3ce65259e0619; lasttime=1451278851664; schoolToken=f66919b9d3836d1cef45d43ab5b6db43bbf254a8c109c38c353a3a972755ef298a755fc6ca498d2ca2b0bdf74d5abcc9401fdf778e807d25bf01b9564ecc5218a2b0bdf74d5abcc99e9ee78ee8a03568e4d16fc8bed14989935c74558e45acedc1e3ed195c6adb538e7cbf71b8922587ee0c3f17f6ee08cc7a80d9e69180b83c7b36e6762ac573cf; IESESSION=alive; msglasttime37700006733=1451279600746; newmsgcount37700006733=24
#"Connection": keep-alive
"Pragma": "no-cache",
"Cache-Control": "no-cache"

}
url_test = "http://yzu.njcedu.com/student/prese/examin/handleTrans.cdo?strServiceName=StudentExminService&strTransName=markStudentExamin"
test_req = s.post(url=url_test,headers=headers_test,data=test_data)
print 'your score is oing...'







#result 
url_res = "http://yzu.njcedu.com/student/prese/examin/result.htm?nExaminType=0&lId=10200000048"
headers_res = {
	
"Host": "yzu.njcedu.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Referer": "http://yzu.njcedu.com/student/prese/teachplan/listdetail.htm?id=10200000026"


}

result_info = s.get(url=url_res,headers=headers_res)
info = result_info.text
#print info
info = str(info.encode('utf-8'))
page = etree.HTML(info.lower().decode('utf-8'))
list_1 = page.xpath('''//span[@style="color: red;padding-left: 10px"]/text()''')
strli = '%2C'.join(list_1)
strli = strli.upper()
#test_right
data_1 = "$$CDORequest$$=%3CCDO%3E%3CSTRF%20N%3D%22%24strDestNodeName%24%22%20V%3D%22TeachingBusiness%22%2F%3E%3CSTRF%20N%3D%22strServiceName%22%20V%3D%22StudentExminService%22%2F%3E%3CSTRF%20N%3D%22strTransName%22%20V%3D%22markStudentExamin%22%2F%3E%3CLF%20N%3D%22lSchoolId%22%20V%3D%22204%22%2F%3E%3CLF%20N%3D%22lUserId%22%20V%3D%22" +luserid+ "%22%2F%3E%3CLF%20N%3D%22lExaminId%22%20V%3D%2210200000048%22%2F%3E%3CLF%20N%3D%22lPlanId%22%20V%3D%2210200000026%22%2F%3E%3CLF%20N%3D%22nExaminType%22%20V%3D%220%22%2F%3E%3CSTRF%20N%3D%22strAnswer0%22%20V%3D%22"+strli+"%22%2F%3E%3CSTRF%20N%3D%22strAnswer1%22%20V%3D%22%22%2F%3E%3CNF%20N%3D%22nCommitType%22%20V%3D%221%22%2F%3E%3CNF%20N%3D%22nExaminState%22%20V%3D%222%22%2F%3E%3CSTRF%20N%3D%22strToken%22%20V%3D%22%22%2F%3E%3C%2FCDO%3E"
#print data_1
test_req = s.post(url=url_test,headers=headers_test,data=data_1)
print 'hahaha,kading you!'
