#!/usr/bin/python2.7
#_*_coding:utf-8_*_

##发送告警信息的接口，可以根据自己的使用情况更改

data = {
    # ip地址
    #'ip':'127.0.0.1',
    # 端口(非端口告警则留空)
    # 'port':'8080',
    # 告警级别
    #'rank':'',
    # 告警类型
    #'type':'',
    #告警等级(CRITICAL,WARN,INFO)
    'level':'WARN',
    #告警信息标题(用作邮件标题)
    'title':'[WARN] Illegal port open',
    #告警内容
    'msg':'ip port service',
    #告警值
    #接收告警名单(支持微信、邮件，需按照以下格式填写，","分割消息类型，“|”分割接收者,)
    # to="weixin:xxx|xxx,mail:xxx@xxx.com.|xxx@xxx.com"
    'to':"mail:xxx@xxx.com"

}

def sendwarn(data):
    import urllib,urllib2,json,time
    for i in data:
        data[i] = urllib.quote(data[i])
    data['ins_time'] = time.strftime("%Y-%m-%d_%H:%M:%S")
    url='http://*.*.*.*/sendmsg'   #发送邮件或者微信的http请求接口，可根据自己情况实现更改
    json_data = json.dumps(data)
    req = urllib2.Request(url, json_data)
    response = urllib2.urlopen(req)
    return response.read()

