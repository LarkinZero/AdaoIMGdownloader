# coding=utf-8
# Install the Python Requests library:
# `pip install requests`

import requests
import json
import os
import sys

def send_request(host,threadid,page):
    # My API (11) (GET http://h.acfun.tv/api/t/117617)

    try:
        r = requests.get(
            url=host+str(threadid),
            # url="http://h.koukuko.com/api/t/"+str(threadid),

            params = {
                "page":str(page),
            },
        )
        # print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
        # print('Response HTTP Response Body : {content}'.format(content=r.content))
        return r.content
    except requests.exceptions.RequestException as e:
        print('HTTP Request failed')

def get_img(host,threadsid,path):

    path = path+str(threadsid)
    os.system('mkdir '+path+'/')

    value = send_request(host,threadsid,1)
    o = json.loads(value)
    imgurl = imghost+str(o['threads']['image'])
    # print o['replys'][1]['image']
    totalreplay = int(o['threads']['replyCount'])
    totalpage = int(o['page']['size'])
    os.system('wget -nc -P '+path+' '+imgurl)
    # print totalpage
    for page in range(1,totalpage+1):
        print "正在处理第"+str(page)+"页"
        tempvalue = send_request(host,threadsid,page)
        o = json.loads(tempvalue)
        replyrange = len(o['replys'])
        # print o['replys'][1]['image']
        for replys in range(1,replyrange):
            replysimg = str(o['replys'][replys]['image'])
            if replysimg != "":
                imgurl = imghost+replysimg
                # print imgurl
                os.system('wget -nc -P '+path+' '+imgurl)


path = "/Volumes/Transcend/Temp/Adao/"

#print len(sys.argv)
if len(sys.argv)==1:
    print "运行参数：[串ID] [0或1；0为匿名岛，1为备胎岛]"
else:
    threadsid = sys.argv[1]
    print threadsid
    hostid = sys.argv[2]
    print hostid
    if hostid == "1":
        host = "http://h.koukuko.com/api/t/"
        imghost = "http://static.koukuko.com/h/"
        get_img(host,threadsid,path)
    elif hostid == "0":
        host = "http://h.nimingban.com/api/t/"
        imghost = "http://cdn.ovear.info:8999/"
        get_img(host,threadsid,path)
    else:
        print "运行参数：[串ID] [0或1；0为匿名岛，1为备胎岛]"

