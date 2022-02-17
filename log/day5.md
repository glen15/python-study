
# Day5

유저데이터모델 생성  
기존에서 확장  

스쿼시대회 관리를 위해 필요한 유저모델 생각해봐  

대회주최자 보조관리자 참가자 어드민

이름 등급 메일 전화 센터or팀

# Substituting a custom User model
https://docs.djangoproject.com/en/2.2/topics/auth/customizing/


## 기존 인스톨앱의 내용 장고앱으로 바꾸고 내가 만든 프로젝트 앱 따라 분류해서 합치기

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS  


users에서 
models.py에서 모델생성

config settings에서

PROJECT_APPS 만들어서
거기에 users 연결 apps.userConfig