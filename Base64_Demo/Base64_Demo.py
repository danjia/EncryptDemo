# -*- coding: utf8 -*-
'''
@brief 用base64加密,解密(必须为ascii)
'''
import base64


'''
@brief  编码加密
@params content 要编码加密的内容(必须为ascii)
'''
def encrypt_base64(content):
    return base64.b64encode(content)

'''
@brief  解码解密
@params secretContent 要解密的内容
'''
def decrypt_base64(secretContent):
    return base64.b64decode(secretContent)


if "__main__" == __name__:
    #要加密的内容
    content = u"123456789ABCDEFGabcefgd"
    #加密
    secretContent = encrypt_base64(content)
    print(secretContent)
    #解密
    print(decrypt_base64(secretContent))
