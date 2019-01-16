#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import sys
import requests
import time


Toparty = ""
AgentID = 
CropID = ""
Secret = ""
Gtoken = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + CropID + "&corpsecret=" + Secret
headers = {'Content-Type':'application/json'}
json_data = json.loads(requests.get(Gtoken).content.decode())
# print json_data
token = json_data['access_token']
Purl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(token)

def msg(title , message):
	image_url = 'https://www.pgyer.com/app/qrcode/yisW'
	weixin_msg = {
		"toparty" : Toparty,
		"msgtype" : "news",
		"agentid" : AgentID,
		"textcard" : {
			"title" : title,
			"description" : message,
			"picurl" : image_url,
			"url" : "www.pgyer.com/Y5mc",
			"btntxt" : "点击跳转下载页面"
		}
	}
	print requests.post(Purl, json.dumps(weixin_msg), headers=headers)

#https://www.pgyer.com/app/qrcode/yisW

def get_media_ID():
	img_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={}&type=image".format(token)
	files = {'image' : 'https://www.pgyer.com/app/qrcode/yisW'}
	r = requests.post(img_url , files=files)
	re = json.loads(r.text)
	print re['media_id']

def image_msg(title , message):
	image_url = 'https://www.pgyer.com/app/qrcode/yisW'
	image_url_2 = "http://tz.img.dns4.cn/pic/192713/p18/20171214154800_8834_zs_sy.jpeg"
	weixin_msg = {
		"toparty" : Toparty,
		"msgtype" : "news",
		"agentid" : AgentID,
		"news" : {
			"articles" : [{
				"title" : title,
				"description" : message,
				"url" : "www.pgyer.com/Y5mc",
				"picurl" : image_url_2
			},{
			"title" : title,
			"description" : message,
			"url" : "www.pgyer.com/Y5mc",
			"picurl" : image_url
			}]
		}
	}
	print requests.post(Purl, json.dumps(weixin_msg), headers=headers)


def get_file_id(file):
	file_path = {"file" : file}
	post_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={}&type=file".format(token)
	r = requests.post(post_url , files=file_path)
	re = json.loads(r.text)
	# print re
	# print re['media_id']
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

	print requests.post(Purl, json.dumps(weixin_msg), headers=headers)


if __name__ == '__main__':
	# title = sys.argv[1]
	# message = sys.argv[2]
	# image_msg("Test", "test")
	# get_media_ID()
	# print token
	# file_msg()
	get_file_id()
