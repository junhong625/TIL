# Django_Model

# Database

> 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
> 
- 체계화된 데이터의 모임

## Database의 구조

### 스키마(Schema)

> 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
> 
- 간단히 얘기하여 데이터베이스의 뼈대(Structure)
- 

| column | datatype |
| --- | --- |
| id | Int |
| name | Text |

### 테이블(Table)

> 필드와 레코드를 사용해 조작된 데이터 요소들의 집합
> 
- 필드(field)
    - 속성, 열(column)
    - 각 필드에는 고유한 데이터 타입이 지정
- 리코드(record)
    - 튜플, 행(row)
    - 테이블의 데이터는 레코드에 저장

### PK(Primary Key)

> 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(Unique)
> 
- 기본 키
- 고유한 값
- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용
- ex) 주민등록번호

### 쿼리(Query)

> 데이터를 조회하기 위한 명령어
> 
<br>
<br>

# Django Model

> Django에서 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구
> 
- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
    - 모델 클래스 1개 == 데이터베이스 테이블 1개

## Model 작성

- 앱 내의 models.py 작성
    - 모델 클래스를 작성하는 것은 데이터베이스 **테이블의 스키마를 정의**하는 것
    - id 컬럼(pk)은 테이블 생성 시 Django가 자동으로 생성
    
    ```python
    from django.db import models
    
    class Article(models.Model): # models.Model클래스를 상속
    		title = models.CharField(max_length=10) # title 필드 정의
    		content = models.TextField() # content 필드 정의
    		created_at = models.DateTimeField(auto_now_add=True) # 생성 시각 정의
            updated_at = models.DateTimeField(auto_now=True) # 수정 시각 정의
    ```
    
    - models.CharField(max_length=10)
        - CharField타입
            - 길이의 제한이 있는 문자열(최대 길이 : 255)
            - `max_length` attribute 필수로 작성
    - models.TextField()
        - TextField타입
            - 많은 문자열 입력이 필요할 시 사용
                - database에 따라 최대 크기가 달라지기에 위와 같이 설명
            - 필수 attribute가 없음
    - models.DateTimeField()
        - DateTimeField타입
            - 날짜와 시간을 받는 타입
            - option으로 `auto_now_add`와 `auto_now`가 존재
                - `auto_now_add` : True로 설정 시 처음 생성했을 때의 시각으로 저장
                - `auto_now` : True로 설정 시 수정했을 때의 시각으로 변경
- 위와 같이 클래스 상속 기반 형태의 Django를 사용함으로써 더욱 편리하게 기능을 생성 가능

<br>
<br>

# Migrations

> Django가 모델에 생긴 변화(필드 추가, 수정 등)를 실제 DB에 반영하는 방법
> 

## 주요 명령어

### makemigrations

> Model의 변경사항에 대해 새로운 migration을 만들 때 사용
> 

```bash
python manage.py makemigrations
```

### migrate

> makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정(db.sqlite3 파일에 반영)
> 
- 모델의 변경 사항과 데이터베이스를 동기화

```bash
python manage.py migrate
```

## 데이터베이스 확인

### sqlite 다운(vs code)

- db.sqlite3파일 우클릭 후 open database 클릭
- SQLITE EXPLORER를 통해 동기화된 데이터베이스를 확인 가능

## 기타 명령어

### showmigrations

> migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
> 

```bash
python manage.py showmigrations
```

### sqlmigrate

> migrate를 통해 생성한 설계도를 SQL문으로 보는 용도
> 

```bash
python manage.py sqlmigrate [앱 이름] [번호]
```

## 추가 필드 정의

> 추가 필드를 DB에 적용 시키기 위해서는 다시 한 번 migration 작업이 필요
> 
- 기본적으로 컬럼들은 빈 값을 갖고 추가될 수 없음
- 그렇기에 추가되는 컬럼에 대한 기본 값을 설정하기 위해 어떤 값을 기본 값으로 설정할 것인지 물어보게 됨
- 두 가지의 선택지가 주어짐
    1. 다음 화면으로 넘어가서 새 컬럼의 기본 값을 직접 입력
    2. 현재 과정에서 나가고 모델 필드에 default 속성을 직접 작성하는 방법
