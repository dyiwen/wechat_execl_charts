# -*- coding: utf-8 -*-

import json
import os
import sys
import requests
import time
import urllib


Toparty = "8"
AgentID = 1000023
CropID = "ww81574f0e4b5b1fd8"
Secret = "np98KiE_lqm1drjP2PZP_AvfdaG_i8zUpI46HGwFAKM"   
Gtoken = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + CropID + "&corpsecret=" + Secret
headers = {'Content-Type':'application/json'}
json_data = json.loads(requests.get(Gtoken).content.decode())
token = json_data['access_token']
Purl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(token)

def get_file_id(file):
	file_data = open(file,'rb')
	print file_data
	file_path = {"file" : file_data}
	data = {'enctype':'multipart/form-data','name':'duanyiwen'}
	post_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={}&type=file".format(token)
	r = requests.post(post_url , data = data, files=file_path)
	re = json.loads(r.text)
	print re
	print re['media_id']
	return re['media_id']

def file_msg(file):
	media_id = get_file_id(file)

	weixin_msg = {
		"toparty" : Toparty,
		"agentid" : AgentID,
		"msgtype" : "file",
		"file" : {
			"media_id" : media_id
		}
	}
	print media_id
	print requests.post(Purl, json.dumps(weixin_msg), headers=headers)


if __name__ == '__main__':
	# get_file_id(u"./前置机数据统计.xlsx")
	file_msg(u"./前置机数据统计.xlsx")
	# 3l0GdBGASSUBtOxRn8-nxWE5DTfZmUyWtvKrg_btbuMWuvHNTYTgcYK2GP07DbJo3
	# 3blKgPbkMuU2IFt-OuF0BUDlDW7J0R2ObyzCKVzqzBOk
	# get_file_id()
