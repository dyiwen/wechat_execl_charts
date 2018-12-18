# -*- coding:utf8 -*-
import paramiko
import re
import collections
import sys
import time
import os
from push_xls import file_msg
from execl_tool import generate_excel
from execl_append import append_excel
reload(sys)
sys.setdefaultencoding('utf8')

'''
16002 南大一 16001 山西心研  16000 十堰太和
'''
port_list = [16000,16001,16002]

sql_table_list = ['follow_up',                          #随访信息
				  'home_page',                          #病案首页
				  'inpatient_check',                    #住院检验
				  'inpatient_disease_course_journal',   #住院病程志
				  'inpatient_examination',              #住院检查
				  'inpatient_journal',                  #住院志
				  'inpatient_treatment',                #住院医嘱
				  'nursing_record',                     #护理记录
				  'operation_record',                   #手术数据
				  'outpatient_check',                   #门诊检验
				  'outpatient_disease_course_journal',  #病程志数据
				  'outpatient_examination',             #门诊检查
				  'outpatient_treatment',               #医嘱数据
				  'screening'                           #筛查信息数据
				  ]

dict = {
	'host' : '120.78.136.55',
	'user' : 'root',
	'pwd' : '4rfv%TGB6yhn',
}


#------------------------------------------------------------------------------------------------------------
def re_job(xx,source):
	rex = re.compile(xx)
	result = rex.findall(source)
	return result

def ssh_exec(port,cmd):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(dict['host'],port,dict['user'],dict['pwd'])
		stdin, stdout, stderr = ssh.exec_command("mysql -uroot -pMypassword@2qq -Daf -e '{}'".format(cmd))
		result = stdout.readlines()[1]
		ssh.close()
		return result
	except Exception, e:
		print e

def table_count(port):
	dict = collections.OrderedDict()
	if port == 16000:
		dict['hospital_name'] = u'十堰太和医院'+' '*7
	elif port == 16001:
		dict['hospital_name'] = u'山西心研所'+' '*7
	elif port == 16002:
		dict['hospital_name'] = u'南京大学第一附属医院'+' '*7
	t = time.strftime("%Y-%m-%d %H:%M",time.localtime())
	dict['create_time'] = t

	for table_name in sql_table_list:
		cmd = "select count(*) as a,(select create_time from {} order by create_time desc limit 1) as b from {};".format(table_name,table_name)
		result = ssh_exec(port,cmd = cmd)
		result = re_job(r'(\d+)\s(.*)',result)
		dict[table_name] = result[0][0]+u'条'+'('+result[0][1]+')'
	print dict
	return dict

def insert_info_to_xls():
	total_dict = {}
	for p in port_list:
		info_dict = table_count(p)
		total_dict[p] = info_dict
		# break
	print '-'*100
	print total_dict
	# for key in total_dict.keys():
	# 	print key
	if not os.path.exists(u"C:\\Users\\dyiwen\\Desktop\\dyiwen-tool\\前置机数据统计.xls"):
		print "XXXX.xlsx is not here, creating!~~~~~"
		generate_excel(total_dict)
		print "xlsx生成完毕,发送中"
		file_msg(u"./前置机数据统计.xlsx")

	else:
		print "XXXX.xls has been there"
		append_excel(total_dict)
		print "xls追加完毕,发送中"
		file_msg(u"./前置机数据统计.xls")









if __name__ == '__main__':
	insert_info_to_xls()