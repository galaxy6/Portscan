#Portscan

##portscan
这个脚本的主要作用是每天对线上服务器的22和3306端口做监控，如果有端口开放且可以进行爆破则会发送到邮箱进行告警。


##Introduce

1.环境python2.7，直接运行在服务器上。

2.扫描到的非法端口直接发送要邮箱进行告警。

3.日志存放在log目录下，程序运行实时状态可用通过日志查看。

4.protect是保护进程，port进程停止后protect会杀死这个进程并重启新的进程。

Usage

Usage: 

    python port.py    	
    python protect.py