- 1번 선택지를 선택 시 형식에 맞게 기본 값을 설정해주기에 1번 선택지를 추천
- 이후 기존 설계도를 덮어쓰는 것이 아닌 새로운 설계도를 생성
    - 로그와 같이 이전 설계도들을 기록하기 위함
    - 새로 생성된 설계도는 이전 설계도에 dependency하고 있음
    - 즉, 이전 설계도가 존재해야 의미가 있음
- 모든 작업이 끝난 후 migrate를 해줘야 DB에 반영이 이루어짐!!!

### DateTimeField()

> Python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드
> 
- 선택 인자
    1. auto_now
        - 최종 수정 일자
        - 데이터가 수정될 때마다 현재 날짜와 시간으로 갱신
    2. auto_now_add
        - 최초 생성 일자
        - 데이터가 실제로 만들어질 때의 현재 날짜와 시간으로 자동 설정

<br>
<br>

# ORM(Object-Relational-Mapping)

> 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술
> 
- Django에는 내장 **Django ORM**을 사용
- 즉, SQL을 사용하지 않고도 데이터베이스를 조작할 수 있게 만들어주는 기술

### 장점

- SQL을 잘 알지 못해도 객체 지향 언어로 DB 조작이 가능
- 객체 지향적 접근으로 인한 **높은 생산성**

### 단점

- ORM 만으로 세밀한 데이터베이스 조작을 구현하기 어려운 경우

# QuerySet API

> QuerySet과 상호 작용하기 위해 사용하는 도구
> 

## 설치 및 설정

- 라이브러리 설치
    
    ```bash
    pip install ipython django-extension
    ```
    
    - ipython
        
        > 파이썬 기본 쉘보다 더 강력한 파이썬 쉘
        > 
    - django-extension
        
        > Django 확장 프로그램 모음
        > 
        - shell_plus, graph model 등 다양한 확장 기능 제공
- 환경 설정
    
    ```bash
    # project의 settings.py
    
    INSTALLED_APPS = [
    ...,
    'django_extensions',
    ...,
    ]
    ```
    
- 패키지 목록 업데이트
    
    ```bash
    pip freeze > requirements.txt
    ```
    

## Django shell 실행

```bash
python manage.py shell_plus
```

- django shell과 ipython이 동시에 실행

### objects manager

> DB를 Python Class로 조작할 수 있도록 여러 메서드를 제공하는 manager
> 
- Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
- Django는 기본적으로 모델 클래스를 생성 시 **objects**라는 Manager 객체를 자동으로 추가

### Query

> 데이터베이스에 특정한 데이터를 보여 달라는 요청
> 

### QuerySet

> 데이터베이스에게서 전달 받은 순회가 가능한 데이터
> 
- Django ORM을 통해 만들어진 자료형으로, 필터를 걸거나 정렬 등을 수행 가능
- **objects manager**를 사용하여 **복수**의 데이터를 가져오는 메서드를 사용할 때 반환되는 객체

### CRUD

> 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지
> 
- Create : 생성
- Read : 조회
- Update : 수정
- Delete : 삭제

## CREATE(데이터 객체 생성)

### 1번째 방법

```python
article = Article() # 생성한 모델 클래스를 통해 인스턴스 생성
article.title = '제목' # 미리 생성했던 인스턴스 변수(속성)에 값 할당
article.content = '내용' # 미리 생성했던 인스턴스 변수(속성)에 값 할당
article.save() # save 메서드를 통해 DB에 반영
```

### 2번째 방법

```python
article = Article(title='제목', content='내용') # 인스턴스를 생성하며 즉시 인스턴스 변수(속성)에 할당
article.save() # save 메서드를 통해 DB에 반영
```

### 3번째 방법

```python
Article.objects.create(title='제목', content='내용') # objects의 create 메서드를 사용하여 즉시 DB에 반영
```

## READ(데이터 조회)

### all()

> 전체 데이터를 조회하여 QuerySet으로 반환
> 
- QuerySet return → 순회 가능한 복수의 데이터
- 전체 데이터 조회

### get()

