# Django_Image Update
> 이미지는 바이너리 데이터이기 때문에 텍스트처럼 일부만 수정하는 것은 불가능
> 
- 새로운 사진으로 대체하는 방식

## UPDATE

### update.html

> enctype 속성값을 추가
> 

```html
<!-- articles/update.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
```

### views.py

> request.FILES 추가
> 

```python
@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            ...
```

## 사용자 지정 업로드 경로와 파일 이름 설정하기

### 1. 문자열 값이나 경로 지정 방법

> upload_to 인자에 새로운 이미지 저장 경로를 추가 후 migration
> 

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    ...
    # image = models.ImageField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    ...
```

```bash
python manage.py makemigrations
python manage.py migrate
```

- 이미지 업로드 후 media에 `images`라는 폴더가 생성된 것을 확인 가능

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    ...
    # image = models.ImageField(blank=True)
    # image = models.ImageField(blank=True, upload_to='images/')
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    ...
```

- 단순 문자열 뿐만 아니라 파이썬 time 모듈의 strftime()형식도 포함될 수 있으며 이는 파일 업로드 날짜/시간으로 대체 됨

### 2. 함수 호출 방법

> upload_to는 독특하게 함수처럼 호출이 가능하며 해당 함수가 호출되면서 반드시 2개의 인자를 받음
> 

```python
# 앱/models.py

from django.db import models
from django.conf import settings

def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'

# Create your models here.
class Article(models.Model):
    ...
    # image = models.ImageField(blank=True)
    # image = models.ImageField(blank=True, upload_to='images/')
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    image = models.ImageField(blank=True, upload_to=articles_image_path)
    ...
```

- 2개의 인자
    1. instance 
        - FileField가 정의된 모델의 인스턴스
        - 대부분 이 객체는 아직 데이터베이스에 저장되기 전이므로 아직 PK값이 없을 수 있으니 주의
    2. filename
        - 기존 파일 이름
- migration 과정 진행 후 이미지 업로드 결과 확인하기

## Image Resizing

> 실제 원본 이미지를 서버에 그대로 로드 하는 것은 여러 이유로 부담이 큼
> 
- HTML <img>태그에서 직접 사이즈를 조정할 수 있지만 실제 저장된 사이즈가 변환이 되는 것이 아님
- 따라서 업로드 될 때 이미지 자체를 resize가 필요

### django-imagekit 모듈

> 이미지 처리를 위한  Django 앱
> 
- 썸네일, 해상도, 사이즈, 색깔 등을 조정할 수 있음
- 설치
    
    ```python
    pip install django-imagekit
    pip freeze > requirements.txt
    ```
    
- 등록
    
    ```python
    INSTALLED_APPS = [
        'articles',
        'accounts',
        'django_extensions',
        'imagekit',
        ...
    ]
    ```
    

## 썸네일 생성

### 1. 원본 이미지 저장 X

> request로 들어온 원본 이미지를 resize한 후 작업 후의 이미지만 `upload_to`로 설정한 경로에 저장
> 

```python
# 앱/models.py

from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'

# Create your models here.
class Article(models.Model):
    ...
    # image = models.ImageField(blank=True)
    # image = models.ImageField(blank=True, upload_to='images/')
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    # image = models.ImageField(blank=True, upload_to=articles_image_path)
    image = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 80},
    )
    ...
```

```python
python manage.py makemigrations
python manage.py migrate
```

- precessors : 적용할 함수와 크기
- format : 저장할 확장자
- options : 장고 공식 문서에서 제공하는 키 사용

### 2. 원본 이미지 저장 O

> request.FILES로 받아온 이미지를 원본을 저장해뒀다가 필요 시에 리사이징하여 cached 폴더에 저장한 후 해당 이미지를 출력
> 

```python
# 앱/models.py

from django.db import models
from django.conf import settings
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField

def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'

# Create your models here.
class Article(models.Model):
    ...
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality': 80},
    )
    ...
```

```html
{% extends 'base.html' %}

{% block content %}
  {% if article.image %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}">
    <img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">
  {% endif %}
```

- image : 원본 파일을 저장
- image_thumbnail : 필요 시에 이 변수를 통해 리사이징 된 이미지 출력
    - source : 리사이징에 사용할 이미지
    - precessors : 적용할 함수와 크기
    - format : 저장할 확장자
    - options : 장고 공식 문서에서 제공하는 키 사용