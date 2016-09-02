#!/usr/bin/python2.7
#_*_coding:utf-8_*_

import time
import requests
import logging
from portscan import nmapscan

def logger():
	logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='./log/scan.log')	

def task():
	url = 'http://www.xxx.com/getIps' #提供的ip端接口，ip端形式192.168.1.1-200这样的表示形式，如果有多个段换行即可
	resp = requests.get(url)
	content = resp.content if resp.content else resp.text
	for ips in content.split('\n'):
		hostlist = []
		if ips:
			suffix_ip = ips[ips.rfind('.')+1:]
			prefix_ip = ips[:ips.rfind('.')+1] 
			suffix_ip = suffix_ip.split('-')
			count_1 = int(suffix_ip[0]) if suffix_ip[0] else 0
			count_2 = int(suffix_ip[1])+1 if suffix_ip[1] else 0
			for ip_ in range(count_1,count_2):
				ip = "%s%s"%(prefix_ip,ip_)
				hostlist.append(ip)
			nmapscan()._threading(hostlist)

def main():
	logger()
	while True:
		current_time = time.localtime()
		curhour = current_time.tm_hour
		curmin = current_time.tm_min
		if curhour < 10:
			deltahour = 10 - curhour
		else:
			deltahour = 24 - curhour + 10
		sleep_time = deltahour*3600 -curmin*60
        
		diff_time = 30*60
		task()
		time.sleep(sleep_time)


if __name__ == '__main__':
   main()

