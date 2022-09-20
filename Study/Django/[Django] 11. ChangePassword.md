# Django_ChangePassword

> Django에서 기본적으로 제공해주는 PasswordChangeForm을 사용
> 

### PasswordChangeForm

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변경
- SetPasswordForm을 상속 받는 클래스

### 회원 정보 수정(update) 페이지의 폼 button

> 폼을 클릭 시 `/accounts/password/`로 이동
> 
- 자동적으로 PasswordChangeForm에 설정된 주소로 이동
    - 이러한 이유로 인해 회원과 관련한 앱의 name을 accounts로 하는 것을 권장

### urls.py

```python
# accounts/urls.py

from django.urls import path
from. import views

app_name = 'accounts'
urlpatterns = [
    ...
    path('password/', views.change_password, name='change_password'),
    ...
]
```

### views.py

- `update_session_auth_hash(request, user)`
    - 이 함수를 사용하지 않는다면 비밀번호가 변경되면서 session에 존재하는 기존의 유저 정보와 달라지기 때문에 자연스럽게 로그아웃이 됨
    - 하지만 `update_session_auth_hash()`을 사용하여 변경 사항을 세션에 반영한다면 로그인이 그대로 유지될 수 있음
    - 아래의 예시에서는 form.user로 유저의 정보를 함수에 할당해줬지만 이렇게 할 경우 관리자가 유저의 비밀번호를 변경하면 관리자 계정이 로그아웃되는 상황이 발생
        - 이는 request에 들어오는 user의 정보와 form.user를 통해 들어오는 user정보가 다르기 때문 따라서 form.user가 아닌 request.user를 사용하면 이러한 문제를 해결 가능

```python
# accounts/views.py

from django.contrib.auth.forms import PasswordChangeForm
from djnago.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) 
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)
```

### change_password.html

```html
{% templates/accounts/change_password.html %}

{% extends 'base.html' %}

{% block content %}
    <h1>비밀번호 변경</h1>
    <form action="{% url 'accounts:change_password' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock content %}
```