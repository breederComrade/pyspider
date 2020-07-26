# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/7/26
  author: wangjun
  description: 七牛上传和下载文件
  
"""
import time

from qiniu import Auth, put_data, etag
from flask import current_app

from app.core.error import FileUploadFailException


class QiNiu(object):
    
    # 上传文件
    @staticmethod
    def uploadFile(inputdata):
        '''
        
        :param inputdata: bytes类型数据
        :return: 文件上传后名字
        '''
        sk = current_app.config['QINIU_SK']
        ak = current_app.config['QINIU_AK']
        # 鉴权
        auth = Auth(ak, sk)
        '''上传文件'''
        # 上传空间
        bucket_name = 'goods'
        # 生成token
        # 上传文件到七牛后， 七牛将文件名和文件大小回调给业务服务器。
     
        # 如果需要对上传的图片命名，就把第二个参数改为需要的名字
        key = 'screen03.png'
        
        token = auth.upload_token(bucket_name, key, 3600, )
        
        ret1, ret2 = put_data(token, key, data=inputdata)
        print('ret1:', ret1)
        print('ret2:', ret2)
        if ret2.status_code != 200:
            raise FileUploadFailException()
        return ret1.get('key')
    
    # 下载文件
    @staticmethod
    def downloadFile():
        '''下载文件'''
        pass
