# # PJT 05

## 5번째 관통 pjt를 하며 느낀 점
> 매번 배움의 고통과 즐거움을 함께 떠넘겨주는 알고리즘을 해결하는 것도 정말 재밌지만 즉각적으로 원하는 부분을 반영하고 알고리즘 보다는 좀 더 쉬운 접근 방법으로 문제를 해결할 수 있는 BACKEND&CSS는 정말 저의 적성에 잘 맞는 파트라고 생각됩니다. 알고리즘이 싫은건 절대 아니지만 장고 너무 재밌습니다.......

## Model

- 요구 사항 : 
  - 클래스의 이름 : Movie
  - 명세서에 나와있는 설계도대로 구성

- 결과 : 
![](https://user-images.githubusercontent.com/83000975/194508426-bf58dbf0-95cf-4e72-a46d-d63b69a25b2e.png)

- 문제 접근 방법 및 코드 설명
    
```py
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.BigIntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
```

- 이 문제에서 어려웠던 점
> 오랜만에 각 컬럼에 알맞은 타입의 필드를 설정하려다보니 어떠한 필드가 있는지 잘 기억이 나지 않았었습니다.
- 내가 생각하는 이 문제의 포인트
> CTRL + SPACE 를 이용하여 models.에서 사용가능한 메서드를 보고 의미를 추측할 수 있는 역량
  
---

## URL
- 요구사항 : 
    - 명세서에 나와있는 패턴과 역할에 맞춰 urlpatters 작성

- 문제 접근 방법 및 코드 설명
    
```py
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

- 문제에서 어려웠던 점
> 매일 실습하고 배웠던 내용이라 어렵지 않게 작성할 수 있었습니다.
- 내가 생각하는 문제의 포인트
> 각 url들이 views의 어떠한 함수를 불러오고 어떠한 주소로 이동하게 될 것인지에 대해 인지하며 작성하는 것

---

## View

- 요구사항
    - 명세서에 나와있는 각 함수명과 역할에 맞춰 작성

  - 문제 접근 방법 및 코드 설명

    ```py
    from django.shortcuts import render, redirect
    from django.views.decorators.http import require_http_methods, require_POST, require_safe
    from .forms import MovieForm
    from .models import Movie

    # Create your views here.
    @require_safe
    def index(request):
        movies = Movie.objects.all()
        context = {
            'movies' : movies,
        }
        return render(request, 'movies/index.html', context)

    @require_http_methods(['GET', 'POST'])
    def create(request):
        if request.method == 'POST':
            form = MovieForm(request.POST)
            if form.is_valid():
                movie = form.save()
                return redirect('movies:index')
        else:
            form = MovieForm()
        context = {
            'form' : form,
        }
        return render(request, 'movies/create.html', context)

    @require_safe
    def detail(request, pk):
        movie = Movie.objects.get(pk=pk)
        context = {
            'movie': movie,
        }
        return render(request, 'movies/detail.html', context)

    @require_http_methods(['GET', 'POST'])
    def update(request, pk):
        movie = Movie.objects.get(pk=pk)
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', pk)
        else:
            form = MovieForm(instance=movie)
        context = {
            'form':form,
            'pk' : pk
        }
        return render(request, 'movies/update.html', context)

    @require_POST
    def delete(request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return redirect('movies:index')
    ```

- 문제에서 어려웠던 점
> 각 기능마다 사용되는 함수에 어떠한 인자가 들어가야하는지 기억하고 있는 것

- 내가 생각하는 이 문제의 포인트
> 각 함수들에 어떤 메서드의 사용이 필요하고 해당 메서드를 불러오기 위해 어떤 라이브러리를 import해야하는지 인지하고 있어야 하며 함수들이 어떻게 작동할 것인지에 대해 머리속으로 그리면서 그에 맞춰 작성하는 것

---

## Admin

- 요구사항
    - 클래스 Movie를 Admin Site에 등록
    - Admin site에서 데이터의 생성, 조회, 수정, 삭제가 가능해야함

- 결과
![](https://user-images.githubusercontent.com/83000975/194509467-9d10c6b9-35ed-4db4-86f5-e070bc5c39ba.png)
![](https://user-images.githubusercontent.com/83000975/194509635-da060b68-00bf-4c17-9d90-b13590ab4f21.png)

- 문제 접근 방법 및 코드 설명

    ```bash
    python manage.py createsuperuser
    ```

    ```py
    from django.contrib import admin
    from .models import Movie

    # Register your models here.
    admin.site.register(Movie)
    ```

- 문제에서 어려웠던 점
> 이번주 학습 시간에 admin에 등록하는 작업을 해봤기에 금방 떠올라 쉽게 할 수 있었습니다.

- 내가 생각하는 이 문제의 포인트
> admin.site의 메서드에서 대해서 알고있거나 공식 문서에서 관련 메서드를 찾아보는 것

---

## Template

### 1. base.html

- 요구사항
    - 다른 템플릿들은 base.html을 상속받아 작성해야 함

- 문제 접근 방법 및 코드 설명

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <style>
            @font-face {
                font-family: 'BinggraeSamanco-Bold';
                src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10@1.0/BinggraeSamanco-Bold.woff') format('woff');
                font-weight: normal;
                font-style: normal;
            }
        * {
            font-family: 'BinggraeSamanco-Bold';
            font-size: 20px
        }
        </style>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    </head>
    <body>
        <div class="navbar bg-warning px-3 d-flex justify-content-center">
            <a class="navbar-brand" href="{% url 'movies:index' %}">
            <img src="https://search.pstatic.net/common?type=f&size=174x174&quality=95&direct=true&src=https%3A%2F%2Fnng-phinf.pstatic.net%2FMjAyMTExMjZfMTQw%2FMDAxNjM3ODg4MDI0NDYx.jQlgk0wgOHenvZXCDCbGz1k3Mff8MvJfAwGR5kxlXJMg.OZCmgnGglrk9R0-xgNW-FyiocBfUmoFO8IzHhYEKfCIg.PNG%2F9%25EA%25B5%25AC%25EC%258A%25A4.png" class="img-fluid rounded-4 border" style="height:50px; width:50px" alt="">
            </a>
            <h1 class="mx-5">영화 평론가 [No-Duck-Goose]</h1>
        </div>
        <div class="m-auto w-50">
        {% block content %}
        
        {% endblock content %}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
    </body>
    </html>
    ```

- 문제에서 어려웠던 점
> base.html을 작성하는 방법은 잊지 않고 있었기에 쉽게 작성할 수 있었습니다.

- 내가 생각하는 이 문제의 포인트
> 적절한 위치에 `block`과 `endblock`을 설정하고 해당 `block`을 `div`감싸 원하는 방식으로 디자인 하는 것

### 2. index.html

- 요구사항
    - 전체 영화 목록 조회 페이지
    - 데이터 베이스에 존재하는 모든 영화의 목록 표시
      - 영화 제목 및 평점도 표시
    - 제목을클릭 시 해당 영화의 상세 조회 페이지로 이동

- 결과  
  ![](https://user-images.githubusercontent.com/83000975/194510345-90b322df-7dce-45fd-9f3c-df1e2b674d58.png)

- 문제 접근 방법 및 코드 설명

    ```html
    {% extends 'base.html' %}

    {% block content %}
        <div>
            <div class="d-flex justify-content-end my-3">
                <a class="btn btn-warning" href="{% url 'movies:create' %}">생성</a>
            </div>
            <div class="px-5 mx-5">
                <hr>
                {% for movie in movies %}
                <div class="d-flex border rounded-4 p-3">
                    <div class="d-flex flex-column w-100">
                        <div class="d-flex">
                            <p class="col-2 border-end text-center">제목</p><b><a class="px-5 text-decoration-none text-dark" href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></b>
                        </div>
                        <div class="d-flex">
                            <p class="col-2 border-end text-center">장르</p><p class="px-5">{{ movie.genre }}</p>
                        </div>
                        <div class="d-flex">
                            <p class="col-2 border-end text-center">평점</p><p class="px-5">{{ movie.score }}</p>
                        </div>
                    </div>
                    <div><img src="{{ movie.poster_url }}" alt="{{ movie.title }} 포스터" style="width:150px; height:150px;" class="me-5 rounded-4"></div>
                </div>
                <hr>
                {% endfor %}
            </div>
        </div>
    {% endblock content %}
    ```

- 문제에서 어려웠던 점
> 백엔드와 HTML은 그래도 어렴풋이 기억나 검색 없이 충분히 작성할 수 있었지만 CSS는 전혀 떠오르지 않아 폰트를 바꾸는데 검색과 많은 노력이 필요했습니다.....

- 내가 생각하는 이 문제의 포인트
> `div`와 `d-flex`를 이용하여 구상하는 이미지의 틀을 잡고 구현해나가기

### 3. detail.html

- 요구사항
    - 영화 상세 정보 페이지
    - 특정 영화의 상세 정보 표시
    - 해당 영화의 수정 및 삭제 버튼 표시
    - 전체 영화 목록 조회 페이지로 이동하는 링크 표시

- 결과  
    ![](https://user-images.githubusercontent.com/83000975/194510716-adebe9f9-01bc-452c-8a84-9ed7161407e3.png)

- 문제 접근 방법 및 코드 설명

    ```html
    {% extends 'base.html' %}

    {% block content %}
        <div class="card m-auto my-5 d-flex flex-column align-items-center w-50 rounded-5">
            <img src="{{ movie.poster_url }}" class="card-img-top rounded-5" alt="{{ movie.title }} 포스터">
            <div class="card-body">
            <h5 class="card-title text-center">{{ movie.title }}</h5>
            </div>
            <div class="d-flex flex-column w-100">
                <div class="d-flex">
                    <p class="col-4 border-end text-center">관객</p><p class="px-4">{{ movie.audience }} 명</p>
                </div>
                <div class="d-flex">
                    <p class="col-4 border-end text-center">장르</p><p class="px-4">{{ movie.genre }}</p>
                </div>
                <div class="d-flex">
                    <p class="col-4 border-end text-center">평점</p><p class="px-4">{{ movie.score }}</p>
                </div>
                <div class="d-flex">
                    <p class="col-4 border-end text-center">설명</p><p class="px-4">{{ movie.description }}</p>
                </div>
            </div>
        </div>
        <div class='my-3 d-flex justify-content-end'>
            <a class="btn btn-warning" href="{% url 'movies:update' movie.pk%}">수정</a>
            <form action="{% url 'movies:delete' movie.pk %}" method="POST">
                {% csrf_token %}
                <input type="submit" value="삭제" class="btn btn-warning mx-3">
            </form>
            <a class="btn btn-warning" href="{% url 'movies:index' %}">뒤로</a>
        </div>
    {% endblock content %}
    ```

- 문제에서 어려웠던 점
> 원하는 기능을 구현하고 디자인을 만드는 것은 어렵지 않았지만 원하는 위치에 원하는 기능을 배치시키는 것이 조금 어렵다고 느껴졌습니다.

- 내가 생각하는 이 문제의 포인트
> `card`를 `m-auto`를 통해 간단하게 중앙에 배치하는 것 
> POST 사용 시 필수 csrf_token을 넣어줘야 하는 것

### 4. create.html

- 요구사항
    - 영화 생성 페이지
    - form 태그 사용
    - 제출 시 create로 전송
    - 전체 영화 목록 조회 페이지로 이동하는 링크 표시

- 결과
  ![](https://user-images.githubusercontent.com/83000975/194511386-5cf4344f-6df4-4fbf-b504-f36d84ae61aa.png)
  ![](https://user-images.githubusercontent.com/83000975/194511475-1349c19d-7e95-4f2a-8555-c8cbf65ac85e.png)

- 문제 접근 방법 및 코드 설명

    ```html
    {% extends 'base.html' %}

    {% block content %}
    <form class="my-3" action="{% url 'movies:create' %}" method="POST">
        {% csrf_token %}
        {% for f in form %}
            <label class="col-4 form-label mt-3">
                <b>{{ f.label }}</b>
            </label>
            {{ f }}
        {% endfor %}
        <div class='my-3 d-flex justify-content-end'>
            <input class="btn btn-warning mx-3" type="submit" value="완료">
            <a class="btn btn-warning" href="{% url 'movies:index' %}">뒤로</a>
        </div>
    </form>
    {% endblock content %}
    ```

- 문제에서 어려웠던 점
> `for`태그를 이용하기 위해서는 각 `field`의 `label`과 입력하는 칸을 구분하여 표현하기가 어려웠습니다.

- 내가 생각하는 이 문제의 포인트
> `label`과 입력하는 칸을 구분하기

### 5.  update.html

- 요구사항
    - 영화 수정 페이지
    - form 태그 사용
    - 기존의 데이터 출력
    - reset 버튼을 통해 사용자의 모든 입력 초기 값으로 재설정
    - 제출 시 update url로 전송
    - 영화 상세 정보페이지로 이동하는 링크 표시

- 결과  
  ![](https://user-images.githubusercontent.com/83000975/194511909-df43fdf2-f50e-4acd-ab3c-1f6a54d6730d.png)
  ![](https://user-images.githubusercontent.com/83000975/194511964-6c1d73b1-00a4-44b4-bfd0-76b3849d681f.png)

- 문제 접근 방법 및 코드 설명

    ```html
    {% extends 'base.html' %}

    {% block content %}
    <form class="my-3" action="{% url 'movies:update' pk %}" method="POST">
        {% csrf_token %}
        {% for f in form %}
            <label class="col-4 form-label mt-3">
                <b>{{ f.label }}</b>
            </label>
            {{ f }}
        {% endfor %}
        <div class='my-3 d-flex justify-content-end'>
            <input class="btn btn-warning mx-3" type="submit" value="완료">
            <a class="btn btn-warning" href="{% url 'movies:index' %}">뒤로</a>
        </div>
    </form>
    {% endblock content %}
    ```

- 문제에서 어려웠던 점
> 부트스트랩의 `form-control`을 이용하면 간단하게 원하는 디자인을 구현할 수 있었으나 model에서 적용하는 부분에 있어 어려움을 겪어 html에서 한참을 시도했었습니다.

- 내가 생각하는 이 문제의 포인트
> `for`태그를 이용하여 이전에 PJT를 진행했을 때보다 더욱 간결하게 작성

---
# 후기
- 매일 새롭고 어려운 장고를 통해 스트레스를 받고 있었는데 해당 개념에 대해서만 잘 알고 있다면 쉽게 해결할 수 있는 장고를 진행하며 힐링을 할 수 있었습니다.
- 발생한 오류들을 직접 해결해 나갈 때마다 장고가 어떤 구조로 구성되어 있고 어떻게 작동을 하는지 깨달을 수 있었고 이러한 과정들을 통해 장고에 더욱 애정을 가지게 되었습니다.  
- 아직 배워야할 부분들이 많겠지만 앞으로도 현재와 비슷하게 진행이 된다면 계속 장고에 애정을 가지고 열심히 할 수 있을 것 같습니다.
- 알고리즘도 좋지만 장고가 최고다!!!!!!!!!