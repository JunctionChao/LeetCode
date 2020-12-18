#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
在用mongo等非关系型数据库时，不希望把脏数据，空数据存入数据库，造成混乱
写一个函数删除json dict里面的空数据，包括空dict, 空list, 空string, None
假设输入的python dict从合法json读取，即key必为string, 
value可以是number/string/list/dict
"""

def filter_null_data(data, types=(str, list, dict)):
    if data is None or (isinstance(data, types) and not data): # 空字符串，空列表，空字典
        return False
    else:
        return True


def clean_data(data, types=(str, list, dict)):
    col = []
    for k, v in data.items():
        if v is None:
            col.append(k)
        elif isinstance(v, str): 
            if not v:
                col.append(k)
        elif isinstance(v, list):
            if not v:
                col.append(k)
            else:
                v = list(filter(filter_null_data, v))
                v = [clean_data(i) if isinstance(i, dict) else i for i in v] # 这层清理后里列表里可能会存在None
                v = [i for i in v if i is not None] # 再次清理
                if not v: # 如果list被清空
                    col.append(k)
                else:
                    data[k] = v
        elif isinstance(v, dict):
            if not v:
                col.append(k)
            else:
                data[k] = clean_data(v)
                if data[k] is None:  # 清理后为None
                    col.append(k)

    for k in col:
        del data[k]

    if not data: # 字典清理后为空
        return None
    else:
        return data
    


if __name__ == '__main__':
    data1 = {"a":{1:2,3:None}}
    data2 = {"a":[1,0,"c",{"x":1}]}
    data3 = {"a":{"a":[None,"",{},{"x":None}]}}
    print(clean_data(data1))
    print(clean_data(data2))
    print(clean_data(data3))

    data4 = {"a":{"a":[None,"",{}, 5]}, "b":0, "c":[1, 2, [], {"a": None}, {"b": [1,2], "c":7}]}
    print(clean_data(data4))
