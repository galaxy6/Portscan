#!/usr/bin/python2.7
# _*_coding:utf-8_*_

import nmap 
import sys 
import re
import time
import logging
from warn import *
from verify import remote_ssh
from verify import remote_mysql
from multiprocessing import Pool 


def nmScan(host,portrange):
	'''
	检测端口是否开放
	参数host:要检测的主机
	参数partrange:要检测的端口
	'''
	nm = nmap.PortScanner()
	tmp = nm.scan(host,portrange)
	logging.info('ip:%s,port:%s'%(host,portrange))
	port =  tmp.get('nmap').get('scaninfo').get('tcp').get('services')
	port = port.replace('-',',')
	ports = port.split(',')
	for _ in ports:
		if _ == '22':
			port_detail(tmp,_,host,'ssh')
		elif _== '3306':
			port_detail(tmp,_,host,'mysql')
		else:
			logging.info('Port error!')
	return 'sucess'

def port_detail(tmp,port,host,service):
	'''
	验证端口是否能够爆破并发送报警信息
	'''
	if tmp.get('scan'):
		state = tmp.get('scan').get(host).get('tcp').get(int(port)).get('state')
		if (state == 'open'):
			if port =='22':
				if remote_ssh(host):
					info = "We need to close the port! \n\r Information  ip: %s  port: %s  service: %s" % (host,port,service)
					data['msg']= info
					return sendwarn(data)
			elif port =='3306':
				if remote_mysql(host):
					info = "We need to close the port! \n\r Information  ip: %s  port: %s  service: %s" % (host,port,service)
					data['msg']= info
					return sendwarn(data)
			else:
				logging.info('Port error!')
			
	
class nmapscan(object):
	def __init__(self):
		self.portrange = '22,3306'
		self.f = nmScan	

	def _threading(self,hostlist):
		'''
		5个线程进行测试，可根据自己情况更改
		'''	
		result = []
		pool = Pool(processes = 5)
		for ip in hostlist:
			result.append(pool.apply_async(self.f,(ip.strip(),self.portrange)))
		pool.close()
		
		for res in result:
			res.get() 


