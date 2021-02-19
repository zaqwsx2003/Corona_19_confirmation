from urllib import request
from bs4 import BeautifulSoup
 
location = request.urlopen("http://ncov.mohw.go.kr/")
 
pll = BeautifulSoup(location, "html.parser")
 
nums = []
 
for dates in pll.select("div.datalist"):
    for data in dates.select("span.data"):
        nums.append(int(data.string))

print("오늘 코로나 확진자 수 :", sum(nums), "명 입니다.")
