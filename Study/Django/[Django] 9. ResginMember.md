# Django_ResignMember

# 회원 탈퇴

> DB에서 유저를 delete하는 것과 같음
> 

### urls.py

```python
# accounts/urls.py

from django.urls import path
from. import views

app_name = 'accounts'
urlpatterns = [
    ...
    path('delete/', views.delete, name='delete'),
    ...
    ]
```

### views.py

- 탈퇴하면서 해당 유저의 세션 정보도 함께 삭제를 원할 경우
    - auth_logout(request)를 사용하여 세션 정보 삭제
- auth_logout(request)를 먼저 작성할 경우
    - request에 담겨있던 객체(유저) 정보가 사라지기에 회원 탈퇴에 필요한 정보 또한 없어지기 때문

```python
# accounts/views.py

...
def delete(request):
    request.user.delete()
    auth_logout(request) # 삭제 이후 계정 로그 아웃
    return redirect('articles:index')
...
```

### base.html

```html
{% templates/base.html %}

<form action="{% url 'accounts:delete' %}" method="POST">
	{% csrf_token %}
	<input type="submit" value="회원탈퇴">
</form>
```