> **Primary Key와 같은 고유성을 보장하는 데이터를 조회할 때 사용해야 함**
> 
- 단일 데이터 조회
- 객체를 찾을 수 없을 경우 DoesNotExist 예외 발생
- 둘 이상의 객체를 찾을 경우 MultipleObjectsReturned 예외 발생

### filter()

> 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
> 
- 조회된 객체가 없거나 1개여도 QuerySet을 반환
- 데이터가 없을 경우 에러가 발생하지 않기에 PK 데이터를 조회 시 사용 X

### Field lookups

> 특정 레코드에 대한 조건을 설정
> 
- 필요 시 [공식 문서](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups) 참고
- ex)
    
    ```python
    Article.objects.filter(content__contains='ja') # content에 'ja'를 포함하고 있는데 데이터 조회
    ```
    

## UPDATE(데이터 수정)

> 수정을 할 시에는 반드시 먼저 수정할 데이터를 조회해야 함
> 

### 수정 방법

```python
article = Article.objects.get(pk=1) # 수정할 데이터를 조회
article.content = 'DJANGO' # 데이터 수정
article.save() # DB에 반영
```

## DELETE(데이터 삭제)

> 삭제할 데이터를 반드시 먼저 조회해야 함
> 

### 삭제 방법

```python
article = Article.objects.get(pk=1) # 삭제할 데이터를 조회
article.delete() # 데이터 삭제
```

- 삭제를 한 이후 데이터를 생성하면 비어있는 PK로 생성되는 것이 아니라 마지막으로 생성했던 레코드 PK의 다음 PK로 생성됨

<br>
<br>

# VIEWS.PY에서 CRUD사용

## READ

### urls.py

```python
# 앱/ urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]
```

### views.py

```python
# 앱/views.py

from django.shortcuts import render
from .model import Article # 생성한 클래스 import

def index(request): # READ
		articles = Article.objects.all() # 전체 데이터 조회
		context = { # dict 형식으로 전체 데이터 저장
				'articles' : articles
		}
		return render(request, 'articles/index.html', context # articles폴더의 index.html 파일에 context를 전달
```

### index.html

```html
{% extends 'base.html' %} <!-- bast.html 상속 -->

{% block content%}
    <h1>Articles</h1>
		<a href="{% url 'articles:new' %">NEW</a>
    <hr>
    {% for article in articles %} <!-- 입력받은 context에서 key가 articles인 value들을 받아 하나씩 꺼내 for문으로 순회 -->
        <p>글 번호: {{ article.pk }}</p> <!-- 각각의 레코드에서 pk를 variable로 출력 -->
        <p>제목: {{ article.title }}</p> <!-- 각각의 레코드에서 title을 variable로 출력 -->
        <p>내용: {{ article.content }}</p> <!-- 각각의 레코드에서 content를 variable로 출력 -->
				<hr>
    {% endfor %}
{% endblock content%}
```

## CREATE

> CREATE를 구현하기 위해서는 두 개의 view 함수가 필요함
> 
1. 글을 작성할 페이지를 render하는 함수
2. 작성한 페이지에서 데이터를 받아 DB에 저장하는 함수

### GET

> 특정 리소스를 가져오도록 요청할 때 사용
> 
- DB의 형태가 URL에 표시되기 때문에 반드시 데이터를 가져올 때만 사용해야 함
- DB에 변화 X
- CRUD에서 R담당

### POST

> 서버로 데이터를 전송할 때 사용
> 
- GET과 다르게 URL로 보내지지 않음
- csrf_token이 반드시 필요함
- CRUD에서 C/U/D의 역할을 담당

### CSRF-Token(Cross-Site-Request-Forgery Token)

> 사이트 간 요청 위조를 막기 위해 token값이 유효한지 검증하는 기법
> 
- Django에서는 csrf_token 템플릿 태그를 사용

### urls.py

```python
# 앱/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
		path('new/', views.new, name='new'),
		path('create/', views.create, name='create'),
]
```

### views.py

