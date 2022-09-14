# Django_Login

# Login

> 로그인은 Session을 Create하는 과정
>
- 인증을 직접 구현하기는 너무 어렵기에 Django에서는 기본적으로 built-in forms을 제공 
- 로그인 후 쿠키에 생성된 session id로 로그인이 됐다는 것을 확인 가능

## AuthenticationForm

> 로그인을 위한 built-in form
> 
- 로그인 하고자 하는 사용자 정보를 입력 받음
- 기본적으로 username과 apssword를 받아 데이터가 유효한지 검증
- request를 첫 번째 인자로 취함

## Login 구현

### base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <div class='container'>
        <h3>{{ user }}</h3>
        <a href="{% url 'accounts:login' %}">Login</a>
        <hr>
        {% block content %}
        {% endblock content %}
    </div>  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```

### urls.py

```python
# account/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
	path('login/', views.login, name='login'),
]
```

### views.py

```python
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, request.POST) # 첫번째 인자 : request, 두번째 인자 : data
		if form.is_valid():
			auth_login(request, form.get_user()) # 첫번째 인자 : request, 두번째 인자 : 유저 정보
			return redirect('articles:index')
	else:
		form = AuthenticationForm()
	context = {
		'form' : form,
	}
	return render(request, 'accounts/login.html', context)
```

### login.html

```html
{% comment %}templates/accounts/logint.html{% endcomment %}

{% extends 'base.html' %}

{% block content %}
    <h1>LOGIN</h1>
    <form action="{% url 'accounts:login' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock content %}
```

### view에서 사용한 login()함수

> login(request, user, backend=None)
> 
- 인증된 사용자를 로그인 시키는 로직으로 view 함수에서 사용됨
- 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 사용
- HttpRequest객체(`request`)와 User객체(`form.get_user`)가 필요

### 현재 로그인 되어있는 유저 정보 출력

> settings.py의 `context porocessors` 의 `django.contrib.auth.context_processors.auth`로 인해 base.html에서 `{{ user }}`로 간단하게 유저 정보를 출력할 수 있음
> 
- 그렇기 때문에 view에서 context로 데이터를 전달할 때 key를 user로 설정하여 전달해준다면 
두 정보가 겹칠 수 있기 때문에 key를 user로 설정하는 것을 피해야 함
- context processors
    - 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
    - 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함
    - django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해둔 것
- 로그인 되어있는 경우 : 유저의 ID 출력
- 로그인 되어있지 않은 경우 : AnonymousUser로 출력