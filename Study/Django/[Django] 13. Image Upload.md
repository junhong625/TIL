# Django_Image Upload

> Django IamgeField를 사용해 사용자가 업로드한 정적 파일 관리
> 

### ImageField()

> 이미지 업로드에 사용하는 모델 필드
> 
- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능 
+ 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
- ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성, max_length 인자를 사용하여 최대 길이를 변경 가능
    - ImageField임에도 문자열이 들어가는 이유는 파일의 경로가 저장될 것이기 때문!

### FileField()

- FileField(upload_to=’’, storage=None, max_length=100, **options)
- 파일 업로드에 사용하는 모델 필드
- 2개의 선택 인자를 가지고 있음
    1. upload_to
    2. storage

### FileField / ImageField를 사용하기 위한 단계

1. settings.py에 `MEDIA_ROOT`, `MEDIA_URL` 설정
2. `upload_to` 속성을 정의하여 업로드 된 파일에 사용할 `MEDIA_ROOT`의 하위 경로를 지정(선택 사항)

### MEDIA_ROOT

> 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로
> 
- Default : ‘’
- Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
    - 데이터베이스에 저장되는 것은 ‘파일 경로’
- `MEDIA_ROOT`는 `STATIC_ROOT`와 반드시 다른 경로로 지정해야 함

```python
# settings.py

MEDIA_ROOT = BASE_DIR / 'media'
```

### MEDIA_URL

> `MEDIA_ROOT`에서 제공되는 미디어 파일을 처리하는 URL
> 
- Default : ‘’
- 업로드 된 파일의 주소(URL)를 만들어 주는 역할
    - 웹 서버 사용자가 사용하는 public URL
- 비어 있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야 함
- `MEDIA_URL`은 `STATIC_URL`과 반드시 다른 경로로 지정해야 함

```python
# settings.py

MEDIA_URL = '/media/'
```

### 개발 단계에서 사용자가 업로드한 미디어 파일 제공

```python
# 프로젝트/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- 사용자로부터 업로드 된 파일이 프로젝트에 업로드 되고 나서, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요
    - 업로드 된 파일의 URL == `settings.MEDIA_URL`
    - 위 URL을 통해 참조하는 파일의 실제 위치 == `settings.MEDIA_ROOT`
    

## CREATE

### ImageField 작성

```python
class Article(models.Model):
	...
	image = models.ImageField(blank=True)
	...
```

- 기존 컬럼 사이에 작성해도 추가되는 것이기에 실제 테이블에선 제일 우측(뒤)에 추가
- 필드 option인 blank와 null의 차이
    - blank
        - Default : False
        - True인 경우 필드를 비워 둘 수 있음
            - 이럴 경우 DB에는 ‘’(빈 문자열)이 저장됨
        - 유효성 검사에서 사용 됨(is_valid)
            - “Validation-related”
            - 필드에 `blank=True`가 있으면 form 유효성 검사에서 빈 값을 허용
    - null
        - Default : False
        - True인 경우 Django는 빈 값을 DB에 NULL로 저장
            - “Database-related”
        - CharField, TextField와 같은 문자열 기반 필드에는 null 옵션 사용을 피해야 함
            - 문자열 기반 필드에 `빈 문자열`과 `NULL` 2가지 모두 가능하게 하지 않도록 하기 위함
    - 즉, 문자열 기반인 image필드에는 빈 문자열이 저장되는 `blank`를 사용

### Migrations 진행

> ImageField를 사용하려면 반드시 Pillow 라이브러리가 필요
> 
- Pillow 설치 없이는 makemigrations 실행 불가
    - Pillow
        - 광범위한 파일 형식 지원, 효율적이고 강력한 이미지 처리 기능을 제공하는 라이브러리
        - 이미지 처리 도구를 위한 견고한 기반을 제공

```python
pip install Pillow

python manage.py makemigrations
python manage.py migrate

pip freeze > requirements.txt
```

## 이미지 업로드

### Articles에서 변경 사항 확인

- forms.py에서 field에 image를 추가해준다면 게시물 생성 시 파일 선택하는 버튼이 생성 된 것을 확인 가능
- 하지만 해당 버튼으로 파일을 업로드 하더라도 이미지가 업로드 되지 않음
- 파일 또는 이미지 업로드 시에는 form태그에 `enctype` 속성을 변경해야 함

```python
<form action="" method="POST" enctype="multipart/form-data">
```

- `multipart/form-data`
    - 파일/이미지 업로드 시에 반드시 사용해야 함
    - 전송되는 데이터의 형식을 지정
    - `<input type=’file’>`을 사용할 경우 사용

### request.FILES

> 파일 및 이미지는 request의 POST 속성 값으로 넘어가지 않고 FILES 속성 값에 담겨 넘어감
> 

```python
# 앱/views.py

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
```

- 만약 같은 이름의 파일을 업로드 한다면 Django가 알아서 이름의 끝에 난수를 추가해 줌

## 이미지 출력

> 업로드 된 파일의 상대 URL은 Django가 제공하는 url 속성을 통해 얻을 수 있음
> 

```html
{% extends 'base.html' %}

{% block content %}
  <img src="{{ article.image.url }}" alt="{{ article.image }}">
```

- `article.image.url` - 업로드 파일의 경로
- `article.image` - 업로드 파일의 이름