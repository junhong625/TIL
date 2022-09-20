# Django_SignUp

# 회원 가입

> User를 Create하는 것이며 UserCreationForm built-in form을 사용
> 

### UserCreationForm

> 주어진 username과 password로 권한이 없는, 새 user를 생성하는 ModelForm
> 
- 필드
    - username
    - password1
    - password2

### urls.py

```python
# accounts/views.py

from django.urls import path
from. import views

app_name = 'accounts'
urlpatterns = [
    ...
    path('signup/', views.signup, name='signup'),
    ...
    ]
```

### forms.py 생성

- get_user_model() 사용 이유
    - django에서는 직접 참조를 권장하지 않음

```python
# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm): # 기본 UserCreationForm 상속
    
    class Meta(UserCreationForm.Meta):# UserCreationForm.Meta 상속
        model = get_user_model() # 간접 참조하기 위한 함수를 사용
        fields = UserCreationForm.Meta.fields + ('email',)
```

### views.py

- form에서 제공해주는 UserCreationForm을 사용하면 User가 변경되었기에 오류 발생

```python
# accounts/views.py
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 유효성 검사 실시
            user = form.save()
            auth_login(request, user) # 바로 로그인 적용
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)
```

### singup.html

```html
# templates/accounts/singup.html

{% extends 'base.html' %}

{% block content %}
    <h1>SIGNUP</h1>
    <form action="{% url 'accounts:signup' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock content %}
```

### base.html

```html
...
<a href="{% url 'accounts:signup' %}">Signup</a>
...
```