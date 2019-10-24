#!C:\Users\duwns\AppData\Local\Continuum\anaconda3\python
#-*- coding: utf-8 -*-

import cgi, os

# 한글 사용 가능하게 하도록하는 코드
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("content-type:text/html; charset=utf-8\n")
print()
