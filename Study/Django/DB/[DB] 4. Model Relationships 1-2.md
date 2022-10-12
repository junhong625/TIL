2# N : 1 (Article - User)

> Article(N) 모델과 User(1) 모델 간 관계 설정
> 
- 0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있다.
- Article의 user_id는 User의 id를 참조하는 Foreign Key

## Django에서 User 모델을 참조하는 방법

### 1. setting.AUTH_USER_MODEL

> **models.py의 모델 필드에서 User모델을 참조할 때 사용**
> 
- 반환 값 : ‘accounts.User’(문자열)
- User 모델에 대한 외래 키 또는 M:N 관계를 정의할 때 사용

### 2. get_user_model()

> **models.py가 아닌 다른 모든 곳에서 User 모델을 참조할 때 사용**
> 
- 반환 값 : User Object(객체)
- 현재 활성화(active)된 User 모델을 반환

### 게시글에서 User 참조

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

- 이와 같이 객체가 아닌 문자열을 통해 참조하는 이유
    - 생성 순서로 인해 유저 객체가 생성되지 않았음에도 호출하는 경우 오류가 발생하기에 문자열을 통해 참조

### migration 진행

> model이 변경되었으니 migration 진행
> 
- 위 과정 이후 makemigrations를 진행 시 기존에 존재하던 데이터에 새로운 컬럼인 user_id를 추가하기에 user_id컬럼의  default값을 설정하라는 문구가 뜰 것임
    - 모든 컬럼에는 기본적으로 NOT NULL 제약 조건이 있기 때문에 데이터가 없이는 새로운 컬럼이 추가되지 않음
- django에서 추천하는 기본 설정인 1번을 선택하고 admin 유저의 번호인 1을 입력하면 해결!(user컬럼은 정수 타입)
- 이후 db에 들어가서 테이블을 확인하면 ForeignKey에 해당하는 user_id라는 컬럼이 생성된 것을 확인 가능

## Article에 작성자 속성 부여

- 이전 과정까지 모두 완료하고 게시글 작성을 위해 create 버튼을 누르면 기존에 없던 user를 선택하는 버튼이 나오는 것 확인 가능
- comment를 추가했을 때와 똑같은 상황
- 그렇다면 comment를 작성했을 때와 똑같은 방법으로 해결 가능
    - forms.py에서 user를 제외
    - request 객체에 담겨있는 user데이터를 views.py에서 직접 할당

### 1. forms.py

> form에서 user를 제외시켜주기
> 

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('user',)
```

### 2. views.py

> create함수에서 article.user에 대해 직접 user데이터를 할당 해주기
> 
- commit=False로 저장은 멈추고 인스턴스 반환
- 인스턴스.user에 request에 담겨있는 user를 할당
- article.save()로 저장

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): 
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)
```

## Article Delete

> 작성자가 정보가 추가되었으니 본인이 작성한 게시글만 삭제할 수 있도록 수정
> 

### views.py

> 현재 요청을 보낸 user와 게시물 user가 같은지 판단
> 

```python
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

## Article Update

> 수정도 삭제와 마찬가지로 요청을 보낸 user와 게시물을 작성한 user가 같은지 판단
> 

### views.py

> 요청한 user와 작성한 user가 같은지 판단하여 같지 않을 경우 메인 페이지로 이동
> 

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form' : form
    }
    return render(request, 'articles/update.html', context)
```

### detail.html

> 요청한 user와 작성한 user가 같지 않다면 수정, 삭제 버튼이 뜨지 않도록 수정
> 

```html
{% if request.user == articles.user %}
  <a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
{% endif %}
```

## Article Read

> 게시글을 누가 작성했는지 표시
> 

### index.html, detai.html

> 본인이 원하는 위치에 작성자를 표시
> 

```html
<p><b>작성자 : {{ article.user }}</b></p>
```