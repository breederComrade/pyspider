# _*_ coding: utf-8 _*_
"""
  project:有单生意
  date: 2020/06/10.
  author: wangjun
  description: 
  
"""
from app.core.swagger_filed import IntegerQueryFiled, IntegerPathFiled, \
    StringPathFiled, StringQueryFiled, ArrayQueryField, \
    BodyField

# test
test_in_body = BodyField(name='test', type='string', description='test', enum=['t', 'v'])

# 通用
id_in_body = BodyField(name='id', type='integer', description='id')
id_in_query = IntegerQueryFiled(name='id',description='id')
name_in_body = BodyField(name='id', type='string', description='名称')

# Token登录相关
token_in_body = BodyField(name='token', type='string', description='Token', enum=[
    'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NjM2ODEzMCwiZXhwIjoxNTg4OTYwMTMwfQ.eyJ1aWQiOjEsInR5cGUiOjEwMCwic2NvcGUiOiLns7vnu5_nrqHnkIblkZgifQ.ovFuc5Ti5zGm5B7JS7AGOBBmrYHGCRsVk9OFAWb88LhY7v9Ubw4c_3xGik7K8Emd6_fz4Ho6Hk3GI1_fjcSIww'])
account_in_body = BodyField(name='account', type='string', description='用户名(此处可以传邮箱，或者微信登录的code)', enum=["666@qq.com"])
secret_in_body = BodyField(name='secret', type='string', description='密码', enum=["123456"])
type_in_body = BodyField(name='type', type='integer', description='登录方式', enum=[101, 100])

# 分页相关
page = IntegerQueryFiled(name='page', description="第几页", enum=[1, 2, 3, 4, 5], default=1)
size = IntegerQueryFiled(name='size', description="每页大小", enum=[10, 20, 30, 40, 50, 100], default=10)

# 时间区间
start = IntegerQueryFiled(name='start', description="开始时间(时间戳)",
                          enum=[1588130000, 1588131000, 1588132000, 1588133000, 1588134000, ])
end = IntegerQueryFiled(name='end', description="结束时间(时间戳)",
                        enum=[1588135000, 1588136000, 1588137000, 1588138000, 1588139000, ])

uid_in_path = IntegerPathFiled(
    name='uid', description="用户ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1, required=True)
uid_in_query = IntegerQueryFiled(
    name='uid', description="用户ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1, required=True)
uid_in_body = BodyField(
    name='uid_id', type='integer', description="用户ID", enum=[1, 2, 3, 4, 5, 10, 15, 20])

product_id_in_path = IntegerPathFiled(
    name='id', description="商品ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
product_id_in_query = IntegerQueryFiled(
    name='product_id', description="商品ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
product_id_in_body = BodyField(
    name='product_id', type='integer', description="商品ID", enum=[1, 2, 3, 4, 5, 10, 15, 20])

# 重新排序
src_order_in_body = BodyField(
    name='src_order', type='integer', description="原顺序", enum=[1, 2, 3, 4, 5, 10, 15, 20])
dest_order_in_body = BodyField(
    name='dest_order', type='integer', description="新顺序", enum=[1, 2, 3, 4, 5, 10, 15, 20])

category_id_in_path = IntegerPathFiled(
    name='id', description="类别 ID", required=True)
category_id_in_query = IntegerQueryFiled(
    name='category_id', description="类别 ID", required=True)

order_id_in_path = IntegerPathFiled(
    name='id', description="订单ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
order_id_in_query = IntegerQueryFiled(
    name='order_id', description="订单ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)

order_no_in_query = StringQueryFiled(
    name='order_no', description='订单号', enum=['B0X439892335427188', 'B0X433513735427169'])

# 权限组
group_id_in_path = IntegerPathFiled(
    name='id', description="权限组ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
group_id_in_query = IntegerQueryFiled(
    name='group_id', description="权限组ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
group_id_in_body = BodyField(
    name='group_id', type='integer', description="权限组ID", enum=[1, 2, 3, 4, 5, 10, 15, 20])
src_id_in_body = BodyField(
    name='src_id', type='integer', description="源权限组ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100])
dest_id_in_body = BodyField(
    name='dest_id', type='integer', description="目标权限组ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100])

# 权限
auth_ids_in_body = BodyField(name='auth_ids', type='array', description='权限ID列表',   enum=[[6, 7, 8], [12, 13, 14]])

# Password
password_in_body = BodyField(name='password', type='string', description='密码', )
old_password_in_body = BodyField(name='old_password', type='string', description='密码', )
new_password_in_body = BodyField(name='new_password', type='string', description='密码', )
confirm_password_in_body = BodyField(name='confirm_password', type='string', description='密码', )

# User
nickname_in_body = BodyField(name='nickname', type='string', description='昵称', )
username_in_body = BodyField(name='username', type='string', description='用户名', )
email_in_body = BodyField(name='email', type='string', description='邮箱',)
mobile_in_body = BodyField(name='mobile', type='string', description='手机', )
avatar_in_body = BodyField(name='avatar', type='string', description='头像url', )
userId_in_query = StringQueryFiled(name='userId', description='用户id', default='1', required=True)

# Address
address_id_in_path = IntegerPathFiled(
    name='id', description="地址ID", required=True)

address_id_in_query = IntegerPathFiled(
    name='id', description="地址ID", required=True)

# customer
customer_id_in_query= IntegerQueryFiled(
    name='id', description='客户id', required=True
)
customer_id_in_body= BodyField(
    name='id',type='integer',description='客户id'
)

customer_name_in_body=BodyField(
    name='nickname',type='string',description='客户名称',
)

customer_avatar_in_body=BodyField(
    name='avatar',type='string',description='头像'
)

customer_mobile_in_body=BodyField(
    name='mobile',type='string',description='手机号'
)

wechat_in_body=BodyField(
    name='wechat',type='string',description='微信号'
)
customer_company_id_in_body = BodyField(
    name='company_id',type='integer',description='企业id'
)





# File
file_id_in_path = IntegerPathFiled(
    name='id', description="文件ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1)
file_id_in_query = IntegerQueryFiled(
    name='file_id', description="文件ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1)
file_ids_in_query = ArrayQueryField(
    name='ids', description='文件ID集(多选)',
    item_type='integer', enum=[1, 2, 3, 4, 5, 10, 100],
    default=1, required=True)

parent_id_in_path = IntegerPathFiled(
    name='id', description="父级目录ID", enum=[0, 1, 2, 3, 4, 5, 10, 100], default=1)
parent_id_in_query = IntegerQueryFiled(
    name='parent_id', description="父级目录ID", enum=[0, 1, 2, 3, 4, 5, 10, 100], default=1)

filename_in_query = StringQueryFiled(name='filename', description='文件名',
                                     enum=['virtualmachine1.png', 'cellphone.png', '新建文件夹', '新建文件夹2'],
                                     required=True)
