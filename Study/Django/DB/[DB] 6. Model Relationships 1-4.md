# Authenticated & View decarator

## 인증된 사용자에게만 댓글 작성/삭제 허용하기

### 댓글 생성 시 인증된 사용자 확인

> is_authenticated로 인증된 사용자 확인
> 
- 인증된 사용자의 경우
    - 댓글 작성 후 해당 페이지로 이동
- 인증되지 않았을 경우
    - 로그인 페이지로 이동

```python
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:login')
```

### 인증되지 않은 사용자에게 안내해주기

> 인증되지 않은 사용자에게 href 제공해주기
> 

```html
{% if request.user.is_authenticated %}
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
{% else %}
    <a href="{% url 'accounts:login' %}">댓글을 작성하려면 로그인 하세요.</a>
{% endif %}
```

### 댓글 삭제 시 인증된 사용자 확인

> is_authenticated로 인증된 사용자인지 확인
> 
- 인증된 사용자의 경우
    - 작성자와 요청한 사용자가 같은지 확인 후 댓글 삭제
- 인증되지 않은 사용자의 경우
    - 변경 없이 해당 페이지로 이동

```python
def comments_delete(request, article_pk, comment_pk):
    if request.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```

### View decorator로 특정 요청만 받기

> 댓글 생성과 삭제 모두 POST 요청만 받기
> 

```python
@require_POST
def comments_create(request, pk):
    ...

@require_POST
def comments_delete(request, article_pk, comment_pk):
    ...
```