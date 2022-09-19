# Django_Intro

# Framework

> 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것
> 
- 소프트웨어의 생산성과 품질을 UP ⬆️

# WWW(World Wide Web)

> 전 세계에 퍼져 있는 거미줄 같은 연결망
> 

---

# 클라이언트-서버 구조

## 클라이언트

> 웹 사용자의 인터넷에 연결된 장치
> 
- ex) (Chrome, Firefox)와 같은 웹 브라우저, 서비스를 요청하는 주체

## 서버

> 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
> 
- 클라이언트가 웹 페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시
- 요청에 대해 서비스를 응답하는 주체

---

# Web browser & Web page

## Web browser

> 웹에서 페이지를 찾아 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
> 
- 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는 (렌더링, rendering) 프로그램

## Web page

> 웹에 있는 문서로 우리가 보는 화면 각각 한 장 한 장이 웹 페이지
> 

### Web page 종류

- 정적 웹 페이지
    - HTML 파일의 내용이 변하지 않고 사용자에게 동일한 모습으로 전달 되는 웹 페이지
- 동적 웹 페이지
    - 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달 되는 웹 페이지
    

---

# Design Pattern

> 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙, 커뮤니케이션의 효율성을 높이는 기법
> 

## 소프트웨어 디자인 패턴의 장점

- 특정 문맥에서 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책을 제시
- 디자인 패턴을 알고 있다면 서로 복잡한 커뮤니케이션이 매우 간단해짐

## Django의 디자인 패턴

### **MVC 패턴**

> **MTV 패턴**의 기반이자 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론
> 
- 역할
    - **Model**
        - 데이터와 관련된 로직을 관리
    - **View**
        - 레이아웃과 화면을 처리
    - **Controller**
        - 명령을 model과 view 부분으로 연결
- 목적
    - 관심사 분리
    - 더 나은 업무의 분리와 향상된 관리를 제공
    - 개발 효율성 및 유지보수
    - 다수의 멤버로 개발하기 용이

### **MTV 패턴**

> Django에 적용된 디자인 패턴
> 
- MVC 패턴과의 차이점
    - 일부 역할에 대해 부르는 이름이 다름
- 역할
    - **Model**
        - 데이터와 관련된 로직을 관리
        - 데이터 구조 정의
        - 데이터베이스의 기록 관리
        - MVC 패턴에서 Model의 역할
    - **Template**
        - 레이아웃과 화면을 처리
        - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
        - MVC 패턴에서 View의 역할
    - **View**
        - Model & Template과 관련한 로직을 처리해서 응답을 반환
        - 클라이언트의 요청에 대해 처리를 분기하는 역할
        - MVC 패턴에서 Controller의 역할

---

# Django

## Django 설치

```bash
pip install django
```

- django 뒤에 버전을 입력함으로써 원하는 버전 설치가 가능
- 패키지 목록 생성
    
    ```bash
    pip freeze > requirements.txt 
    ```
    

## Django Project

- 프로젝트 생성
    
    ```bash
    django-admin startproject firstpjt .
    ```
    
    - Project 이름에는 Python이나 Django에서 사용 중인 키워드 및 ‘-’사용 불가
    - ‘.’을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성하게 됨
- 서버 실행
    
    ```bash
    python manage.py runserver
    ```
    

### Project 구조

- __init__.py
    - Python에게 이 디렉토리를 하나의 패키지로 다루도록 지시
    - 별도로 추가 코드 작성 X
- asgi.py
    - Asynchronous Server Gateway Interface
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
    - 추후 배포 시에 사용
- settings.py
    - Django 프로젝트 설정을 관리
- urls.py
    - 사이트의 url과 적절한 views의 연결을 지정
- wsgi.py
    - Web Server Gateway Interface
    - Django 애플리케이션이 웹 서버와 연결 및 소통하는 것을 도움
    - 추후 배포 시에 사용
- manage.py
    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

## Django Application

- 애플리케이션 생성
    
    ```bash
    python manage.py startapp articles
    ```
    

### 애플리케이션 구조(articles)

- admin.py
    - 관리자용 페이지를 설정하는 곳
- apps.py
    - 앱의 정보가 작성된 곳
    - 별도로 추가 코드를 작성하지 않음
- models.py
    - 애플리케이션에서 사용하는 Model을 정의하는 곳
    - MTV 패턴의 M에 해당
- tests.py
    - 프로젝트의 테스트 코드를 작성하는 곳
- views.py
    - view 함수들이 정의되는 곳
    - MTV 패턴의 V에 해당

### 애플리케이션 등록

- 프로젝트에서 앱을 사용하기 위해서는 반드시 **settings.py**의 `INSTALLED_APPS` 리스트에 반드시 추가해야 함
    - 꼭 생성 후에 settings.py에 추가를 해야함
