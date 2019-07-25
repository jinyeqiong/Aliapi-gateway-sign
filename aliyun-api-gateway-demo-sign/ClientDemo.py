# -*- coding: utf-8 -*-
from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request
from com.aliyun.api.gateway.sdk.common import constant

host = "http://787f97ec61ed4e469c38b7dc72ebf82f-cn-beijing.alicloudapi.com"
url = "/user?first_pay_year=2019&partner_code=ahhdq&product_cd=59"
# url = "/user"


cli = client.DefaultClient(app_key="app_key", app_secret="app_secret")

# GET
req = request.Request(host=host, protocol=constant.HTTP, url=url, method="GET", time_out=30000)
print(cli.execute(req))


#post body stream

# import json
# req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="POST", time_out=30000)
# body = {}
# body["first_pay_year"] = "2019"
# body["partner_code"] = "ahhdq"
# body["product_cd"] = "59"
# print(json.dumps(body))
# req_post.set_body(body)
# req_post.set_content_type(constant.CONTENT_TYPE_STREAM)
# print(cli.execute(req_post))


#post form

# req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="POST", time_out=30000)
# bodyMap = {}
# bodyMap["first_pay_year"] = "2019"
# bodyMap["partner_code"] = "ahhdq"
# bodyMap["product_cd"] = "59"
# req_post.set_body(bodyMap)
# req_post.set_content_type(constant.CONTENT_TYPE_FORM)
# print(cli.execute(req_post))
