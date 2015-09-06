# -*- coding: utf8 -*-
'''
@brief 异或加密, 解密
	   异或加密和解密同时通过对"每个字符"和"秘钥"进行异或
	   注意秘钥为""整形"
'''


'''
@brief 用key对content进行异或操作
'''
def XOR(content, key):
	result = u""
	for ch in content:
		temp = ord(ch)^key
		result += unichr(temp)
	return result


'''
@brief  编码加密
@params content 要编码加密的内容
        key     秘钥
'''
def encrypt_XOR(content, key):
	return XOR(content, key)

'''
@brief  解码解密
@params secretContent 要解密的内容
        key     秘钥
'''
def decrypt_XOR(secretContent, key):
	return XOR(secretContent, key)
	

if "__main__" == __name__:
	#要加密的内容
	content = u"123abc你好"
	#秘钥(必须整形)
	key     = 123
	
	decrypt_XOR(encrypt_XOR(content, key), key)