- 직접 선언한 앱 → 외부 라이브러리 → 장고 기본 라이브러리 순으로 추가

## Project & Apllication

- Project
    - collection of apps
    - 프로젝트는 앱의 집합
    - 앱은 여러 프로젝트에 있을 수 있음
- Application
    - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
    - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장
    

---

# 요청과 응답

> URL → VIEW → TEMPLATE 순의 작성 순서로 코드를 작성
> 

## URLs.py

```python
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
		path('admin/', admin.site.urls),
		path('index/', views.index),
]
```

## Views.py

```python
def index(request):
		return render(request, 'index.html')
```

- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
- Template에게 HTTP 응답 서식을 맡김

### render()

```python
redner(request, template_name, context)
```

- 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수
    1. request
        - 응답을 생성하는 데 사용되는 요청 객체
    2. template_name
        - 템플릿의 전체 이름 또는 템플릿 이름의 경로
    3. context
        - 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)

## templates

- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의
- templates 파일의 기본 경로
    - app 폴더 안의 templates 폴더
    - app/templates/{index.html}

---

# Django Template

> 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
> 
- Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입
- Template System의 기본 목표를 숙지

## Django Template System

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직을 담당

## Django Template Language(DTL)

- Django template에서 사용하는 built-in template system
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
    - Python처럼 일부 프로그래밍 구조(if, for등)를 사용할 수 있지만 Python코드로 실행 X
    - Django 템플릿 시스템은 Python이 HTML에 포함된 것이 아님
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심

## DTL Syntax

### Variable

```html
{{ variable }}
```

- 변수명은 영어, 숫자와 밑줄(-)의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
    - 공백이나 구두점 문자 또한 사용할 수 없음
- dot(.)을 사용하여 변수 속성에 접근할 수 있음
- render()의 세번째 인자로 {’key’:value}와 같이 딕셔너리 형태로 넘겨주며, 
여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨

### Filters

```html
{{ variable|filter }}
```

- 표시할 변수를 수정할 때 사용
- ex)
    - name 변수를 모두 소문자로 출력 `{{ name|lower }}`
- 60개의 built-in template filters를 제공
- chained가 가능하며 일부 필터는 인자를 받기도 함 `{{ name|truncatewords:30 }}`

### Tags

```html
{% tag %}
```

- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요 `{% if % }{% endif %}`
- 약 24개의 built-in template tags를 제공

### Comments

```html
{# #}
```

- Django template에서 라인의 주석을 표현하기 위해 사용
- 아래처럼 유효하지 않은 템플릿 코드가 포함될 수 있음
    - `{# {% if %} text {% endif %} #}`
- 한줄 주석에만 사용할 수 있음(줄 바꿈이 허용X)
- 여러 줄 주석은 {% comment %}와 {% endcomment %} 사이에 입력

---

# 템플릿 상속

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤
- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 
하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 ‘skeleton’ 템플릿을 만들 수 있음

## 템플릿 상속에 관련된 태그

```html
{% extends '' %}
```

- 반드시 템플릿 최상단에 작성 되어야 함(즉, 2개 이상 사용할 수 없음)

```html
{% block content %}{% endblock content %}
```

- 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의
- 즉, 하위 템플릿이 채울 수 있는 공간
- 가독성을 높이기 위해 선택적으로 endblock 태그에 이름을 지정할 수 있음

### 추가 템플릿 경로 추가하기

- 기본 template 경로가 아닌 다른 경로를 추가하기 위해 코드를 아래와 같이 작성
    - settings.py
        
        ```html
        TEMPLATES = [
        		{
        				...
        				'DIRS': [BASE_DIR / 'templates',],
        				...
        ```
        
- **BASE_DIR**을 사용하여 앱의 최상위 위치 지정 가능

### BASE_DIR

> settings.py에서 특정 경로를 절대 경로로 편하게 작성할 수 있도록 Django에서 미리 지정해둔 경로 값
> 

---

# Sending form data (Client)

## HTML <form> element

> 사용자로부터 할당된 데이터를 서버로 전송
> 

### 핵심 속성

- action
    - 입력 데이터가 전송될 URL을 지정
    - 데이터를 어디로 보낼 것인지 지정
- method
    - 데이터를 어떻게 보낼 것인지 정의
    - **GET**방식과 **POST**방식이 존재
        - **GET** 방식 : 보안이 취약
        - **POST** 방식 : JSON으로 변환하기에 보안에 강점을 보임

## HTML <input> element

> 사용자로부터 데이터를 입력 받기 위해 사용
> 
- `type` 속성에 따라 동작 방식이 달라진다.

### 핵심 속성

- name
    - form을 통해 데이터를 제출(submit)했을 때 name 속성에 설정된 값을 서버로 전송하고,
    서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음.
    - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것
        - GET 방식에서는 URL에서 `'?key=value&key=value/'` 형식으로 데이터를 전달

