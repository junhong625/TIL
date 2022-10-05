# N : 1 (Comment - User)

> Commnet(N) 모델과 User(1) 모델 간 관계 설정
> 
- 0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있다.
- Comment의 User_id는 User의 id를 참조하는 Foreign Key

## Comment에 Foreign Key 생성

### models.py

> user의 id를 가리키는 user_id(Foreign Key) 생성
> 

```python
class Comment(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

### migration 진행

> model이 변경되었으니 migration 진행
> 

```python
python manage.py makemigrations
python manage.py migrate
```

- 위 과정 이후 makemigrations를 진행 시 기존에 존재하던 데이터에 새로운 컬럼인 user_id를 추가하기에 user_id컬럼의  default값을 설정하라는 문구가 뜰 것임
    - 모든 컬럼에는 기본적으로 NOT NULL 제약 조건이 있기 때문에 데이터가 없이는 새로운 컬럼이 추가되지 않음
- django에서 추천하는 기본 설정인 1번을 선택하고 admin 유저의 번호인 1을 입력하면 해결!(user컬럼은 정수 타입)
- 이후 db에 들어가서 comment 테이블을 확인하면 ForeignKey에 해당하는 user_id라는 컬럼이 생성된 것을 확인 가능

## 댓글 작성자 설정

- 위 과정을 마치면 이전에 실행할 때 발생했던 문제처럼 댓글을 작성 시 User를 선택하는 버튼이 뜨는 문제 발생
- 이전과 똑같이 2가지 방법으로 문제 해결
    1. User 선택 버튼 가리기
    2. views.py에서 User에 직접 user 할당해주기

### 1. forms.py

> CommentForm에서 user를 제외하기
> 

```python
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', 'user',)
```

### 2. views.py

> comment.user에 User정보를 할당
> 
- User 정보를 request.user로 전달

```python
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)
```

## 댓글 작성자 출력

### detail.html

> comment.user를 detail 페이지에서 출력
> 

```html
{% for comment in comments %}
  <li>
    {{ comment.user }} - {{ comment.content }}
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="삭제">
    </form>
  </li>
{% empty %}
```

## 댓글 삭제

### views.py

> 요청한 user와 작성한 user가 같을 경우에만 삭제
> 

```python
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
```

### detail.html

> 본인이 작성한 댓글만 삭제할 수 있도록 설정
> 

```
{% if request.user == comment.user %}
                    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
                        {% csrf_token %}
                        <input type="submit" value="삭제">
                    </form>
                {% endif %}
```