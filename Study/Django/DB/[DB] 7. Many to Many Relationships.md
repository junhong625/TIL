# Many to many Relationships

> 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
> 
- 서로 1:N의 관계를 가짐

### 데이터 모델링

> 물리적인 데이터베이스 모델로 만들어 고객의 요구에 따라 특정 정보 시스템의 데이터베이스에 반영하는 작업
> 

### target model

> 관계 필드를 가지지 않은 모델
> 
- N:1에서 1에 해당

### source model

> 관계 필드를 가진 모델
> 
- N:1에서 N에 해당

## N:1 모델 관계의 한계

> 의사와 환자 간 예약 시스템을 구현
> 
- N:1 모델 관계를 활용하여 한 명의 의사에게 여러 환자가 예약할 수 있다고 모델 관계를 설정
- 하지만 이렇게 작성할 경우 한 환자가 여러 명의 의사에게 모두 방문하기 위해선 동시에 예약이 되지 않아 따로따로 예약을 해야 함(같은 이름의 환자 객체 추가 생성 필요)

### 해결 방법 (1) 중개 모델 생성

> 외래 키만 가지고 있는 모델
> 
- 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성
- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐
- 중개 모델을 사용 시 추가적인 객체 생성할 필요 없이 예약이 가능해짐
- 역참조를 통해 의사, 환자 입장에서 데이터 조회 가능
    - ex ) patient.reservation_set.all(), doctor.reservation_set.all()

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

### 해결 방법 (2) ManyToManyField 생성

> 본인이 생각하는 논리적인 위치에 필드 작성
> 
- 새로운 모델을 생성할 필요 없이 필드를 작성한 클래스와 `To`를 통해 지정한 클래스의 이름들을 합친 이름으로 중개 테이블을 자동 생성
- 중개 모델과 마찬가지로 추가적인 객체 생성 없이 예약이 가능해짐
- 환자와 의사가 주체가 되어 예약이 가능해져 좀 더 현실적인 예약이 가능함
- 서로 종속적인 관계가 아니기에 양쪽에서 자유롭게 예약이 가능
    - 필드가 존재한 테이블에서는 참조, 필드가 존재하지 않는 테이블에서는 역참조(`_set`)로 예약 가능
- 중개 모델과 가장 큰 차이점
    - 중개 모델과 다르게 `ManyToManyField`는 예약한 환자 데이터만 바로 조회가 가능하다.

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

## ManyToManyField

- ManyToManyField(to, **options)
- M:N 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자가 필요
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 생성 가능
- `db_table` arguments를 사용하여 중개 테이블의 이름을 변경 가능

## Arguments

### 1. related_name

> target model이 source model을 참조할 때 사용할 manager name
> 
- ForeignKey()의 related_name과 동일

### 2. through

> 중개 모델을 직접 작성해야 하는 경우에 사용하는 옵션
> 
- `ManyToManyField` 사용 시 자동으로 생성되는 테이블을 원하는 모델로 직접 지정
- 중개 테이블에 추가 데이터를 사용해 M:N 관계와 연결하려는 경우
- 문자열로 작성
- 기존과 다르게 추가 시 through_defaults에 추가 입력이 필요
    - ex) patient2.doctors.add(doctor1, through_defaults={’symptom’: ‘ flu’})

```
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

### 3. symmetrical

> ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
> 
- 기본 값 : True
- True일 경우
    - _set 매니저를 추가하지 않음
    - source model의 인스턴스가 target model의 인스턴스를 참조하면 자동으로 target model의 인스턴스가 source model 인스턴스를 참조하도록 함
    

## methods

### 1. add()

> 지정된 객체를 관련 객체 집합에 추가
> 
- 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

### 2. remove()

> 관련 객체 집합에서 지정된 모델 객체를 제거
> 
- 내부적으로 QeurySet.delete()를 사용하여 관계가 삭제
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

## LIKE

> ManyToManyField를 이용하여 좋아요 기능 구현
> 

### models.py

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

- 이후 migration을 진행하면 오류가 발생
    - `like_users` 필드 생성 시 자동으로 역참조를 위한 `article_set` 매니저가 생성됨
    - 하지만 이전 1:N 관계(Article에서 user를 ForeignKey로 사용)에서 이미 똑같은 이름의 매니저를 사용 중
    - 따라서 두 매니저의 이름이 같지 않게 하기 위해 둘 중에 하나의 이름을 related_name으로 변경 필요
    - 통상적으로 M:N 관계의 매니저의 이름을 변경

### urls.py

> LIKE에 대한 url과 함수 경로 설정
> 

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    ...,
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

### views.py

> LIKE 함수 생성
> 

```python
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # if request.user in article.like_users.all():
    if Article.objects.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```

- 게시물에 ‘좋아요’를 한 유저 목록에 현재 유저가 있을 경우
    - ‘좋아요’ 취소
- 게시물에 ‘좋아요’를 한 유저 목록에 현재 유저가 없을 경우
    - ‘좋아요’
- `if request.user in article.like_users.all():`를 통해 검색할 경우 데이터가 커질 경우 느려질 가능성이 있음
    - 따라서 `if Article.objects.filter(pk=request.user.pk).exists():` 를 통해 조건을 설정하는 것이 좀 더 효율적일 수 있음

### index.html

> 좋아요 버튼 추가
> 

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p><b>작성자 : {{ article.user }}</b></p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <div>
      <form action="{% url 'articles:likes' article.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <input type="submit" value="좋아요 취소">
        {% else %}
          <input type="submit" value="좋아요">
        {% endif %}
      </form>
    </div>
    <a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
    <hr>
  {% endfor %}
{% endblock content %}
```

- views.py와 마찬가지로 게시물에 ‘좋아요’를 한 유저 목록에 현재 유저가 있을 경우
    - ‘좋아요’ 취소
- 게시물에 ‘좋아요’를 한 유저 목록에 현재 유저가 없을 경우
    - ‘좋아요’

### authentication

> 코드를 작성 후 decorator와 조건들 설정
> 

```python
# views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        # if request.user in article.like_users.all():
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```