## HTTP request methods

- HTTP
    - HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- HTTP는 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의
- 자원에 대한 행위를 정의
- 주어진 리소스에 수행하길 원하는 행동을 나타냄
- HTTP method 예시
    - GET, POST

## GET

> 서버로부터 정보를 조회하는데 사용
> 
- 데이터를 가져올 때만 사용
- 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
- `<form>`의 기본 설정값이지만 좀 더 직관적으로 파악하기 위해 GET으로 꼭 명시해주기

---

# Retrieving the data(Server)

> 데이터 가져오기
> 
- 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게 됨
- 이러한 목록에 접근하는 방법은 사용하는 특정 프레임워크에 따라 다름

## Catch 작성

1. `throw.html` 의 <form>에서 action을 catch로 변경
    
    ```html
    <form action="/catch/" method="GET"> 
    ```
    
2. urls.py의 urlpatterns에 catch 추가
    
    ```python
    urlpatters = [
    		...
    		path('catch/', views.catch)
    ]
    ```
    
3. views.py의 catch 함수 생성
    - request.GET.get()함수를 이용하여 메세지 가지고 오기
    
    ```python
    def catch(request):
    		message = request.GET.get('message') # throw에서 사용한 name
    		context = {
    				'message' : message
    		}
    		return render(request, 'catch.html', context)
    ```
    
4. templates/에 catch.html 생성(상속 이용)
    
    ```html
    {% extends 'base.html' %}
    
    {% block content %}
    <h1>catch로 받아오기</h1>
    <h2>catch : {{ message }}</h2>
    <a href="/throw/">또 전송해보기</a>
    {% endblock content %}
    ```
    

---

# Variable routing

> URL 주소를 변수로 사용하는 것
> 
- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

## Variable routing 작성

- 변수는 `<>`에 정의하며 view 함수의 인자로 할당됨
- 기본 타입은 string이며 5가지 타입으로 명시 가능
    1. str
        - `/`를 제외하고 비어있지 않은 모든 문자열
        - 작성하지 않을 경우 기본 값
    2. int
    3. slug
    4. uuid
    5. path 
- ex)
    - urls.py
    
    ```python
    urlpatterns = [
    		..., 
    		path('hello/<name>/', views.hello), 
    ]
    ```
    
    - views.py
    
    ```python
    def hello(request, name):
    		context = {
    				'name' : name,
    		}
    		return render(request, 'hello.html'. context) 
    ```
    
    - hello.html
    
    ```html
    {% extends 'base.html' %}
    {% block centent %}
    		<h1>만나서 반가워요 {{name}}님!</h1>
    {% endblock content %}
    ```
    

# App URL mapping

> 앱이 많아졌을 때 urls.py를 각 app에 매핑
> 
- app의 view함수가 많아지면서 사용하는 path() 또한 많아지고, app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지 보수에 좋지 않음
- 이를 위한 해결 방법
    - **각각의 app 폴더 안에 urls.py를 작성**
        
        ```python
        # articles/urls.py
        from django.urls import path
        from . import views
        
        urlpatterns = [
        		...
        		...
        ]
        
        # pages/urls.py
        from django.urls import path
        
        urlpatterns = [
        ]
        ```
        
    - include를 사용
        
        ```python
        # fisrtpjt/urls.py
        from django.contrib import admin
        from django.urls import path, include
        
        urlpatters = [
        		path('admin/', admin.site.urls),
        		path('articles/', include('articles.urls'),
        		prth('pages/', include('pages.urls'),
        ]
        ```
        
        - include에 들어가는 앱의 urls.py에는 반드시 빈 urlpatterns라도 존재해야 한다.

# Naming URL patterns

> 링크에 URL을 직접 작성하는 것이 아니라 `path()`함수의 name 인자를 정의해서 사용하는 패턴
> 
- DTL의 tag 중 하나인 `URL` 태그를 사용해서 `path()` 함수에 작성한 name을 사용할 수 있음
- 이를 통해 URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음
- Django는 URL에 이름을 지정하는 방법을 제공함으로써 view 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움

## URL tag

- 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
- 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크 출력 가능

## DRY(Don’t Repeat Yourself) 원칙

> 소스 코드에서 동일한 코드를 반복하지 말자
> 
- 동일한 코드가 반복된다는 것은 잠재적인 버그의 위협을 증가
- 반복되는 코드를 변경해야 하는 경우, 반복되는 코드를 모두 찾아서 수정해야 함
- 프로젝트 규모가 커질수록 애플리케이션의 유지 보수 비용이 커짐

# Django의 설계 철학(Templates System)

1. 표현과 로직(view)을 분리
    - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일뿐
    - 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 함
2. 중복을 배제
    - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 가짐
    - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애햐 함
    - 템플릿 상속의 기초가 되는 철학