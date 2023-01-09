import requests
from bs4 import BeautifulSoup

def crawling(soup):
  result = []

  tb = soup.find('tbody')
  # print(tb) # 추출 확인
  # print('-------')

  for p in tb.find_all('p', class_ = 'title'):
    # print(p.get_text()) # 추출 확인
    result.append(p.get_text().replace("\n","")) # \n 제거

  return result

def main():
  url = 'https://music.bugs.co.kr/chart'
  custom_header = {
      'referer' : 'https://www.google.com/',
      'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
  }

  req = requests.get(url, headers = custom_header)
  # print(req.status_code) # 확인 코드
  # print(req.text) # 내용 확인

  soup = BeautifulSoup(req.text, "html.parser")
  result = crawling(soup) # 리스트에 담기
  print('--------- 최종 결과 ---------')
  print(result)

if __name__ == "__main__":
  main()