# Django_Logout

> Logout은 session을 delete하는 과정
> 
- login과 마찬가지로 django에서 `logout()`함수를 지원

## logout(request)

- HttpRequest 객체를 인자로 받고  반환 값이 없음
- 사용자가 로그인하지 않은 경우 오류를 발생 시키지 않음
- 2가지를 처리
    1. 현재 요청에 대한 session data를 DB에서 삭제
    2. 클라이언트의 쿠키에서도 sessionid를 삭제
    - 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 데이터에 액세스하는 것을 방지하기 위함

### urls.py

```python
# accounts/urls.py

from django.urls import path
from. import views

app_name = 'accounts'
urlpatterns = [
    ...
    path('logout/', views.logout, name='logout'),
    ...
    ]
```

```python
# accounts/views.py
from django.contrib.auth import logout as auth_logout

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

```html
{% base.html %}
...
<form action="{% url 'accounts:logout' %}" method="POST">
  {% csrf_token % }
  <input type="submit" value="Logout">
</form>
...
```