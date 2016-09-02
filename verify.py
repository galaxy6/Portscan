#!/usr/bin/python2.7
#_*_coding:utf-8_*_

import paramiko
import commands


def remote_ssh(host):
	"""
	确认ssh服务可以远程爆破
	"""
	try:
		client = paramiko.SSHClient() 
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
		sucess = client.connect(host, 22, username='root', password='49d6a25d112avcsss', timeout=10)  #用户和密码是错误的就行
	except Exception,e:
		result = '%s' % e
		if result.find('EntryPoint') != -1:
			return host

def remote_mysql(host):
	"""
	确认mysql服务可以远程爆破
	"""
	output = commands.getstatusoutput('/usr/bin/mysql -h %s -uroot -p49d6a25d112exss --connect-timeout=5'%host) #运行mysql的路径自己设置，确保密码用户错误的
	if output[1].find('ERROR 1045') != -1:
		return host