```python
# 앱/views.py

from django.shortcuts import render, redirect
from .model import Article # 생성한 클래스 import

...

def new(request): # CREATE 첫번째 함수
		return render(request, 'articles/new.html') # articles폴더의 new.html 파일로 이동

def create(request): # CREATE 두번째 함수
		# 사용자의 데이터 변수에 저장
		title = request.POST.get('title') # 전송받은 데이터 중 key가 title인 데이터를 title 변수에 저장
		content = request.POST.get('content')	# 전송받은 데이터 중 key가 content인 데이터를 content 변수에 저장 
		
		# DB에 저장
		article = Article(title=title, content=content) # 인스턴스 생성하면서 각 속성에 데이터 삽입
		article.save() # DB에 반영
		return redirect('articles:index') # 생성 완료 후 index페이지로 이동
	# return redirect('articles:detail', article.pk) # 생성 후 입력한 데이터의 detail 페이지로 바로 이동
```

### new.html

```html
# templates/articles/new.html

{% extends 'base.html' %} <!-- base.html 상속 -->

{% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST"> <!-- 입력받은 데이터를 articles의 urls.py의 name이 create인 path로 전송, 전송 방식은 POST -->
        {% csrf_token %} <!-- POST 방식으로 전송하기 위해서는 csrf_token 필수 -->
        <label for="title">TITLE: </label> <!-- for은 같은 name을 찾아 해당 태그로 이동 -->
        <input type="text" name='title'><br> <!-- name은 데이터를 전송할 때 key의 역할, 전송한 데이터를 name을 key로 이용하여 데이터를 읽어들임-->
        <label for="content">CONTENT: </label>
        <textarea name="content"></textarea><br>
        <input type="submit" value='작성'> <!-- 작성을 누를 시 action으로 전송-->
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">BACK</a> <!-- BACK을 누를 시 articles의 urls.py에서 name이 index인 path로 이동 -->
{% endblock content %}
```

### index.html

```html
<!-- 새로운 데이터를 입력할 NEW 반영 -->

{% extends 'base.html' %} <!-- bast.html 상속 -->

{% block content%}
    <h1>Articles</h1>
		<a href="{% url 'articles:new' %">NEW</a> <!-- articles의 urls.py에서 name이 new인 path로 이동  -->
    <hr>
    {% for article in articles %} <!-- 입력받은 context에서 key가 articles인 value들을 받아 하나씩 꺼내 for문으로 순회 -->
        <p>글 번호: {{ article.pk }}</p> <!-- 각각의 레코드에서 pk를 variable로 출력 -->
        <p>제목: {{ article.title }}</p> <!-- 각각의 레코드에서 title을 variable로 출력 -->
        <p>내용: {{ article.content }}</p> <!-- 각각의 레코드에서 content를 variable로 출력 -->
				<hr>
    {% endfor %}
{% endblock content%}
```

## READ 2(detail)

> 글의 번호(PK)를 활용해서 개별 게시글 상세 페이지 조회
> 
- variable routing을 활용 <int:pk>

### urls.py

```python
 # 앱/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
		path('new/', views.new, name='new'),
		path('create/', views.create, name='create'),
		path('<int:pk>/', views.detail, name='detail'), # variable routing을 활용
]
```

### views.py

```python
# 앱/views.py

from django.shortcuts import render, redirect
from .model import Article # 생성한 클래스 import

...

def detail(request, pk):
		article = Article.objects.get(pk=pk) # DB에서 pk로 데이터를 조회하여 article 변수에 할당
		context = { # article변수에 저장한 데이터 context에 dict형태로 저장
				'article' : article
		}
		return render(request, 'articles/detail.html', context) # articles폴더의 detail.html에 context 전달 
```

### detail.html

