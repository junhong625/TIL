# N : 1 (Comment - Article)

> Comment 모델과 Article 모델 간 관계 설정
> 
- 0개 이상의 댓글은 1개의 게시글에 작성될 수 있음
- comment의 article_id는 Article의 id를 참조하는 Foreign Key

## Foreign Key

> 외래 키, 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
> 
- 참조하는 테이블에서 1개의 키에 해당, 이는 참조되는 측 테이블의 기본 키(Primary Key)를 가리킴
- 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응
    - 따라서 참조되는 테이블에 나타나지 않는 값은 포함 X
- 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조 가능

### Foreign Key 특징

- 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
    - 참조 무결성
        - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
        - 외래 키가 선언된 테이블의 외래 키 속성의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함
- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

## Django Relationship fields 종류

### 1. OneToOneField()

- A one-to-one relationship

### 2. ForeignKey(to, on_delete, **options)

- A many-to-one relationship
- Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
- 2개의 필수 위치 인자가 필요
    - to : 참조하는 model class
    - on_delete : 외래 키가 참조하는 객체가 사라졌을 때 어떻게 처리할 지를 정의
        - 데이터 무결성을 위해서 매우 중요한 설정
            - 데이터 무결성
                - 데이터의 정확성과 일관성을 유지하고 보증하는 것
                - 데이터베이스나 RDBMS의 중요한 기능
                - 무결성 제한의 유형
                    1. 개체 무결성 (Entity integrity)
                    2. 참조 무결성 (referential integrity)
                    3. 범위 무결성 (Domain integrity)
        - 옵션 값:
            - CASCADE : 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제
            - PROTECT, SET_NULL, SET_DEFAULT 등 여러 옵션 값들이 존재
    - **options(선택 인자)
        - related_name
            
            ```python
            article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
            ```
            
            - 역참조 시 사용하는 매니저 이름(related manager)을 변경할 수 있음
            - 작성 후 migration 과정 필요
            - 선택 옵션이지만 상황에 따라 반드시 작성해야 하는 경우가 발생하기도 함
            - 변경하면 기존의 article.comment_set은 사용 불가 즉, 할당한 이름(comments)으로 대체 됨

### 3. ManyToManyField()

- A many-to-many relationship

# Comment 모델

> 댓글 기능 만들기
> 

## Comment 모델 정의

- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장

```python
## Articles/models.py

from django.db import models

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

### Migration 진행

> model이 변경되었으니 migration 진행
> 

```python
python manage.py makemigrations
python manage.py makemigrate
```

- migrate 후 Comment 모델 클래스로 인해 생성된 테이블 확인(앱_모델)
- ForeignKey 모델 필드로 인해 작성된 컬럼의 이름이 ForeignKey 클래스에서 인자로 설정한 Article로 인해 article_id로 생성된 것을 확인

### shell_plus로 댓글 생성

- shell_plus 실행

```python
python manage.py shell_plus # shell_plus 실행
```

- 댓글 생성

```python
comment = Comment()
comment.content = 'first comment'
comment.save()
# 게시글이 없기에 오류가 발생
```

- 게시글 생성

```python
article = Article.objects.create(title='title', content='content') # 게시물 생성
comment.article = article # 객체 자체를 미리 생성한 댓글의 article에 할당. 즉, 외래 키
comment.save()

comment = Comment(content='second comment', article=article) # 생성된 게시물에 댓글 남기기
comment.save()
```

- 댓글이 외래키를 가지고 있기에 아래와 같이 댓글에서 게시글 참조 가능

```python
comment.article.pk
comment.article.title
comment.article.content
```

> 그렇다면 게시글(1)에서 댓글(N)은 어떻게 참조하지?? → **역참조**를 활용
> 

## 역참조

> 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
> 
- 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
- N : 1관계에서 1이 N을 참조하는 것

### Related manager

> N : 1혹은 M : N 관계에서 사용 가능한 문맥(context)
> 
- Django는 모델 간 N : 1 혹은 M : N 관계가 설정되면 역참조할 때에 사용할 수 있는 manager를 생성
    - 우리가 이전에 모델 생성 시 `objects`라는 매니저를 통해 queryset api를 사용했던 것처럼 `related manager`를 통해 queryset api를 사용할 수 있게 됨
- `[1에 해당하는 모델].[N에 해당하는 모델]_set`
    
    ```python
    article.comment_set.method()
    ```
    
- Article 모델이 comment 모델을 역참조할 때 사용하는 매니저
- `article.comment` 형식으로는 댓글 객체를 참조 할 수 없음
    - 실제로 Article 클래스에는 Comment와 어떠한 관계도 작성되어 있지 않기 때문
- 대신 Django가 역참조 할 수 있는 `comment_set manager`를 자동으로 생성해 `article.comment_set` 형태로 댓글 객체를 참조할 수 있음
    - **N:1관계에서 생성되는 related manager는 역참조할 `모델명_set` 이름 규칙으로 생성**
- 예시)

```python
article = Article.objects.get(pk=1)  # 첫번째 게시물 인스턴스 생성
comments = article.comment_set.all() # related manager를 활용해 역참조하여 해당 게시물의 댓글 모두 가져오기
for comment in comments:             # 게시물의 모든 댓글 출력   
    print(comment.content)
