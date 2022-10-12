# Djnago_Static files

### 정적 파일(Static file)

> 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
> 
- 파일 자체가 고정되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정
    - ex) 이미지, 자바 스크립트, CSS 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야 함
- 사용자의 요청에 따라 바뀌는 것이 아니라 요청한 것을 그대로 보여줌
- Django는 `staticfiles`라는 내장 앱을 통해 정적 파일과 관련된 기능을 제공

### 미디어 파일(Media File)

> 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
> 

### 웹 서버와 정적 파일

- 웹 서버의 기본 동작
    - 특정 위치(URL)에 있는 자원을 요청(HTTP request) 받아서
    - 응답(HTTP response)을 처리하고 제공(serving)하는 것
- 이는 자원과 자원에 접근 가능한 주소가 존재한다는 의미
    - 예를 들어, 사진 파일은 자원이고 해당 사진 파일을 얻기 위한 경로인 URL이 존재
- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(static resource)

### 소프트웨어 배포(Deploy)

- 프로그램 및 애플리케이션을 서버와 같은 기기에 설치하여 서비스를 제공하는 것
- 클라우드 컴퓨팅 서비스(AWS, Google Cloud, MS Azure 등)에 프로그램 및 애플리케이션을 설치해 제공하는 것)

## Django에서 Static files 구성하기

### 1. INSTALLED_APPS에  django.contrib.staticfiles가 포함되어 있는지 확인하기

### 2. settings.py에서 STATIC_URL을 정의하기

### 3. 앱의 static 폴더에 정적 파일을 위치하기

- 예시) my_app/static/sample_img.jpg

### 4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기

```sql
{% load static %}

<img src="{% static 'sample_img.jpg' %}" alt="sample img">
```

- `{% load %}`
    - `load tag`
    - 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
    - 파이썬의 import와 비슷
- `{% static '' %}`
    - `static tag`
    - `STATIC_ROOT`에 저장된 정적 파일에 연결

## Static files 관련 Core Settings

### 1. STATIC_ROOT

- Default : None(개발 과정에서는 필요 없기 때문)
- Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
- `collectstatic`이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
    
    ```python
    # settings.py
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    ```
    
    ```python
    python manage.py collectstatic
    ```
    
    - `STATIC_ROOT`에 Django 프로젝트의 모든 정적 파일을 수집하는 명령어
    - 즉, 개발 과정보다는 배포 시에 사용하는 명령어
- 개발 과정에서 settings.py의 `DEBUG`값이 `True`로 설정되어 있으면 해당 값은 작용하지 않음
- 실 서비스 환경(배포 환경)에서 Django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위해 사용
- 배포 환경에서는 Django를 직접 실행하는 것이 아니라, 다른 서버에 의해 실행되기 때문에 실행하는 다른 서버에게 Django에 내장되어 있는 정적 파일들의 위치를 알려줘야 함

### 2. STATICFILES_DIRS

- Default : [] (Empty list)
- `app/static/` 이라는 기본 디렉토리 경로를 사용하는 것 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
- 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함

```python
# settings.py

STATICFILES_DIRS = [
	BASE_DIR / 'static'.
]
```

### 3. STATIC_URL

- Default : None
- `STATIC_ROOT`에 있는 정적 파일을 참조 할 때 사용할 URL
- 개발 단계에서는 실제 정적 파일들이 저장되어 있는 `app/static/` 경로(기본 경로) 및 `STATICFILES_DIR`에 정의된 추가 경로들을 탐색
- 실제 파일이나 디렉토리가 아니며, URL로만 존재
- 비어 있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야 함

```python
# settings.py

STATIC_URL = '/static/'
```

## Static file 가져오는 2가지 방법

### 1. 기본 경로에 있는 static file 가져오기

- articles/static/articles 경로에 이미지 파일 배치하기
- static tag를 사용해 이미지 파일 출력하기

```python
<!-- articles/index.html -->

{% extends 'base.html' %}
{% load static %}

{% block content %}
  <img src="{% static 'articles/sample_img.jpg' %}" alt="sample img">
```

### 2. 추가 경로에 있는 static file 가져오기

- 추가 경로 작성

```python
# settings.py

STATICFILES_DIRS = [
	BASE_DIR / 'static'
]
```

- static tag를 사용해 이미지 파일 출력하기

```python
<!-- articles/index.html -->

{% extends 'base.html' %}
{% load static %}

{% block content %}
  <img src="{% static 'sample.jpg' %}" alt="sample img">
```

### STATIC_URL 확인

- Django가 해당 이미지를 클라이언트에게 응답하기 위해 만든 image url 개발자 도구에서 확인하기
- `STATICL_URL + Static file 경로`로 설정됨
    - ex) http://127.0.0.1:8000/static/articles/sample.jpg