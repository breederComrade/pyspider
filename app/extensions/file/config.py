# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/11.
  author: wangjun
  description: 
  
"""

# 文件相关配置
UPLOAD_FOLDER = 'app/static/files'
IMG_FOLDER = 'static/images'

FILE = {
    "STORE_DIR": UPLOAD_FOLDER,  # 'app/assets',
    "SINGLE_LIMIT": 1024 * 1024 * 2,
    "TOTAL_LIMIT": 1024 * 1024 * 20,
    "NUMS": 10,
    "INCLUDE": set(['jpg', 'jpeg', 'png'] +
                   ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf', 'md'] +
                   ['mp3', 'mp4'] +
                   ['zip']),
    "EXCLUDE": set([])
}

