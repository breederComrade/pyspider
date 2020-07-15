# _*_ coding: utf-8 _*_
"""
  Created by wangjun on 2020/06/10.
  __author__ = 'wangjun'
"""
from collections import namedtuple

from flask.json import dumps

from flask import current_app, request


def jsonify(*args, **kwargs):
    indent = None
    separators = (',', ':')
    
    if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] or current_app.debug:
        indent = 2
        separators = (', ', ': ')
    
    if args and kwargs:
        raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
    elif len(args) == 1:  # single args are passed directly to dumps()
        data = args[0]
    else:
        data = args or kwargs
    return current_app.response_class(
        dumps(data, indent=indent, separators=separators) + '\n',
        mimetype=current_app.config['JSONIFY_MIMETYPE']
    ).json

def paginate():
    '''获取分页查询的参数
    :return: page第几页；size每页数据的规模
    '''
    from app.validators.forms import PaginateValidator
    validator = PaginateValidator().dt_data
    page_default = current_app.config.get('PAGE_DEFAULT')
    size_default = current_app.config.get('SIZE_DEFAULT')
    
    page = validator.get('page', page_default if page_default else 1)
    size = validator.get('size', size_default if size_default else 1)
    
    return page, size

def pageinateByBody():
    '''从body数据中获取查询分页参数
    :return : pageIndex 第几页; PageSize 每页显示数据规模
    '''
    from app.validators.forms import  PaginateValidatorByBody
    # 验证数据
    #
    validator = PaginateValidatorByBody().dt_data
    page_default = current_app.config.get('PAGE_DEFAULT')
    size_default = current_app.config.get('SIZE_DEFAULT')
    
    pageIndex = validator.get('pageIndex',page_default if page_default else 1)
    pageSize = validator.get('pageSize',size_default if size_default else 20)
    
    return pageIndex,pageSize

    
    
    
    
    
    
    
    
    


def time_interval():
    '''
    :return:
    '''
    from app.validators.forms import TimeIntervalValidator
    validator = TimeIntervalValidator().dt_data
    start = validator.get('start', None)
    end = validator.get('end', None)
    return start, end


def as_namedtuple(dict_obj):
    '''将字典类型转为namedtuple类型
    :param dict_obj: 字典
    :return:
    '''
    key_list, value_list = [], []
    for key, value in dict_obj.items():
        if value is not None:
            key_list.append(key)
            value_list.append(value)
    NamedTuple = namedtuple('NamedTuple', [key for key in key_list])
    return NamedTuple(*value_list)


def get_request_args(as_dict: bool = False):
    '''获取请求中的query和body中的所有参数
       并将数据集转为 字典类型 或者 namedtuple类型
    :param as_dict: 是否转为字典类型
    :return:
    '''
    data, args = request.get_json(silent=True), request.args.to_dict()
    args_json = dict(data, **args) if data is not None else args
    data = {
        key: value for key, value in args_json.items() if value is not None
    }
    return data if as_dict else as_namedtuple(data)
