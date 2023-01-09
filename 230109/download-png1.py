# page 9
import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = 'test.png'

#다운로드
urllib.request.urlretrieve(url, savename)
print('저장되었습니다')