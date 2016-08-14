# coding:UTF-8

import urllib2
from bs4 import BeautifulSoup
import json


url="http://www.ishadowsocks.org/"

#response=urllib2.urlopen(url)

#print response.getcode()

request=urllib2.Request(url)

request.add_header("user-agent","Mazilla/5.0")

response=urllib2.urlopen(url)

print response.getcode()

html_doc=response.read().decode("UTF-8")

#html_doc=open('G:\\b.txt','r')

print html_doc

soup = BeautifulSoup(  
           html_doc,              # HTML文档字符串
           "lxml"  
           )
#for tag in soup.find_all('div',class_="col-lg-4 text-center",limit=4):
#	print tag.text

#for tag in soup.find_all('h4',limit=9):
#	print tag.text+" ``"	

ss_config={"strategy" :None,
			"index" : 2,#用第几个服务器
			"global" : False,
			"enabled" : True,
			"shareOverLan" : False,
			"isDefault" : False,
			"localPort" : 1080,
			"pacUrl" : None,
			"useOnlinePac" : False,
			"availabilityStatistics" : False}#一些基本配置


list_config=[]#储存服务器配置列表
str_server={}#储存单个服务器配置
i=0

for tag in soup.find_all('h4',limit=18):#从网页源代码中可以看出前 18个h4标签内有相应的服务器信息
	if i%6==0:
		str1=tag.text.split(':')[1]
		#print str1
		str_server['server']=str1
		
	if i%6==1:
		str1=tag.text.split(':')[1]
		#print str1
		str_server['server_port']=str1
		
	if i%6==2:
		str1=tag.text.split(':')[1]
		#print str1
		str_server['password']=str1
	if i%6==3:
		str1=tag.text.split(':')[1]
		#print str1
		str_server['method']=str1
		str_server['remark']=""
		#print str_server
		list_config.append(str_server)
		#print list_config
		str_server={}
	i=i+1

print "Success"

ss_config["configs"]=list_config#生成最后的json数据

#print ss_config
file ='C:\\Users\\Yu\\Desktop\\Shadowsocks-2.5.8\\gui-config.json'#ss路径
fp=open(file,'w')
#fp.write(json.loads(str))
json.dump(ss_config,fp)

fp.close()

print "Success"