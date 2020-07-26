# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/7/26
  author: wangjun
  description: 上传图片
  
"""
from flask import request, jsonify

from app.core.error import Success
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import express as api_doc
from app.service.qiniu import QiNiu

api = Redprint(name='file', description='文件', api_doc=api_doc)


@api.route('/upload_img', methods=["POST"])
@api.doc()
def upload_img():
    '''上传图片'''
    try:
        data = request.files.get('file').read()
        print(data)
    except Exception as e:
        print('3',e)
        return jsonify(errmsg='数据错误')
    
    try:
        filename = QiNiu.uploadFile(data)
    except Exception as e:
        print('e',e)
        return jsonify(errmsg='上传失败', errcode=500)
    return Success()