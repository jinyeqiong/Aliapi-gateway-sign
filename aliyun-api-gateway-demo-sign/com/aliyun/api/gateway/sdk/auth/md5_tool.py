# -*- coding:utf-8 -*-
#  Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# coding=utf-8

"""
MD5 tools module.

Created on 9/28/2015

@author: alex
"""

import hashlib
import base64


# def _get_md5(content):
#     m = hashlib.md5()
#     m.update(buffer(content))
#     return m.digest()

def _get_md5(name):
    hl = hashlib.md5()
    hl.update(str(name).encode(encoding='utf-8'))
    name_md5 = hl.hexdigest()
    return name_md5

def get_md5_base64_str(content):
    md5_base64 = base64.b64encode(_get_md5(content).encode('utf-8')).strip()
    print("md5_base64类型：", type(str(md5_base64, 'utf-8')))
    return str(md5_base64, 'utf-8')



