# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/11.
  author: wangjun
  description: 
  
"""

from werkzeug.utils import secure_filename

# from app.models.file import File
# from app.dao.file import FileDao
from app.core.file import Uploader

__author__ = 'Allen7D'


class LocalUploader(Uploader):
    pass
    # def locate(self, parent_id=0):
    #     self.parent_id = parent_id
    #
    # def upload(self):
    #     ret = []
    #     self.mkdir_if_not_exists()
    #     for single in self._file_storage:
    #         file_md5 = self._generate_md5(single.read())
    #         single.seek(0)
    #         file = File.query.filter_by(md5=file_md5).first()
    #         if file and self.parent_id != file.parent_id:
    #             if not File.query.filter_by(parent_id=self.parent_id, md5=file_md5).first():
    #                 file = FileDao.copy_file(
    #                     dest_parent_id=self.parent_id,
    #                     src_file_id=file.id
    #                 )
    #
    #         if not file:
    #             absolute_path, relative_path, uuid_filename = self._get_store_path(single.filename)
    #             secure_filename(single.filename)
    #             single.save(absolute_path)
    #             File.create(
    #                 parent_id=self.parent_id,
    #                 name=single.filename,
    #                 uuid_name=uuid_filename,
    #                 path=relative_path,
    #                 extension=self._get_ext(single.filename),
    #                 size=self._get_size(single),
    #                 md5=file_md5
    #             )
    #             file = File.get(parent_id=self.parent_id, md5=file_md5)
    #         ret.append(file)
    #     return ret

