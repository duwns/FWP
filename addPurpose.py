#!C:\Users\duwns\AppData\Local\Continuum\anaconda3\python
import cgi
import os 
from datetime import datetime

# 한글 사용 가능하게 하도록하는 코드
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


# url에 있는 parameter 가져오기
form = cgi.FieldStorage()
print("content-type:text/html; charset=UTF-8\n")
print(form)

print(form["purpose"].value)

now = datetime.now()

print('0 '+ str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '. ' + form["purpose"].value)


f = open('data.txt', 'a')
f.write('0 ' + str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '. ' + form["purpose"].value)
f.write("\n")
f.close()

print("<script>location.href = 'http://google.com'</script>")




# html css javascript 들으시고 (생코 프로젝트 따라하면서 하기)
# row index값을 0으로 직접 집어넣는 것이 아니라 변수로 집어넣어
# 마지막에 넣은 index 값 +1 을 항상 넣어 준다.
# css 고치고 싶으면 고쳐보시고
