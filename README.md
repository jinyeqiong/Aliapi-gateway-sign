### 1、本示例的 Python 版本为python3
### 2、本demo主要是为了提供签名方法，调用示例可以参考 ClientDemo.py 文件
- 输入key和key_secret，直接运行ClientDemo就行
- 调用api网关详情：https://help.aliyun.com/document_detail/29490.html?spm=a2c4g.11186623.2.13.4b342c2bxATbqx
### 3、使用注意事项：
- 含有中文和空格的query, body在请求时需要对值进行urlencode处理，编码为utf-8.
- 参数参与签名时，必须使用原文签名，不能用urlencode后字符串的进行签名.所以请在签名之后再对query、body的值做urlencode.
- [签名文档](http://https://help.aliyun.com/document_detail/29475.html)