```

### comment도 admin site에서 관리하기

> 새로 작성한 comment admin site에
> 

```python
# articles/admin.py

from .models import Comment

...
admin.site.register(Comment)
```

## Comment 구현(CREATE)

### 1. Form 생성

> 사용자로부터 댓글 데이터를 입력 받기 위해 ModelForm을 활용해 CommentForm 작성
> 

```python
# articles/forms.py

from django import forms
from .model import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
```

### 2. View 작성

> detail 함수의 context에 CommentForm 추가
> 

```python
# articles/views.py
from .forms import CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

### 3. html 수정

> detail 페이지에서 CommentForm 출력
> 

```html
<!-- articles/templates/detail.html-->
...
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
  {% csrf_token %}     <!--post 사용 시 필수 토큰-->
  {{ comment_form }}
  <input type="submit">
</form>
...
```

- comment가 정상적으로 출력되나 내가 댓글을 달기 위해 들어온 게시물에 댓글을 남기는 것이 아닌 게시물을 선택하여 댓글을 달 수 있도록 설정되어 있음
- 이와 같이 출력 되는 이유는 Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요하기 때문에 출력 되고 있는 것
- 따라서 외래 키 필드는 사용자의 입력이 아닌 view 함수 내에서 받아 별도로 처리되어 저장하도록 한다면 이런 상황을 막을 수 있음
    - CommentForm에서 `fields='__all__'` 로 설정하는 것이 아닌 `exclude=(’article’,)`로 설정하여 article을 출력에서 제외
    
    ```python
    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            exclude = ('article',)
    ```
    
- 그렇다면 article에 필요한 객체(pk번호)는 어떻게 입력 받을 것인가? → 5.views.py 참고

### 4. urls.py

> 댓글을 생성하는 주소 생성
> 

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    ...,
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```

### 5. views.py

> 댓글을 작성하는 함수 생성
> 

```python
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()

    return redirect('article:detail', article.pk)
```

- `save(commit=False)`
    - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 매우 유용
    - 유효성 검사를 한 이후에 save에 `commit=False`라는 함수를 통해 바로 저장하지 않고 인스턴스를 반환하도록 할 수 있다.
    - 이를 comment에 할당하여 comment.article에 미리 불러온 게시물 객체를 할당 시켜주면 comment의 외래 키 필드인 article에 정상적으로 객체를 할당 시켜 줄 수 있다.
    - 이후 save를 하면 깔끔하게 저장 완료

### 6. detail.html

> 원하는 위치에 댓글을 화면에 출력하기
> 

```html
...
<h4>댓글 목록</h4>
<ul>
  {% for comment in comments %}    <!-- for태그를 이용해 출력-->
    <li>{{ comment.content }}</li>
  {% endfor %}
</ul>
...
```

### Comment 구현(DELETE)

> 수정은 JS를 이용할 예정
> 

### 1. urls.py

> 댓글을 삭제하기 위한 주소 추가
> 

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    ...,
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
```

- article의 pk와 comment의 pk를 모두 받아옴

### 2. views.py

> 댓글을 삭제하는 함수 추가
> 

```python
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

- delete함수를 통해 댓글 삭제

### 3. detail.html

> 댓글을 삭제할 수 있는 버튼 추가
> 

```html
<h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      </li>
    {% endfor %}
  </ul>
```

## Comment 추가 사항

### 댓글 개수 출력하기

1. DTL filter - `length` 사용
    
    ```html
    {{ comments|length }}
    {{ article.comment_set.all()|length }}
    ```
    
2. Queryset API - `count()` 사용
    
    ```html
    {{ comments.count }}
    {{ article.comment_set.count }}
    ```
    

### 댓글이 없을 경우

> `for` 태그에 `empty`를 사용
> 

```html
{% for comment in comments %}
  ...
{% empty %}
  <p>댓글이 없습니다.</p>
{% endfor %}
```