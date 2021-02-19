# Corona_19_confirmation
---
개요
---
[중앙재난안전대책본부](http://ncov.mohw.go.kr/)에서 오늘의 코로나19 확진자를 출력해 주는 프로그램입니다.
---
1. 가장 먼저 Python을 설치를 해야 합니다. 
[Python 설치 링크](https://www.python.org/)

2.Python을 다운 받으면서 이 프로그램은 크롬에서 F12로 개발자도구를 열어 보시면, 확진자와 관련된 태그(요소)들을 찾아내실수 있을겁니다.
아래와 같은 모습으로 나와 있을 겁니다.
```
<div class="datalist">
  <ul>
    <li>
    <span class="subtit">...</span>
    <span class="data">47</span>
```
3. 콘솔창에 아래와 같은 Python 모듈을 설치해야 합니다.
```
> pip install BeautifulSoup
```
---
관련 모듈
---
[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
[Soupsieve](https://pypi.org/project/soupsieve/)