```html
{% extends 'base.html' %}

{% block content %}
    <h2>DETAIL</h2>
    <h3>{{ article.pk }} 번째 글</h3> <!-- views에서 전송한 context에 있는 key가 article인 데이터의 pk 출력 -->
    <hr>
    <p>제목: {{ article.title }}</p> <!-- views에서 전송한 context에 있는 key가 article인 데이터의 title 출력 -->
    <hr>
    <p>내용: {{ article.content }}</p> <!-- views에서 전송한 context에 있는 key가 article인 데이터의 content 출력 -->
    <hr>
    <p>작성 시각: {{ article.created_at }}</p> <!-- views에서 전송한 context에 있는 key가 article인 데이터의 created_at 출력 -->
    <hr>
    <p>수정 시각: {{ article.updated_at }}</p> <!-- views에서 전송한 context에 있는 key가 article인 데이터의 updated_at출력 -->
    <hr>
    <hr>
    <a href="{% url 'articles:edit' article.pk %}">EDIT</a><br> <!-- articles의 urls.py에서 name인 edit인 path로 article의 pk데이터를 전송하여 이동 -->
    <a href="{% url 'articles:index' %}">BACK</a> <!-- articles의 urls.py에서 name인 index인 path로 이동 -->
{% endblock content %}
```

## DELETE

> 데이터 삭제
> 

### urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

### views.py

```python
# 앱/views.py

from django.shortcuts import render, redirect
from .model import Article # 생성한 클래스 import

...

def delete(request, pk):
		article = Article.objects.get(pk=pk) # DB에서 pk로 데이터를 조회하여 article 변수에 할당
		article.delete() # article에 저장된 데이터 삭제
		return redirect('articles:index') # articles의 urls.py에서 name이 index인 path로 이동
```

## UPDATE

> 데이터를 수정하기 위해서는 생성할 때와 마찬가지로 두 개의 함수가 필요
> 
1. 수정할 페이지를 render하는 함수
2. 수정한 페이지에서 데이터를 받아 DB에 저장하는 함수

### urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

### views.py

```python
# 앱/views.py

from django.shortcuts import render, redirect
from .model import Article # 생성한 클래스 import

...

def edit(request, pk): # 수정할 페이지로 이동하는 함수
    article = Article.objects.get(pk=pk) # 수정할 데이터를 조회해서 article변수에 할당
    context = { # article변수에 저장된 데이터를 context에 dict형태로 저장
        'article': article,
    }
    return render(request, 'articles/edit.html', context) # articles폴더의 edit.html로 context를 전달

def update(request, pk): # 수정을 반영하는 함수
    article = Article.objects.get(pk=pk) # 수정할 데이터를 조회해서 article변수에 할당
    article.title = request.POST.get('title') # 수정한 데이터 중 key가 title인 데이터를 가져와 article의 title에 할당
    article.content = request.POST.get('content') # 수정한 데이터 중 key가 content인 데이터를 가져와 article의 content에 할당
    article.save() # 변경사항 저장 및 반영
    return redirect('articles:detail', article.pk) # 수정 완료 후 articles의 urls.py 중 name이 detail인 path에 수정 완료한 데이터의 pk를 전달
```

### edit.html

```html
{% extends 'base.html' %} <!-- base.html 상속 -->

{% block content %}
    <h1>EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}" method="POST"> <!-- 수정한 데이터를 articles의 urls.py에서 name이 update인 path에 context로 들어온 article의 pk데이터와 함께 POST 방식으로 전송 -->
        {% csrf_token %} <!-- POST 방식 전송을 위한 token -->
        <label for="title">TITLE: </label>
        <input type="text" name="title" value="{{ article.title }}"><br> <!-- value에 context로 들어온 article에서 title데이터를 variable로 할당하여 출력-->
        <label for="content">CONTENT: </label>
        <textarea name="content" cols="30" rows="5">{{ article.content }}</textarea><br> <!-- context로 들어온 article에서 content데이터를 variable로 할당하여 출력-->
        <input type="submit"> <!-- 제출 시 form action에 지정된 주소로 전송 -->
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">BACK</a> <!-- articles의 urls.py에서 name이 index인 path로 이동 -->
{% endblock content %}
```

## Admin(관리자)

### admin 계정 생성

```python
python manage.py createsuperuser
```

- 이후 prompt에 뜨는 username과 password를 입력해 관리자 계정 생성
    - email은 선택사항이기에 pass 가능

### admin에 클래스 등록

> admin site에서 데이터 CRUD(조회, 삭제, 수정, 입력)를 하기 위함
> 

```python
# articles/admin.py

from django.contrib import admin
from .models import Article # 생성한 클래스 import

# Register your models here.
admin.site.register(Article) # admin site에 생성한 클래스 등록
```