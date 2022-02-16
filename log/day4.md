
# Day4
python manage.py makemigrations -> 모델만들기
1. migration 생성
2. mirgration 적용
3. 데이터베이스 업데이트됨

---
django project는 여러 app을 가진다  
project = app의 집합  
app = funtion의 집합  

ex)  
room app => room에 관한 CRUD function  
review app => review에 관한 CRUD function  

앱은 한문장으로 설명가능해야한다. and같은게 들어가면 그건 분리되어야한다  
---

django-admin startapp [appnames]  
앱 생성시 만들어진 파일들의 이름을 바꿀 수 없다 - 프레임워크잖아  
라이브러리 : 빌드하기위해 사용하는 것  
프레임워크 : 그 룰 안에서 작업해야함  

admin.py : admin 패널에 반영됨  
models.py : database가 어떻게 생겼는지 설명해주는 곳  
views.py : 사용자들이 보게될것  

config/urls.py : url을 컨트롤함  
각 앱에 urls.py 생성  